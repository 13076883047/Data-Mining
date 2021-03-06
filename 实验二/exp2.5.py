# 5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔

import pandas as pd 
import numpy as np          
import seaborn as sn        
import math     
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',None)     # 显示全部行
pd.set_option('display.max_colum',None)    #  显示全部列

def mean_list(list)->float:    ## 返回列表的平均值，计算时跳过空缺值
    sum = float(0)
    n = float(len(list))
    for num in list:
        if math.isnan(num):
            n -= 1
            continue
        sum += num
    # list 中没有有效值
    if n == 0:
        return float('nan')
    mean = sum / n  
    return mean 

def SD_list(list,mean):
    '''
    返回列表的标准差，计算时跳过空缺值
    '''   
    #均值为nan直接返回nan
    if math.isnan(mean):
        return float('nan')
    
    sumX2=float(0)
    n = float(len(list))
    for num in list:
        #跳过空缺值
        if math.isnan(num):
            n-=1
            continue
        sumX2 += pow(num,2)
    
    SD_list = math.sqrt(sumX2/n - pow(mean,2))

    return SD_list

def z_score(df,colList=None):

    #如果没有给出列名则对整个dataframe作z-score归一化
    if colList is None:
        #获取dataframe列名列表
        colLabel = df.columns.values.tolist() 
        for label in colLabel:
            cList = df[label].tolist()
            cMean = mean_list(cList)
            cSD = SD_list(cList,cMean)
            cList = df[label].tolist()
            rowIndex = df.index.values.tolist()
            i=0
            for index in rowIndex:
                new_num = round((cList[i]-cMean)/cSD,5)
                i+=1
                df.loc[index,label] = new_num
        return

    #否则只对指定列进行z-score归一化
    for label in colList:
        cList = df[label].tolist()
        cMean = mean_list(cList)
        cSD = SD_list(cList,cMean)
        df[label].fillna(cMean,inplace=True)
        cList = df[label].tolist()
        rowIndex = df.index.values.tolist()
        i=0
        for index in rowIndex:
            new_num = round((cList[index]-cMean)/cSD,5)
            i+=1
            df.loc[index,label] = new_num
    return

def corMatrix(df):
    colLabels  = df.columns.values.tolist()
    #列数量,这里做维度
    dimension = df.shape[1] 
    #行数量,这里做样本数量 
    sampleNum = df.shape[0] 
    #用于存储每个维度平均值的list
    col_mean = []          
    #求每个列的平均值,调用mean_list(list)函数
    for column in colLabels:
        c_mean = mean_list(df[column].values.tolist())
        col_mean.append(round((c_mean),8))
    #开始求相关矩阵
    correlationMatrix = []
    for i in range(dimension):
        valuesRow = []
        for j in range(dimension):
            icol = df.iloc[:,i].tolist()
            jcol = df.iloc[:,j].tolist()
            for k in range(sampleNum):
                icol[k] = round(icol[k]-col_mean[i],7)
                jcol[k] = round(jcol[k]-col_mean[j],7)
            result = 0
            for index in range(sampleNum):
                result+=icol[index]*jcol[index]
            result = round(result/(sampleNum-1),6)
            valuesRow.append(result)
        correlationMatrix.append(valuesRow)

    return correlationMatrix

if __name__ == '__main__':
    
    #读取合并后的数据
    df = pd.read_csv('D:\大三上\数据挖掘\data.csv')
    
    #去除完全空缺的列
    isnan = df.isnull().all()
    dropCol = isnan[isnan.values==True].index.tolist()
    df.drop(columns=dropCol,inplace=True)

    #提取成绩数值数据
    dfScore = df.iloc[:,5:16]

    #z-score归一化
    z_score(dfScore)

    #进行矩阵的转置
    dfScore = dfScore.T

    #将转置后的矩阵列名类型转换为string
    dfScore.columns = dfScore.columns.map(str)

    #再对矩阵进行z-score归一化
    z_score(dfScore)
    # print(dfScore)

    resultMatrix = corMatrix(dfScore)
    nprm = np.array(resultMatrix)
    dfresult = pd.DataFrame(data = nprm)
    #print(dfresult)

    
    row = dfresult.shape[0]
    col = dfresult.shape[1]
    list_b = [[0 for i in range(3)] for j in range(row)]  
    list_c = [[0 for i in range(3)] for j in range(row)]
    for r in range(row):
        for c in range(col):
           if r != c:
               if dfresult[r][c] > list_b[r][0]:
                   list_b[r][0] = dfresult[r][c]
                   list_c[r][0] = df['ID'][c]
               elif dfresult[r][c] > list_b[r][1]:
                   list_b[r][1] = dfresult[r][c]
                   list_c[r][1] = df['ID'][c]
               elif dfresult[r][c] > list_b[r][2]:
                   list_b[r][2] = dfresult[r][c]
                   list_c[r][2] = df['ID'][c]

    #print(list_b)
    su = np.array(list_b)   
    su_c = np.array(list_c) 
   # print(su)   
    dfsu = pd.DataFrame(data = su)   
    dfsu_c = pd.DataFrame(data = su_c)   
    print(dfsu_c)  
    dfsu_c.to_csv('D:\大三上\数据挖掘\exp2.5.txt',sep = "\t")
   # print(df['ID'][1])