import pyqtgraph as pg
import numpy as np
import array

app = pg.mkQApp()
data = array.array('d') #可动态改变数组大小, double型数组
N = 200                 #一屏可显示的数据点数
win = pg.GraphicsWindow()
win.setWindowTitle(u'pyqtgraph逐点画波形图')
win.resize(500,300)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0,N-1], yRange=[-1.2,1.2], padding=0)
p.setLabels(left='y / V', bottom='x / point', title='y = sin(x)')

curve = p.plot(pen='y')
idx=0

def plotData():
    global idx
    tmp = np.sin(np.pi / 50 * idx)
    if len(data) < N:
        data.append(tmp)
    else:
        data[:-1] = data[1:]
        data[-1] = tmp
    
    curve.setData(data)
    idx +=1


if __name__ == "__main__":
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(plotData)
    # 连接定时器, 每30ms刷新一次
    timer.start(30)

    app.exec_()
