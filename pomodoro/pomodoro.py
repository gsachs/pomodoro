"""
This is a simple pomodoro clock which runs on terminal

Enhancements:
	1. Start logging work and break
	2. May be with timestamps?
	3. Could be json dumps to begin with, and can extend the logic to a db
	4. Simple dashboard to track the progress
	5. Browser interface may be?

"""

import os,time,sys

pomo_duration = 25
break_duration = 5

def vinput(msg):
	os.system('say -v Victoria ' + msg)
	val = input(msg)
	return val


def custom_sleep(time_duration):
	print('==========================================================================================')
	print('Duration for {0} minutes'.format(time_duration))
	for i in range(int(time_duration),0,-1):
		print('Time left: {0} minutes'.format(i),end="\r",flush = True)
		sys.stdout.flush()
		time.sleep(60)

	print("\n")


pomo_duration = input('Enter work time in minutes: ')
break_duration = input('Enter break time in minutes: ')

while(True):
	print("Starting work for {0} minutes".format(pomo_duration))
	custom_sleep(pomo_duration)
	break_check = vinput('Work done, do you want a break?: ')
	if break_check == 'y':
		print('Taking a break!')
		custom_sleep(break_duration)
	elif break_check == 'c':
		custom_break = vinput('Enter custom break duration: ')
		print('Taking a break!')
		custom_sleep(custom_break)
	elif break_check == 'n':
		# Do nothing, continue
		print('continue with work!')
	else:
		break



