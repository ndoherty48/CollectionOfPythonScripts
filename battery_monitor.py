import psutil
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
battery = psutil.sensors_battery()
plugged_boolean = battery.power_plugged
percent = str(battery.percent)
minutes_to_sleep = 30


def notify_user():
    if int(percent) == 100 and plugged_boolean:
        toaster.show_toast("Turn off Charger", "Device is now at 100% battery, please turn off charger!")
    elif int(percent) <= 25 and not plugged_boolean:
        toaster.show_toast("Turn on Charger", "Device is now at {}% battery, you may want to plug a charger in!"
                           .format(percent))


while True:
    notify_user()
    time.sleep(minutes_to_sleep * 60)
