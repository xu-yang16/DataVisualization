#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False   

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#plt.legend(labels = ('男孩','女孩'),loc='upper left')
plt.scatter(grades_range, girls_grades, color='r', alpha=0.5)
plt.scatter(grades_range, boys_grades, color='b', alpha=0.5)

plt.title('散点图示例')#显示图表标题
plt.xlabel('分数范围')#x轴名称
plt.ylabel('分数等级')#y轴名称
plt.grid(False)#显示网格线
plt.legend(labels = ('男孩','女孩'),loc='upper right')
plt.savefig('./ScatterPlot.png')
plt.show()
