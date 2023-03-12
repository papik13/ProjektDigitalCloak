import datetime
import time

### CODE  ###

while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)