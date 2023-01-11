import pyautogui as gui
import pyperclip as clip
import time

gui.PAUSE = 1
gui.FAILSAFE = True # caso tenha feito algo errado, coloca o mouse na coordenada 0,0 que ele para

clip.copy("word")

gui.press("win")
# gui.write("word")
gui.hotkey('ctrl','v')
time.sleep(3)
#gui.press("enter")

# posso usar sleep para saber a posição
# print(gui.position())
gui.click(x=498,y=454, clicks=2)

