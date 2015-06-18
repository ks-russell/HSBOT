
thefile = open('/Users/krussell/Library/Preferences/Blizzard/Hearthstone/Logs/hearthstone_2015_06_17_22_48_12.log')

while True:
	ret1 = thefile.read()
	str = thefile.seek(0)
	ret2 = thefile.read()
	if len(ret1) > 1 & str == 0:
		print(ret1)
