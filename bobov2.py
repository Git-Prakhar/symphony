import speech_recognition as sr
import pyautogui as pg
import time
import tkinter as tk
from tkinter import simpledialog

def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        while True:
            try:
                print('Listening...')
                audio = r.listen(source, phrase_time_limit=5)
                recognized_text = r.recognize_google(audio).lower()
                recognizedArr = recognized_text.split()
                print(recognizedArr)
                speech_command(recognizedArr)


            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error: {0}".format(e))

def speech_command(commandArr : list):
    print(commandArr)
    if commandArr == []:
        return
    
    if 'cancel' in commandArr:
        return
    
    if 'open' in commandArr:
        openArr = commandArr[commandArr.index('open') + 1:]
        open_command(openArr)

def open_command(openArr : list):
    if openArr == []:
        return
    
    cmdList = [
        'browser',
        'brave',
        'notepad',
        'calculator',
        'folder',
        'figma',
        'code',
        'youtube'
    ]

    if openArr[0] not in cmdList:
        return
    
    if openArr[0] == 'browser' or openArr[0] == 'brave':
        pg.hotkey('win', 'r')
        time.sleep(0.2)
        pg.write('brave')
        pg.press('enter')
    elif openArr[0] == 'notepad':
        pg.hotkey('win', 'r')
        time.sleep(0.2)
        pg.write('notepad')
        pg.press('enter')   
    elif openArr[0] == 'calculator':
        pg.hotkey('win', 'r')
        time.sleep(0.2)
        pg.write('calc')
        pg.press('enter')
    elif openArr[0] == 'folder':
        pg.hotkey('win', 'r')
        time.sleep(0.2)
        pg.write('explorer')
        pg.press('enter')
    elif openArr[0] == 'figma':
        pg.hotkey('win', 'r')
        time.sleep(0.2)
        pg.write('C:/Users/Nitro-5/AppData/Local/Figma/app-124.4.7/Figma.exe')
        pg.press('enter')
    elif openArr[0] == 'code':
        pg.hotkey('win', 'r')
        time.sleep(0.2)
        pg.write('code')
        pg.press('enter')
    elif openArr[0] == 'youtube':
        ytcmdList = [
            'search',
            'write',
            'right',
            'history',
            'playlist'
        ]
        if len(openArr) == 1:
            pg.hotkey('win', 'r')
            time.sleep(0.2)
            pg.write('www.youtube.com')
            pg.press('enter')
        if openArr[1] not in ytcmdList:
            pg.hotkey('win', 'r')
            time.sleep(0.2)
            pg.write('www.youtube.com')
            pg.press('enter')
        else:
            if openArr[1] == 'search':
                pg.hotkey('win', 'r')
                time.sleep(0.2)
                pg.write('brave "https://www.youtube.com/results?search_query=' + '+'.join(openArr[2:]) + '"')
                pg.press('enter')
            elif openArr[1] == 'history':
                pg.hotkey('win', 'r')
                time.sleep(0.2)
                pg.write('brave "https://www.youtube.com/feed/history"')
                pg.press('enter')
            elif openArr[1] == 'write' or openArr[1] == 'right':
                root = tk.Tk()
                root.withdraw()
                write = simpledialog.askstring("YouTube", "Enter the video title")
                if write == None:
                    return
                pg.hotkey('win', 'r')
                time.sleep(0.2)
                pg.write('brave "https://www.youtube.com/results?search_query=' + '+'.join(write.split()) + '"')
                pg.press('enter')
            elif openArr[1] == 'playlist':
                pg.hotkey('win', 'r')
                time.sleep(0.2)
                pg.write('www.youtube.com/feed/playlists')
                pg.press('enter')
    return

listen_for_wake_word()