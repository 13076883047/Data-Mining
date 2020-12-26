# 2. 以5分为间隔，画出课程1的成绩直方图

import numpy as np                    
import pandas as pd                   
import matplotlib.pyplot as plt                    
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('D:\大三上\数据挖掘\data.csv')

# 取出C1列
c1 = df['C1'].values

# 对取出的数组进行排序
c1Sorted = np.sort(c1)   # 升序

# 找到最大、最小值
length = len(c1) 
c1min = c1Sorted[0]     # 第一个值
c1max = c1Sorted[length-1]    # 最后一个值
# c1max =c1Sorted[-1]   # 同样可以表示为最后一个值，即最大值

# x轴单位划分
start = 10*(c1min//10)
end = 10*(c1max//10)+1
bins = np.arange(start,end,5) # 5分一个间隔   

# 作图
(n,bins,patches) = plt.hist(c1Sorted,bins,alpha = 0.6)  # hist（数据,条形数,透明度）
x= np.arange(start+5/2,end-5/2,5)

# 给hist图添加数值
for i,v in enumerate(n):
    plt.text(x[i],v,str(int(v)),horizontalalignment='center')

# 给图加标题
plt.title('C1分数区间统计')

# 保存图
plt.savefig('D:\大三上\数据挖掘\exp2.2.png',bbox_inches='tight')

plt.show()