#/usr/bin/python
#encoding:utf-8
import csv
import os
import time


class App():
    def __init__(self):

        self.starttime = 0
        self.content = ""

    #启动应用
    def LaunchApp(self):
        cmd = "adb shell am start -W -n com.rcplatform.livechat/.ui.MainActivity"
        #localtime = time.time()
        self.content = os.popen(cmd)
        return self.content
    #停止应用
    def StopApp(self):
        #冷启动
        cmd = "adb shell am force-stop com.rcplatform.livechat"
        #热启动
        #cmd = "adb shell input keyevent 3"
        os.popen(cmd)
    #获取启动时长
    def GetLaunchAppTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.starttime =line.split(":")[1]
                break
        return self.starttime


class Controller():
    def __init__(self,count):
        self.testApp = App()
        self.count = count
        self.alldata = [("timestmap","elapsetime")]
    #单次执行过程
    def TestProcess(self):
        self.testApp.LaunchApp()
        time.sleep(3)
        elapsetime = self.testApp.GetLaunchAppTime()
        self.testApp.StopApp()
        time.sleep(1)
        timestmap = self.GetCurrentTime()
        self.alldata.append((timestmap,elapsetime))
    #多次运行
    def run(self):
        while self.count > 0:
            self.TestProcess()
            self.count = self.count -1
    #获取时间戳
    def GetCurrentTime(self):
        currenttime = time.strftime("%Y-%M-%D %H:%M:%S",time.localtime())
        return currenttime

    def SaveDataToCSVFile(self):
        #冷启动时间
        csvfile = open("start_cold_time.csv","w")
        #热启动时间
        #csvfile = open("start_hot_time.csv", "w")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSVFile()