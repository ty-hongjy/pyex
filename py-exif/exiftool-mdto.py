# exiftool-mdt： exiftool modify dateTimeOriginal, 
# it through command line exiftool( https://sno.phy.queensu.ca/~phil/exiftool/)
# python prg:batch modify picture exif dateTimeOriginal by difference 
# between old datetime and new datetime
# path format is: G:\picture
# if run in windows ,please run in minGW64 or in git bash shell,because 'grep' is 
# not for windows cmd or powershell.

import exiftool
import subprocess
import datetime
import time
import os
import configparser

config = configparser.ConfigParser()
# config.read('config.ini')
# old_str = config.get("global", "old")
# new_str = config.get("global", "new")
#self.Software = config.get("global", "Software")

old=datetime.datetime(2014, 8, 30, 23, 2, 0,0)
new=datetime.datetime(2019, 5, 2, 7,00, 0,0)
delta=new-old
print("delta:",delta)
#subprocess.run(["exiftool.exe","-h"])
#subprocess.run(['exiftool.exe', "-dateTimeOriginal=2005:10:23 20:06:34-05:00" ,'DSC02446.JPG'])
#subprocess.run(['exiftool.exe' ,'-a  -u  -g1','DSC02452.JPG'])
#str = subprocess.run('exiftool.exe -a -u -g1 DSC02452.JPG|grep "Date/Time O"',shell=True)
#str = subprocess.call('exiftool.exe -a -u -g1 DSC02452.JPG|grep "Date/Time O"',shell=True)

#str = subprocess.getstatusoutput('exiftool.exe -a -u -g1 DSC02452.JPG|grep "Date/Time O"')
#str = subprocess.getstatusoutput('exiftool.exe -a -u -g1 "E:\\2019502a\DSC02789.JPG"|grep "Date/Time O"')
#print(str)

print( '#------------------------------------')
print( '# python prg:batch modify picture exif dateTimeOriginal by difference between old datetime and new datetime')
print( '# path format is: G:\picture')
print( '#------------------------------------')
dirname =  input('please input picture path：')

start=datetime.datetime.now()
print("start:",start)
i=0
for filename in os.listdir(dirname):
	i+=1
	print("No:",i)
	path = dirname + "\\" + filename
	str1='exiftool.exe -a -u -g1 "'+path+'"|grep "Date/Time O"'
	print(str1)
	str = subprocess.getstatusoutput(str1)
	print(str)
	str_split=str[1].split(':',1)
#	print(str_split)
	print(str_split[1].strip())
	old1=time.strptime(str_split[1].strip(),"%Y:%m:%d %H:%M:%S")
	print(old1)
	old2=datetime.datetime(*old1[0:6])
	print(old2)
	new2=old2+delta
	new2s=new2.strftime("%Y:%m:%d  %H:%M:%S")
	str1='exiftool.exe "-dateTimeOriginal='+new2s+'" '+path
	str = subprocess.getstatusoutput(str1)
	print( 'picture:',str1,'operate successfully')

	#print( '图片:',path,'操作成功')

end=datetime.datetime.now()
print("end:",end)
print("total:",end-start)