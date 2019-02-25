import datetime
import time
import os
import subprocess
time.sleep(25)
now = datetime.datetime.now()
timer = open('timer','r').read()
timeVar = int(timer)

def chkDay():
    dateStat = int(open('nowDate','r').read())
    if os.stat("nowDate").st_size != 0:
        print('date found')
        if now.day == dateStat:
            print("today and nowDate are the same!")
            if int(open('timer','r').read()) == 0:
                print("You're done for the day.")
                os.system("taskkill /IM csgo.exe /F")
                os.system("taskkill /IM steam.exe /F")
                exit()
            else:
                ProcessRead()
        elif now.day != dateStat:
            open("timer", "w").write(str(60))#<= change the number to 120 or make a var *******
            open("nowDate", "w").write(str(now.day))
            timeVar = timer
            ProcessRead()
    else:
        print('no date witnessed')
        open("nowDate", "w").write(str(now.day))
        ProcessRead()

def ProcessRead(): #if csgo is off: close the program
    global timer
    timeVar = int(timer)
    open("procStat", "w")
    procWrite = subprocess.call('TASKLIST | FINDSTR /I "csgo.exe" > procStat', shell=True)#<= Change to "csgo.exe" or make a var or make a variable *******
    procWriteOpen = open("procStat","r")
    procStat = procWriteOpen.read(8)#<= change to .read(8) for csgo.exe or make a var: charlen = process.len() *******
    if procStat == "csgo.exe":#<= change to csgo.exe ******
        print('csgo.exe found')
        if int(timer) == 0:
            subprocess.Popen("taskkill /IM csgo.exe /F", shell=True)
            exit()
        else:
            while (int(timer) >= 0):
                print(timer)
                timer = int(timer) - 1
                time.sleep(60)
                open("timer", "w").write(str(timer))
                ProcessRead()
    else:
        print('process csgo.exe not found')
        exit()

chkDay()
