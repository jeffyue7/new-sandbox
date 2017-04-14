from PyQt4 import QtGui, QtCore
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
import scipy
from scipy import misc

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    l = misc.face()
    p = QtGui.QLabel()
    q = QtGui.QPixmap.fromImage(ImageQt(scipy.misc.toimage(l)))
    p.setPixmap(q)
    p.show()
    app.exec_()