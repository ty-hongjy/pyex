#ecoding:utf-8
#import pyexiv2 as ev
import time
import os
import configparser
import datetime

old=datetime.datetime(2014, 8, 30, 22, 5, 0,0)
new=datetime.datetime(2019, 5, 2, 6,40, 0,0)
delta=new-old
print(delta)

class exif():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.Artist = config.get("global", "Artist")
        self.DateTimeOriginal = config.get("global", "DateTimeOriginal")
        self.Software = config.get("global", "Software")
    
    def imgSave(self,dirname):
        for filename in os.listdir(dirname):
            path = dirname + filename
            if os.path.isdir(path):
                path += '/'
                self.imgSave(path)
            else:
                self.imgExif(path)
    
    def imgExif(self,path):
        try:
            if self.DateTimeOriginal == "now":
                mytime = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(time.time()))
            else:
                mytime = self.DateTimeOriginal

#            exiv_image = ev.ImageMetadata(path)
#            exiv_image.read()
#            exiv_image["Exif.Image.Artist"] = self.Artist
#            exiv_image["Exif.Photo.DateTimeOriginal"] = mytime
#            exiv_image["Exif.Image.Software"] = self.Software
#            exiv_image.write()
            print( '图片:',path,'操作成功')
        except:
            print( '图片:',path,'操作失败')
    
    def star(self):
        path =  input('请输入图片路径：')
        #newpath = unicode(path, 'utf8')
        self.imgSave(path+'/')
        self.star()
print( '#------------------------------------')
print( '# 程序:批量修改图片exif信息')
print( '# 路径格式为:G:\图片')
print( '#------------------------------------')
Exif = exif()
Exif.star()

