
import pyautogui as pg
import time
import pyperclip
t=5
time.sleep(t)
def print_code():
    code=pyperclip.paste()
    lines=code.splitlines()
    count=len(lines)
    for line in lines:
        if not line.startswith('#'):
            pg.write('#')
        if '#' in line and not line.startswith('#'):
            line=line[:line.index('#')]
        pg.write(line.rstrip())
        pg.press('enter')
    for _ in range(count):
        pg.press('up')
    for line in lines:
        if not line.startswith('#'):
            pg.press('delete',presses=2)
            pg.press('end')
            pg.press('enter')
    print('hii')
print_code()

