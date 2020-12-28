
import time   # REMEMBER TO SHOW THEM HOW TO DOWNLOAD
import pyautogui


def SendPrankMessage():
    time.sleep(3)
    f = open("happy.txt")
    for each_line in f:
        pyautogui.typewrite(each_line)
        # pyautogui.press('enter')


SendPrankMessage()


# def SendPrankMessage():
#     time.sleep(3)
#
#     with open('happy.txt') as f:
#         entire_song = f.readlines()
#     for each_line in entire_song:
#         pyautogui.typewrite(each_line.strip())
#         pyautogui.press('enter')
#
#
# SendPrankMessage()