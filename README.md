﻿# Data-Mining
组员信息：区景祥 
参考并致谢：https://github.com/HOLL4ND/DataMining-Experiment
　　　　　　　　　　　　　　　　　　　　　　  数据挖掘实验
                                                        
                                                         实验一
广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在数据库中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。
数据库表：ID (int), 姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。
txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。
两个数据源合并后读入内存，并统计：
1. 学生中家乡在Beijing的所有课程的平均成绩。
2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

                                                        实验二
基于实验一中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言，编程计算：
1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2. 以5分为间隔，画出课程1的成绩直方图。
3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4. 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔

                                                         实验三                                                     
1. 对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？
2. 由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。
现有样例(x,y)数据对，
x	3.45	1.76	4.29	3.35	3.17	3.68	2.11	2.58	3.45	6.17	4.2	5.87	5.47	5.97	6.24	6.89	5.38	5.13	7.26	6.32
y	7.08	7.24	9.55	6.65	6.41	5.99	4.08	7.1	7.88	5.4	6.46	3.87	2.21	3.62	3.06	2.41	2.32	2.73	4.19	3.62
找到聚类中心后，判断(2,6)是属于哪一类？

k-means算法主要思想：
1. 从文件读取数据，点用元组表示，点集用列表表示
2. 初始化聚类中心，获得数据的长度length->在range(0,length)这个区间上随机产生k个不同的值，以此为下标提出数据点，作为聚类初始中心点。
3. 分配数据点，将数据点分配到距离最短的聚类中心点
4. 如果首次分配有结果为空，则重新初始化聚类中心
5. 更新聚类中心，计算每一簇中所有点的平均值，然后再次进行分配并计算平均误差
6. 比较前两次的平均误差是否相等，若不相等则进行循环，否则终止循环，进入下一步
7. 最少进行两次聚类，对比误差，输出较小误差时的结果。


实验一文件夹：exp1.1 合并数据  exp1.2：统计实验要求数据
实验二文件夹：exp2.1 exp2.2 exp2.3 exp2.4 exp2.5分别对应实验二第一、第二、第三、第四个、第五个要求   


实验一用到的库函数：
from numpy.core.defchararray import index        

import pandas as pd
在Python中，pandas是基于NumPy数组构建的，使数据预处理、清洗、分析工作变得更快更简单。pandas是专门为处理表格和混杂数据设计的，而NumPy更适合处理统一的数值数组数据。
pandas 两个主要的数据结构：Series 和 DataFrame，本实验主要用DataFrame
      
import numpy as np
用于大量维度数组与矩阵运算

import math
math.isnan() 用于检查数字是否为NaN，如果为NaN则返回True，否则False

import copy  
copy.deepcopy() 

实验二用到的库函数：

import numpy as np                    
import pandas as pd  
import math  
import seaborn as sn               用于绘图，seaborn是在matplotlib的基础上进行更高级的封装

import matplotlib.pyplot as plt    用于绘图


实验三用到的库函数:

import numpy as np          
import pandas as pd    
import copy 
import pickle     # 实验数据二进制序列化和反序列化

import random     # 随机数

import matplotlib.pyplot as plt    
from math import sqrt  # 平方根计算