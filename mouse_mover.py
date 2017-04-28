import ctypes
import time
import random

mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

while True:
	r = random.random()
	s_time = 30 + r * 60
	print("Zzz... {}".format(s_time))
	time.sleep(s_time)
	mouse_event(MOUSEEVENTF_MOVE, 0, 0, 0, 0)
	
