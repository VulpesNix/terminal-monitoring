from os import system as s
import curses
from time import time as now,sleep

def main(stdscr):
	curses.curs_set(0)

	while 1:	
		y,x = stdscr.getmaxyx()
		s("nvidia-smi --query-gpu=memory.total,memory.used,temperature.gpu --format=csv > data.txt")
		file = open("data.txt","r+")
		raw = file.readlines()
		raw = raw[1]
		raw = raw.split(", ")
		total = raw[0]
		total = total.split()
		total = int(total[0])
		used = raw[1]
		used = used.split()
		used = int(used[0])
		temp = (raw[2].split())[0]
		tempx = temp + "°C"
		print(tempx)
		t_color = 4
		if(int(raw[2]) <= 44):
			t_color = 4
		elif(int(raw[2]) <= 58):
			t_color = 3
		elif(int(raw[2]) <= 72):
			t_color = 2
		else:
			t_color = 1  
		p = round((used*100)/total,2)
		b = int(p // 5)
		bar = "["
		block = "█"
		for i in range(b+1):
			bar += block
		for i in range(21-b):
			bar += " "
		bar += "]"
		var = str(used) + "MB" + "/" + str(total) + "MB"
		curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
		curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
		curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
		curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
		stdscr.addstr(y//2+2,x//2-(len(var)//2),var,curses.color_pair(4))
		stdscr.addstr(y//2-1,x//2-1,tempx,curses.color_pair(t_color))
		if p < 25:
			stdscr.addstr(y//2+1,x//2-11,bar,curses.color_pair(3))
			stdscr.addstr(y//2,x//2-(len(str(p))//2),"%"+str(p),curses.color_pair(3))
		elif p > 25 and p < 70:
			stdscr.addstr(y//2,x//2-(len(str(p))//2),"%"+str(p),curses.color_pair(2))
			stdscr.addstr(y//2+1,x//2-11,bar,curses.color_pair(2))
		else:
			stdscr.addstr(y//2,x//2-(len(str(p))//2),"%"+str(p),curses.color_pair(1))
			stdscr.addstr(y//2+1,x//2-11,bar,curses.color_pair(1))
		past = now()
		while(now() - past < 0.5):
			stdscr.refresh()
		
		stdscr.refresh()
		stdscr.clear()

curses.wrapper(main)
