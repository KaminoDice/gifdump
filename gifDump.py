#!/usr/bin/env python
#coding:utf-8
import sys
import os

desc="""
==========================================================
        DumpGif v 0.1 beta by xkong
        CopyLeft (c) 2012
        xiaokong1937@gmail.com
==========================================================
"""
usage="""
    Usage: DumpGif.exe your_emotion_file.eif
"""
class GetImg():
    def __init__(self,f):
        self.num=0
        self.file=f
    def dump_gif(self):
        with open(self.file, "rb") as f:
            map_ = f.read()
            l=len(map_)
            index=map_.find('GIF',0,l)
            while index > -1:
                if map_[index:index+3]=="GIF" \
                    and map_[index+3]=="8" \
                    and ord(map_[index+4]) in [0x37,0x39]:
                    end=map_.find(";",index,l)
                    while ord(map_[end-1])!=0x00 \
                        or ord(map_[end+1])!=0x00 \
                        or ord(map_[end+2])!=0x00:
                        end=map_.find(";",end+1,l)
                    data=map_[index:end+1]
                    self.save_img(data,"gif")
                index=map_.find('GIF',index+1,l)
        print "All the GIF files have been dumpped."
    def dump_png(self):
        with open(self.file, "rb") as f:
            map_ = f.read()
            l=len(map_)
            self.num=0
            index=map_.find("PNG",0,l)
            print index
            while index > -1:
                if ord(map_[index-1])==0x89 \
                    and ord(map_[index+3])==0x0d \
                    and ord(map_[index+4])==0x0a \
                    and ord(map_[index+5])==0x1a :
                        end=map_.find("IEND",index,l)
                        while ord(map_[end+4])!=0xAE \
                            and ord(map_[end+5])!=0x42\
                            and ord(map_[end+6])!=0x60 \
                            and ord(map_[end+7])!=0x82:
                                end=map_.find("IEND",end+1,l)
                        data=map_[index-1:end+7]
                        self.save_img(data,"png")
                index=map_.find("PNG",index+1,l)
        print "All the PNG files have been dumpped. "
    def save_img(self,data,name):
        with open("%i.%s" % (self.num,name),'wb') as f:
            f.write(data)
            print "%s %s dump ok" % (self.num,name)
            self.num+=1
if __name__=="__main__":
    print desc
    if len(sys.argv)<2:
        print usage
        sys.exit()
    else:
        f=sys.argv[1]
        if not os.path.isfile(f):
            sys.exit("Not a valid Emotion file.")
    test=GetImg(f)
    test.dump_gif()
