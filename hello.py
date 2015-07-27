# -*- coding: cp949 -*-
import sys
import os
import glob
import shutil

#print glob.glob('*') # 현재 폴더 내부의 모든 파일 정보를 가지고 온다.

def CopyFile(s, d):
    try:
        os.makedirs(os.path.dirname(d))
    except:
        pass

    shutil.copy(s, d)
    print 'Copy %s' % (os.path.basename(s))
    
def CopyTree(s, d):
        if not os.path.exists(d):
            print d
            os.makedirs(d)

        for name in os.listdir(s):
                spath = s + '\\' + name
                dpath = d + '\\' + name

                if os.path.isdir(spath):
                    CopyTree(spath, dpath)
                else:
                    CopyFile(spath, dpath)
#
#
#
print os.listdir('.')

if os.path.exists('.\hello'):
    print 'existed!'
else:
    os.makedirs('hello')

print os.path.isdir('.\hello')
print os.path.exists('.\hello')
