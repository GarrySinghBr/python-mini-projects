from plyer import notification
import psutil
import time

battery = psutil.sensors_battery()

# Defining the title and message
title = "Battery Low!"
message = "Please Connect your Charger"

while True:
    if battery.percent < 30:
        notification.notify(title = title ,message = message)
        break
    else:
        time.sleep(300)

