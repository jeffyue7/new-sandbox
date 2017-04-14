import ui_main
import sys
from PyQt4 import QtCore, QtGui

import sys
from PyQt4 import Qt
import PyQt4.Qwt5 as Qwt
from PIL import Image
import numpy
import time

spectroWidth=1000
spectroHeight=1000

a=numpy.random.random(spectroHeight*spectroWidth)*255
a=numpy.reshape(a,(spectroHeight,spectroWidth))
a=numpy.require(a, numpy.uint8, 'C')

COLORTABLE=[]
for i in range(256): COLORTABLE.append(QtGui.qRgb(i/4,i,i/2))

def updateData():
    global a
    a=numpy.roll(a,-5)
    QI=QtGui.QImage(a.data, spectroWidth, spectroHeight, QtGui.QImage.Format_Indexed8)
    QI.setColorTable(COLORTABLE)
    uimain.label.setPixmap(QtGui.QPixmap.fromImage(QI))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win_main = ui_main.QtGui.QWidget()
    uimain = ui_main.Ui_win_main()
    uimain.setupUi(win_main)

    # SET UP IMAGE
    uimain.IM = QtGui.QImage(spectroWidth, spectroHeight, QtGui.QImage.Format_Indexed8)
    uimain.label.setGeometry(QtCore.QRect(0,0,spectroWidth,spectroHeight))
    uimain.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0,0,spectroWidth,spectroHeight))

    # SET UP RECURRING EVENTS
    uimain.timer = QtCore.QTimer()
    uimain.timer.start(.1)
    win_main.connect(uimain.timer, QtCore.SIGNAL('timeout()'), updateData)

    ### DISPLAY WINDOWS
    win_main.show()
    sys.exit(app.exec_())