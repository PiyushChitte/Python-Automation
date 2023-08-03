import schedule
import time
import datetime

def Task_Minute():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular eexecuted after Minute")

def Task_Hour():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular executed after Hour")

def Task_Day():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular executed after Day")

def Task_Afternoon():
    print("Current timme is")
    print(datetime.datetime.now())
    print("Schedular executed at 12")


def main():
    print("-------- Task Schedular script by Piyush Chitte ----------")

    print("Python Task Scheddular")

    print(datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minute)
    schedule.every().hour.do(Task_Hour)
    schedule.every().thursday.do(Task_Day)
    schedule.every().day.at("00:00").do(Task_Afternoon)
    schedule.every().wednesday.at("20:38").do(Task_Day)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()