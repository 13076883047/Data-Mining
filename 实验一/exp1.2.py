import pandas as pd
import copy

def question_1(data,count):     # 家乡为Beijing的所有课程的平均成绩
    answer1 = []     # 结果
    temp = []        # 暂存学生数据
    i = 0
    while i < count:
        if data.loc[i]['City'] == 'Beijing':
            temp.append(data.loc[i]['ID'])
            temp.append(data.loc[i]['Name'])
            aver_Grade = (data.loc[i]['C1'] + data.loc[i]['C2'] + data.loc[i]['C3'] + data.loc[i]['C4'] + data.loc[i]['C5'] +
                          data.loc[i]['C6'] + data.loc[i]['C7'] + data.loc[i]['C8'] + data.loc[i]['C9'] + data.loc[i]['C10']) / 10    # 求所有科目的平均分
            temp.append(aver_Grade)
            a = copy.deepcopy(temp)
            answer1.append(a)
            temp.clear()
        i += 1
    print("家乡为Beijing的学生所有课程的平均成绩：\n", answer1)


def question_2(data,count):
    #学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量---问题二
    boy_Gz = 0
    i = 0
    while i < count:   
        if d.loc[i]['City'] == 'Guangzhou' and d.loc[i]['Gender']=='male' and d.loc[i]['C1'] > 80 and d.loc[i]['C9']>90:
            boy_Gz += 1
        i += 1
    print("家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量:",boy_Gz)



def question_3(data,count):  # 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强
    count_Gz = 0      # 统计广州女生人数
    count_Sh = 0      # 统计上海女生人数
    Grade_Gz = 0      # 广州女生的体育成绩
    Grade_Sh = 0      # 上海女生的体育成绩
    
    i = 0
    while i < count:
        if d.loc[i]['City'] == 'Guangzhou' and d.loc[i]['Gender'] == 'female':
            count_Gz += 1
            Grade_Gz += d.loc[i]['Constitution']
        if d.loc[i]['City'] == 'Shanghai' and d.loc[i]['Gender'] == 'female':
            count_Sh += 1
            Grade_Sh += d.loc[i]['Constitution']
        i += 1
    aver_Gz = Grade_Gz / count_Gz
    aver_Sh = Grade_Sh / count_Sh
    print("广州女生平均体能测试成绩:",aver_Gz)
    print("上海女生平均体能测试成绩:",aver_Sh)
    if aver_Gz > aver_Sh:
        print("广州女生的平均体能测试成绩更好")
    elif aver_Sh > aver_Gz:
        print("上海女生的平均体能测试成绩更好")
    else:
        print("广州上海女生平均体能成绩一样好")

def mean(data,lesson):   # 求平均值
    sum = 0
    row = data.shape[0]
    for i in range(row):
        sum += data[lesson][i]
    mean_sum = sum / row   # 均值
    return mean_sum

def SD(data,lesson):  # 求标准差
    sd_x = 0         #协方差
    sd_b = 0         #标准差
    sum_xi = 0       
    sum_xi_2 = 0 
    
    row =data.shape[0]
    for i in range(row):
        sum_xi += data[lesson][i]
        sum_xi_2 += data[lesson][i]**2

    sd_x = (sum_xi_2 - sum_xi*sum_xi/(row+1)) / row         # 求协方差
    sd_b = sd_x ** 0.5                                      # 标准差 等于 协方差开平方

    return sd_b

def ak(data,lesson):       # 课程C1-C10
    row = data.shape[0]
    list_a = {}
    mean_sum = mean(data,lesson)
    sd_sum = SD(data,lesson)
    for i in range(row):
        list_a[i] = (data[lesson][i] - mean_sum) / sd_sum     # （科目成绩-科目平均成绩）/标准差

    return list_a

def bk(data):                    
    # 求体侧成绩平均成绩和标准差，最后返回 list_b[] = （体侧成绩-体侧成绩平均值）/ 标准差
    # list_b[] 用于求与各科成绩的相关性
    row = data.shape[0]     
    list_b = {}
    mean_sum = mean(data,'Constitution')          # 平均值
    sd_sum = SD(data,'Constitution')              # 标准差
    for i in range(row):
        list_b[i] = (data['Constitution'][i]-mean_sum) / sd_sum

    return list_b

def question_4(data,lesson):      # 学习成绩和体能成绩测试，两者相关性是多少，九门课的成绩分别与体能成绩计算相关性
    dependence_sum = 0
    list_a = ak(data,lesson)
    list_b = bk(data)                            
    row = data.shape[0]
    for i in range(row):
        dependence_sum += list_a[i] * list_b[i]    # 相关性

    print(" 课程 '%s' and 课程 'Constitution 的相关性是' is:%f" %(lesson,dependence_sum))




if __name__ =='__main__':
    d = pd.read_csv('D:\大三上\数据挖掘\data.csv')
    d = d.fillna(0)
    length = len(d)   #学生人数

    question_1(d,length)

    question_2(d,length)

    question_3(d,length)

    question_4(d,'C1')
    question_4(d,'C2')
    question_4(d,'C3')
    question_4(d,'C4')
    question_4(d,'C5')
    question_4(d,'C6')
    question_4(d,'C7')
    question_4(d,'C8')
    question_4(d,'C9')