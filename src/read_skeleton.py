import json
import os
import re

image_path = 'E:\\SeafileSync\\Seafile\\Haskell\\角色动画'

def loadSke(fileName):
    f = open(fileName,'r', encoding='UTF-8')
    ske = json.load(f)
    armature = ske['armature']
    for arm in armature:
        animations = arm['animation']
        for ami in animations:
            aname = ami['name']
            if 'playTimes' in ami:
                playTime = ami['playTimes']
                if (playTime == 0):
                    print(fileName,',', aname)


def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
                #continue

            newDir = os.path.join(dir, s)

            get_filelist(newDir, Filelist)
    return Filelist

if __name__ == '__main__' :
    list = get_filelist(image_path, [])
    for fileName in list:
        searchFile = re.search(r'.*ske\.json', fileName, re.I)
        if searchFile :
            loadSke(fileName)
