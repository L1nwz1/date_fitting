from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg

#拟合函数
def fund(x,a,b,c):
    return a*x**2 + b*x + c

x = [10, 20, 30, 40, 50, 60, 70, 80]
x2 = np.arange(10, 80, 0.001)
y = [0.1, 0.3, 0.7, 0.94, 0.95, 0.68, 0.34, 0.13]
fig,ax=plt.subplots()
popt, pcov=curve_fit(fund, x, y)
#popt数组中，三个值分别是待求参数a,b,c
p1 = np.poly1d(popt) #生成拟合多项式
xxx = np.arange(10, 80, 0.001) #定义以0.01为单位的横坐标间隔集合
yvals = p1(xxx) #将每个横坐标代入拟合函数终
plt.xlabel('T') #横坐标为温度T
plt.ylabel('y') #纵坐标为转化率y
ax.plot(x,y,'b-') #画出初始图像
ax.legend(r'$original\ values$')
y2 = [fund(xx,popt[0],popt[1],popt[2]) for xx in x2]
ax.plot(x2,y2,'r--') #画出拟合后图像
ax.legend(r'$polyfit\ values$')
maxi = sg.find_peaks(yvals)[0] #maxi表示极值点在数组中的位置
print(xxx[maxi])#xxx[maxi]表示极值点，小数点保留后两位
print(yvals[maxi])#yvals[maxi]表示对应的极值

plt.show()