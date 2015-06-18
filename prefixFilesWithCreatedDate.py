import sys
import os
import time
import datetime

for filename in os.listdir(sys.argv[2]):
	if not filename.startswith(sys.argv[1]):
		fileOrig = sys.argv[2] + "\\" + filename
		if not os.path.isdir(fileOrig):
                        newFileName = sys.argv[2] + "\\"+ sys.argv[1] + datetime.datetime.strptime(time.ctime(os.path.getmtime(fileOrig)), "%a %b %d %H:%M:%S %Y").strftime("%Y%m%d") + "_" + filename
                        os.rename(fileOrig, newFileName)
#SUCK IT
