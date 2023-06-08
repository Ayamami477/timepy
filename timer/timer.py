import tkinter
from datetime import datetime
import threading
import time

def timeEvent():
    th = threading.Thread(target=print_datetime)
    th.start()

def print_datetime():
    while True:
        global now
        now_h=datetime.now().hour
        now_s=datetime.now().second
        now_m=datetime.now().minute
        if len(str(now_m)) == 1:
            m = '0' + str(now_m)
        else:
            m = str(now_m)
        if len(str(now_s)) == 1:
            s = '0' + str(now_s)
        else:
            s = str(now_s)
        now_time = '現在時刻:' + str(now_h)+':'+m+':'+s
        print(now_time)
        datetime_label["text"] = now_time
        time.sleep(1)

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("タイマー")
    root.geometry("150x100")
    datetime_label = tkinter.Label(root,text="")
    datetime_label.grid(row=1, column=0)
    timeEvent()
    root.mainloop()