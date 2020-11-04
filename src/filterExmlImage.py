import os
from xml.dom.minidom import parse
import xml.dom.minidom
import json
import re
#第一步

exml_path = 'S:\\workspace\haskell\\haskell_client\\resource\eui_skins\\battle\\scene\\nauka\\explore'
texture_json_path = 'E:\\haskell_map\\scene\\10_nauka\\01'
png_folder = texture_json_path+'\\PNG'
explore_folder = "nauka_explore"

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

def get_jsonfilelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        searchFile = re.search(r'.*\.json', dir, re.I)
        if searchFile:
            Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):

            newDir = os.path.join(dir, s)

            get_jsonfilelist(newDir, Filelist)
    return Filelist

def copyFile(sourceFileName, sourceDir,  targetDir):
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    sourceFile = os.path.join(sourceDir, sourceFileName)
    targetFile = os.path.join(targetDir, sourceFileName)
    if os.path.exists(sourceFile):
        open(targetFile, "wb").write(open(sourceFile, "rb").read())
        os.remove(sourceFile)



def parseTextureJsonAndCopyFile(fileName):
    f = open(fileName,'r', encoding='UTF-8')
    ske = json.load(f)
    frames = ske['frames']
    (filepath, tempfilename) = os.path.split(fileName);
    (shotname, extension) = os.path.splitext(tempfilename);
    targetDir = os.path.join(texture_json_path, shotname)
    for frame in frames:
        copyFile(frame+".png", png_folder, targetDir)


if __name__ == '__main__' :
    list = get_exmlfilelist(exml_path, [])
    sourceSet = []
    for fileName in list:
        readSource(fileName, sourceSet)
    sourceSet = set(sourceSet)
    targetDir = os.path.join(texture_json_path, explore_folder)
    for source in sourceSet:
        source = source.split('.', -1);
        copyFile(source[1] + ".png", png_folder, targetDir)

    jsonList = get_jsonfilelist(texture_json_path, [])
    for jsonFile in jsonList:
        parseTextureJsonAndCopyFile(jsonFile)