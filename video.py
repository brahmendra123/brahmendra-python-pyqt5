# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_video(object):
    def setupUi(self, video):
        video.setObjectName("video")
        video.resize(760, 560)
        self.label = QtWidgets.QLabel(video)
        self.label.setGeometry(QtCore.QRect(50, 60, 651, 321))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(video)
        self.start.setGeometry(QtCore.QRect(520, 410, 75, 23))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(video)
        self.stop.setGeometry(QtCore.QRect(610, 410, 75, 23))
        self.stop.setObjectName("stop")

        self.retranslateUi(video)
        QtCore.QMetaObject.connectSlotsByName(video)

    def retranslateUi(self, video):
        _translate = QtCore.QCoreApplication.translate
        video.setWindowTitle(_translate("video", "Form"))
        self.start.setText(_translate("video", "Start"))
        self.stop.setText(_translate("video", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    video = QtWidgets.QWidget()
    ui = Ui_video()
    ui.setupUi(video)
    video.show()
    sys.exit(app.exec_())
