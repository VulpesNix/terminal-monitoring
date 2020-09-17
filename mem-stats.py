from os import system as s
import curses as c

# command is the one who actually makes the job btw
command = "cat /proc/meminfo | grep Mem > .meminf.log"

def main(stdscr):
	c.curs_set(0)
	c.init_pair(1,c.COLOR_RED,c.COLOR_BLACK)
	c.init_pair(2,c.COLOR_YELLOW,c.COLOR_BLACK)
	c.init_pair(3,c.COLOR_GREEN,c.COLOR_BLACK)
	c.init_pair(4,c.COLOR_WHITE,c.COLOR_BLACK)
	while(1):
		y,x = stdscr.getmaxyx()
		s(command)
		file = open(".meminf.log","r+")
		file = file.readlines()
#getting the data from meminf.log
		totalmem = int(file[0].split()[1])
		usedmem = totalmem - int(file[2].split()[1])
#prc is the percentage of used memory
		prc = round((usedmem*100)/totalmem,1)
		prc = "%" + str(prc)
		barlen = (usedmem*20)//totalmem
	#converting kilobyte to gigabyte
		usedmem = round(usedmem /pow(1024,2),1)
		totalmem = round(totalmem / pow(1024,2),1)
		using = str(usedmem) + "/" + str(totalmem) + "GB"
	#ulen is the half of the length of using why? bc if i wrote it in addstr it will look crazy long
		ulen = len(using) // 2
#I used square because it gives bar a vibe
		bar = "["
#creating the bar according to memory usage
		for i in range(barlen):
			bar += "█"
		for i in range(20-barlen):
			bar += " "
		bar += "]"
#change the color pair according to memory usage
		if barlen < 5:
			color = c.color_pair(4)
		if barlen > 5:
			color = c.color_pair(3)
		if barlen > 10:
			color = c.color_pair(2)
		if barlen > 15:
			color = c.color_pair(1)
#the part that we writing our bar and percentage
		stdscr.addstr(y//2,x//2-11,bar,color)
		stdscr.addstr(y//2-1,x//2-len(prc)//2,prc,color)
		stdscr.addstr(y//2+1,x//2-ulen,using,c.color_pair(4))
		stdscr.refresh()
		stdscr.clear()
c.wrapper(main)
