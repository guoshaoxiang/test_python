import os
from xml.dom.minidom import parse
import xml.dom.minidom
import json
import re
#最后一步

exml_path = 'S:\\workspace\haskell\\haskell_client\\resource\eui_skins\\battle\\scene\\nauka'
exml_path_explore = 'S:\\workspace\haskell\\haskell_client\\resource\eui_skins\\battle\\scene\\nauka\\explore'

def readSource(fileName, sourceSet):
    domtree = xml.dom.minidom.parse(fileName)
    collection = domtree.documentElement
    images = collection.getElementsByTagName("e:Image")
    for image in images:
        if image.hasAttribute("source"):
            sourceSet.append(image.getAttribute("source"))


def get_exmlfilelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
                #continue

            newDir = os.path.join(dir, s)

            get_exmlfilelist(newDir, Filelist)
    return Filelist




if __name__ == '__main__' :
    list = get_exmlfilelist(exml_path, [])
    explore_list = get_exmlfilelist(exml_path_explore, [])
    sourceSet = []
    for fileName in explore_list:
        readSource(fileName, sourceSet)
    sourceSet = set(sourceSet)

    for fileName in list:
        import re

        f = open(fileName, 'r')
        alllines = f.readlines()
        f.close()
        f = open(fileName, 'w+')
        for eachline in alllines:
            a = eachline
            for source in sourceSet:
                sourceSp = source.split('.', -1)
                print(source)
                a = a.replace(source, 'nauka_explore_json.'+sourceSp[1])
            f.writelines(a)

        f.close()



