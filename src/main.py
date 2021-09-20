import sys
import os
from ui_main import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import urllib.request
import requests
import time
from tkinter import *
from json import loads
from ui_about import *
import traceback2 as traceback
from ui_help import Ui_Dialog as Ui_Dialogs

win = None
info = {}

print(sys.argv)

class Docs(QDialog, Ui_Dialogs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

class DocsThread(QThread):
    def __init__(self):
        super().__init__()
        window = Docs()
        window.exec()

def Download():
    global win
    global info
    win.progressBar.setValue(1)
    try:
        req = requests.get(f'http://www.kuwo.cn/url?format=mp3&rid={info["rid"]}&response=url&type=convert_url3&br=128kmp3&from=web&t=1611321054772&httpsStatus=1&reqId=4265a0b0-5cb3-11eb-8d35-9939327ef0bf')
        url = loads(req.text)["url"]
        with open(win.savePath.text(),"wb") as f:
            with urllib.request.urlopen(url) as r:
                f.write(r.read())
        QMessageBox.information(win,"提示","歌曲下载完成")
    except:
        e=traceback.format_exc()
        QMessageBox.critical(win,"错误",e)
        
    win.progressBar.setValue(100)
        
class AboutUs(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.fk)
        self.show()
    def fk(self):
        if os.system("start firefox.exe https://community.itcraft.tk/bbs/send.html") == 1:
            if os.system("start msedge.exe https://community.itcraft.tk/bbs/send.html") == 1:
                if os.system("start chrome.exe https://community.itcraft.tk/bbs/send.html") == 1:
                    QMessageBox.critical(self,"错误","找不到可用浏览器，请自行访问<a href=\"https://community.itcraft.tk/bbs/send.html进行反馈！\">")

class abouThread(QThread):
    def __init__(self):
        super().__init__()
        window = AboutUs()
        window.exec()

def get():
    global win
    global info

    win.sendButton.setEnabled(False)
    win.label_3.setText('准备状态：<span style="color:blue">获取中</span>')
    info["rid"] = str(str(win.urlEdit.text()).split("/")[-1])
    try:
        info["name"] = loads(requests.get(f"http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={info['rid']}&httpsStatus=1&reqId=0ddeda60-fc3f-11eb-bde0-ed219a74e4bd").text)['data']['lrclist'][0]['lineLyric']
        info["name_type"] = 0
    except:
        info["name"] = "未知"
        info["name_type"] = 1

    print(info)

    win.musicId.setText(f"音乐ID：{str(info['rid'])}")
    win.musicName.setText(f"歌曲名：{str(info['name'])}")
    win.label.setText(f'试听链接：<a href="http://kuwo.cn/play_detail/{info["rid"]}">点击试听</a>')
    win.label_3.setText('准备状态：<span style="color:green">就绪</span>')
    win.sendButton.setEnabled(True)
    win.startDown.setEnabled(True)
    
    path = ""
    for i in sys.argv[0].split("\\")[:-1]:
        path += i
        path += "\\"
    
    if info["name_type"] == 0:
        win.savePath.setText(str(path)+info["name"]+".mp3")
    else:
        win.savePath.setText(str(path)+"未知音乐-"+info["rid"]+".mp3")
    win.pushButton.setEnabled(True)
    

class Thread(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        global win
        global getinfo
        while True:
            if win.urlEdit.text() != "":
                win.sendButton.setEnabled(True)
            else:
                win.sendButton.setEnabled(False)

class Kuwo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global win
        super().__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.getinfo)
        self.actionGo_to_kuwo_cn.triggered.connect(self.gotokuwo)
        self.actionGo_to_itcraft_tk.triggered.connect(self.gotohome)
        self.actionAbout_Us.triggered.connect(self.about)
        self.startDown.clicked.connect(self.start)
        self.pushButton.clicked.connect(self.chooie)
        self.actionExit.triggered.connect(self.quit)
        self.actionDocs.triggered.connect(self.docs)
        
        self.startDown.setEnabled(False)
        self.savePath.setText(str(sys.argv[0]))
        self.pushButton.setEnabled(False)
        self.show()

        # 初始化
        win = self
        self.Thread = Thread()      # send按钮启禁用线程
        self.Thread.start()
    
    def docs(self):
        self.doc = DocsThread()
        self.doc.start()
    
    def quit(self):
        sys.exit()
    
    def chooie(self):
        dialog = QFileDialog(self,"选择保存路径")
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("音频文件(*.mp3)")
        if dialog.exec():
            fileNames = dialog.selectedFiles()[0]
            print(fileNames)
            if ".mp3" in fileNames:
                self.savePath.setText(fileNames)
            else:
                self.savePath.setText(fileNames + ".mp3")

    def start(self):
        Download()

    def getinfo(self):
        print("Get Music Info")
        get()

    def gotokuwo(self):
        os.popen("start www.kuwo.cn")

    def gotohome(self):
        os.popen("start www.itcraft.tk")

    def about(self):
        self.about = abouThread()
        self.about.start()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Kuwo()
    sys.exit(app.exec())
