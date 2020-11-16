import os, sys
import cv2
import numpy as np

imagedir = 'E:\\haskell_texture\\texture\\banshu'
outdir = 'E:\\haskell_texture\\banshu\\'
textureManagerCmd = 'S:\\Egret\\TextureMerger\\TextureMerger.exe'


def packerFoler(dir, outputDir):
    for s in os.listdir(dir):
        # 如果需要忽略某些文件夹，使用以下代码
        if s == "icon":
            packerFoler(os.path.join(dir, s), outputDir + "icon\\")
            continue
        newDir = os.path.join(dir, s)
        print(newDir)
        cmdTmp = textureManagerCmd + \
                 " -p " + \
                 newDir + \
                 " -o " + outputDir + s + ".json"

        os.system(cmdTmp)
        img = cv2.imread(outputDir + s+".png")
        sp = img.shape
        if sp[0] > 2048 or sp[1] > 2048:
            print("======================> over 2048:", outputDir + s+".png")




if __name__ == '__main__':
    print("packer start")
    packerFoler(imagedir, outdir)
    print("packer end")
