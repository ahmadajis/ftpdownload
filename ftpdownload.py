#!/usr/bin/python3
import ftplib
import os
import time #option
from dateutil import parser #option
from datetime import datetime #option

ftp = ftplib.FTP('example.com', 'demo','password')
ftp.retrlines('LIST')

ftp.cwd("pub")
ftp.cwd("example")
ftp.retrlines('LIST')

start = datetime.now()
files = ftp.nlst()
for file in files:
	print("Downloading..." + file)
	ftp.retrbinary("RETR " + file ,open("/yourdirectori/file" + file, 'wb').write)

ftp.close()

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')
