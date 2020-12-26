# 1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
import pandas as pd   
import matplotlib.pyplot as plt   

df = pd.read_csv("D:\大三上\数据挖掘\data.csv")

x = df['C1'].values
y = df['Constitution'].values
plt.scatter(x,y) 
plt.xlabel('C1 Score')                  # x轴参数
plt.ylabel('Constitution')              # y轴参数
plt.savefig('D:\大三上\数据挖掘\exp2.1.png',bbox_inches='tight')
plt.show()