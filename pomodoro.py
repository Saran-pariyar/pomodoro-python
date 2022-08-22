from time import sleep
from unittest import result
from pyautogui import confirm, alert


def pomodoro():
    i = 0
    total_number_of_time = 0
    rest_taken = 0
    added_time = 0
    result = (
        "Added time is ",
        added_time,
        "min and rest taken is ",
        rest_taken,
        "min",
    )
    total = "Total number of minutes = ", total_number_of_time + added_time

    while True:
        a = confirm(text="Start pomodoro", title="", buttons=["OK", "No"])
        if a == "No":
            alert(text=result, title=total, button="OK")

        print(a)
        if a == "OK":
            print("Started pomodoro")
            # sleeps for 30 minutes
            sleep(1800)
            # when 30 minutes is over, we will add 30 as value on total_number_of_time
            total_number_of_time = total_number_of_time + 30
            # takes input from the user
            getData = confirm(
                text="Your 30 minute is over",
                title="",
                buttons=["Take 10 min rest", "add 10 min more", "End"],
            )

            if getData == "add 10 min more":
                sleep(600)
                alert(text="Time over, you worked extra 10 min", title="", button="OK")
                added_time = added_time + 10

            elif getData == "Take 10 min rest":
                sleep(600)
                alert(text="Your 10 min rest is over", title="", button="OK")
                rest_taken = rest_taken + 10

            elif getData == "End":
                print(added_time, rest_taken)

                alert(text=result, title=total, button="OK")
                break
            i = i + 1
        else:
            alert(text="Understandable, have a nice day!", title="", button="OK")
            break


pomodoro()
