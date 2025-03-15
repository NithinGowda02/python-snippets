import time
import datetime
import winsound

def set_alaram(alarm_time):
    current_Time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_Time)
    if current_Time == alarm_time:
        print("Wake Up..! Alarm ringing..")
        for _ in range(5):
            winsound.Beep(1000,500)
            break
    time.sleep(1)   
alarm_time = input("Enter the alarm Time (HH:MM:SS) >> ")   
set_alaram(alarm_time)  