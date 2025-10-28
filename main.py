from m5stack import *
from m5ui import *
from uiflow import *
import math
import ntptime
import wifiCfg
wifiCfg.autoConnect(lcdShow=False)
pi = math.pi
ntp = ntptime.client(host='ntp.nict.jp', timezone=9)
setScreenColor(0x000000)


def Watch_BG(center):
    r = 70
    M5Circle(center[0], center[1], r, 0xFBFBFB, 0xFBFBFB)
    for i in range(12):
        if (i % 3 == 0):
            dot_r = int(r / 16)
        else:
            dot_r = int(r / 32)
        M5Circle(int(center[0] + r * 16 / 20 * math.sin(i * pi * 2 / 12)),
                 int(center[1] + r * 16 / 20 * math.cos(i * pi * 2 / 12)),
                 dot_r, 0x0b0b0b, 0x0b0b0b)


def Watch_Needle(center, r, nowTime):
    M5Triangle(
        int(center[0] - r / 2 * math.sin(-(nowTime[0] %
            12 + nowTime[1] / 60) / 12 * pi * 2)),
        int(center[1] - r / 2 * math.cos(-(nowTime[0] %
            12 + nowTime[1] / 60) / 12 * pi * 2)),
        int(center[0] - r / 20 * math.sin(-(nowTime[0] %
            12 + nowTime[1] / 60) / 12 * pi * 2 + pi / 2)),
        int(center[1] - r / 20 * math.cos(-(nowTime[0] %
            12 + nowTime[1] / 60) / 12 * pi * 2 + pi / 2)),
        int(center[0] - r / 20 * math.sin(-(nowTime[0] %
            12 + nowTime[1] / 60) / 12 * pi * 2 - pi / 2)),
        int(center[1] - r / 20 * math.cos(-(nowTime[0] %
            12 + nowTime[1] / 60) / 12 * pi * 2 - pi / 2)),
        0x0b0b0b, 0x0b0b0b)
    M5Triangle(
        int(center[0] - r * 4 / 5 * math.sin(-nowTime[1] / 60 * pi * 2)),
        int(center[1] - r * 4 / 5 * math.cos(-nowTime[1] / 60 * pi * 2)),
        int(center[0] - r / 20 * math.sin(-nowTime[1] / 60 * pi * 2 + pi / 2)),
        int(center[1] - r / 20 * math.cos(-nowTime[1] / 60 * pi * 2 + pi / 2)),
        int(center[0] - r / 20 * math.sin(-nowTime[1] / 60 * pi * 2 - pi / 2)),
        int(center[1] - r / 20 * math.cos(-nowTime[1] / 60 * pi * 2 - pi / 2)),
        0x0b0b0b, 0x0b0b0b)
    M5Circle(center[0], center[1], int(r / 14), 0x0b0b0b, 0x0b0b0b)


def Watch(watchTime):
    Watch_BG((245, 165))
    Watch_Needle((245, 165), 70, watchTime)


def getRankSuffix(rank):
    if (rank % 10 == 1 and rank != 11):
        return "st"
    elif (rank % 10 == 2 and rank != 12):
        return "nd"
    elif (rank % 10 == 3 and rank != 13):
        return "rd"
    else:
        return "th"


def getMonth(m):
    month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    return month[m - 1]


def printDate(todayDate):
    M5TextBox(30, 30, str(todayDate[1]) + getRankSuffix(int(todayDate[1])) + " " +
              getMonth(int(todayDate[0])), lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)


todayDate = [ntp.month(), ntp.day()]
printDate(todayDate)
watchTime = [ntp.minute(), ntp.second()]
Watch(watchTime)
while True:
    if watchTime != [ntp.hour(), ntp.minute()]:
        setScreenColor(0x000000)
        watchTime = [ntp.hour(), ntp.minute()]
        Watch(watchTime)
        todayDate = [ntp.month(), ntp.day()]
        printDate(todayDate)

    wait_ms(2)
