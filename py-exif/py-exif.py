#ecoding:utf-8
import pyexiv2 as ev
import time
import os
import ConfigParser
class exif():
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.ini', "rb"))
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
            exiv_image = ev.ImageMetadata(path)
            exiv_image.read()
            exiv_image["Exif.Image.Artist"] = self.Artist
            exiv_image["Exif.Photo.DateTimeOriginal"] = mytime
            exiv_image["Exif.Image.Software"] = self.Software
            exiv_image.write()
            print u'图片:',path,u'操作成功'
        except:
            print u'图片:',path,u'操作失败'
    def star(self):
        path =  raw_input(unicode('请输入图片路径：','utf-8').encode('gbk'))
        #newpath = unicode(path, 'utf8')
        self.imgSave(path+'/')
        self.star()
print u'#------------------------------------'
print u'# 程序:批量修改图片exif信息'
print u'# 路径格式为:G:\图片'
print u'#------------------------------------'
Exif = exif()
Exif.star()

