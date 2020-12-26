##  两个数据源合并后读入内存，并统计

from numpy.core.defchararray import index
import pandas as pd        # python 数据分析模块
import numpy as np                                       
import math
pd.set_option('display.max_rows',None)          # 显示所有行

# 性别统一： 男(boy)->male  女(girl)->female
def gen(gender):
    if gender == 'boy':
        return 'male'
    elif gender == 'girl':
        return 'female'
    else:
        return gender


# 体测成绩百分制
def peScore(pe):
    if pe == 'excellent':
        return 90
    elif pe == 'good':
        return 80
    elif pe =='general':
        return 70
    elif pe =='bad':
        return 60
    elif pe=='':
        return np.NaN


# 身高统一使用 米 为单位
def height(height):
    h = float(height)
    if h>100:              # 厘米为单位的身高除以100
        h=h/100.0
        return h
    else:
        return h

# C6-C10 十分制课程 转 百分制
def tenTimes(score):
    if score=='':
        return score
    s=float(score)*10
    return s

def tptoPer(df):
    df['C6'] =df['C6'].apply(tenTimes)
    df['C7'] =df['C7'].apply(tenTimes)
    df['C8'] =df['C8'].apply(tenTimes)
    df['C9'] =df['C9'].apply(tenTimes)
    df['C10'] =df['C10'].apply(tenTimes)


# 合并处理函数
def dupMerge(dataframe):
    '''
    合并处理函数,仅保留重复的第一个值,如果行中有空缺则向重复行寻找
    '''
    df=dataframe          # dataframe 以命名列方式的分布式数据集

    # 根据IP排序
    # DataFrame.sort_values（by，axis = 0，ascending = True，inplace = False，kind = ' quicksort '，na_position = 'last'，ignore_index = False，key = None）

    df.sort_values(by='ID',inplace = True, ascending = True)   # 按照某一列的大小进行升序排序

    # 去除完全重复的行
    df = df.drop_duplicates(keep='first')    # 保留第一次出现的数据

    # 重设index
    df = df.reset_index(drop=True)

    # 定位'ID'重复的位置，位置存入 dupStartList=>List
    idcol = df['ID']
    oneDup = idcol.drop_duplicates(keep='first')    # 保存第一次出现的重复行
    notDup = idcol.drop_duplicates(keep = False)    # 删除所有重复项
    dupStart = oneDup.append(notDup).drop_duplicates(keep=False)

    # 所有重复数据的起始处保存为列表List
    dupStartList = dupStart.index.tolist()

    # 取列数
    col = df.shape[1]

    # 处理'ID'重复的数据
    for row in dupStartList:
        dupStart = opFlag = row
        dupEnd = row
        # 找到重复区间，dupEnd为重复结束index
        while df.iloc[dupEnd,0] == df.iloc[dupEnd+1,0]:
            dupEnd = dupEnd + 1
        # 如果出现空值，则向下寻找非空值
        for c in range(col):
            if pd.isna(df.iloc[dupStart,c]):
                while dupEnd - opFlag >0:
                    opFlag = opFlag + 1
                    if not pd.isna(df.iloc[opFlag,c]):
                        df.iloc[dupStart,c] = int(df.iloc[opFlag,c])
                        break

    # 处理结束后，去除其他重复行
    df = df.drop_duplicates(subset=['ID'],keep = 'first')

    # 重设index
    df = df.reset_index(drop = True)

    return df


 ## 返回列表的平均值，计算时跳过空缺值
def mean_list(list)->float:  
    sum = float(0)
    n = float(len(list))
    for num in list:
        # 跳过空缺值
        if math.isnan(num):
            n-=1
            continue
        sum += num
    # list 中没有有效值
    if n==0:
        return float('nan')
    mean = sum / n
    return mean

    
def fillNaN(df):
    cLabels = df.columns.values.tolist()[5:16]
    for label in cLabels:
        cList =df[label].tolist()
        cMean =mean_list(cList)
        if math.isnan(cMean):
            continue
        df[label].fillna(cMean,inplace = True)


if __name__ =='__main__':
    converters={'Gender':lambda x:gen(x),'Height':lambda x: height(x),'Constitution':lambda x:peScore(x)}

    # df1
    df1 = pd.read_table('D:\大三上\数据挖掘\data2.txt',sep=',',converters=converters)
    
    tptoPer(df1)
    df1 =dupMerge(df1)

    # df2
    df2 = pd.read_excel('D:\大三上\数据挖掘\data1.xlsx',converters=converters)

    # 学生ID处理函数
    def compID(id):
        x = int(id)
        return 202000+x

    df2['ID'] = df2['ID'].apply(compID)
    tptoPer(df2)
    df2=dupMerge(df2)


    # df
    # 合并两个表
    df = pd.concat([df1,df2],ignore_index=True)
    df = dupMerge(df)

    # 将空缺处填上该列均值
    fillNaN(df)

    # 最终合并的dataframe => 'df
    print(df)

    #将结果保存到csv中
    df.to_csv('D:\大三上\数据挖掘\data.csv',index=False)

    print("Done")
