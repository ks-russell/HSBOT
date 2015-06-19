import os
import datetime
import sys

log_location = '/Users/krussell/Library/Preferences/Blizzard/Hearthstone/Logs/'
newest_file = None
newest_file_time = 0

for file in os.listdir(log_location):
	t = os.path.getctime(log_location + file)
	time = datetime.datetime.fromtimestamp(t)
	timeStr = time.strftime('%Y%m%d%X')
	condensed_timeStr = timeStr[0:9] + timeStr[11:13] + timeStr[14:]
	if int(condensed_timeStr) > newest_file_time:
		newest_file_time = int(condensed_timeStr)
		newest_file = file

thefile = open(log_location + newest_file)

while True:
	ret1 = thefile.read()
	str = thefile.seek(0)
	if str == None:
		print('Hearthstone game not found.')
		sys.exit()
	ret2 = thefile.read()
	if len(ret1) > 1 & str == 0:
		print(ret1)
