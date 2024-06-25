import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test!")
    stdscr.addstr("\nPress any key to begin: ")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr,tgt,curr,wpm=0):
    stdscr.addstr(tgt)
    stdscr.addstr(1,0,f"WPM: {wpm}")

    for i,char in enumerate(curr):
        crt_char=tgt[i]
        color=curses.color_pair(1)

        if char!=crt_char:
            color=curses.color_pair(2)
        
        stdscr.addstr(0,i,char,color)

def load_text():
    with open("11_sample_text.txt",'r')as f:
        lines=f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    tgt_txt=load_text()
    current=[]
    wpm=0
    start=time.time()
    stdscr.nodelay(True)

    while True:
        time_lapse=max(time.time()-start,1)
        wpm=round((len(current)/(time_lapse/60))/5)
        stdscr.clear()
        display_text(stdscr,tgt_txt,current,wpm)
        stdscr.refresh()

        if "".join(current)==tgt_txt:
            stdscr.nodelay(False)
            break
        try:
            key=stdscr.getkey()
        except:
            continue
         
        if ord(key)==27:
            break

        if key in("KEY_BACKSPACE",'\b',"\x7f"):
            if(len(current)>0):
                current.pop()
        elif (len(current)<len(tgt_txt)):
            current.append(key)

        

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You completed the text! Press any key to continue !")
        key = stdscr.getkey()
        if ord(key)==27:
            break

wrapper(main)