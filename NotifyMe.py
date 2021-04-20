from plyer import notification
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\SUNNY KUMAR\\Downloads\\Graphicloads-Flat-Finance-Target-market.ico",
        timeout = 10,
    )



if __name__=='__main__':
    while True:
        notifyMe("Hey Sunny, just take a break !","and Focus on your Target.")
        time.sleep(5)


