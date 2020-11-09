import os, sys

folderName = 'battle_original'
imagedir = 'E:\\haskell_map\\scene\\01_wasteland\\01\\'
texturePackerCmd = 'E:\\TexturePacker\\bin\\TexturePacker.exe'


def packerFoler(dir, outputDir):
    for s in os.listdir(dir):
        newDir = os.path.join(dir, s)
        print(newDir)
        cmdTmp = texturePackerCmd + \
                 " --format egret-spritesheet" + \
                 " --data " + outputDir + s + ".json" + \
                 " --sheet " + outputDir + s + ".png" + \
                 " --max-size 1024 --opt RGBA8888 --size-constraints POT" + \
                 " --force-squared" + \
                 " --scale 0.5" + \
                 " " + \
                 newDir

        os.system(cmdTmp)


if __name__ == '__main__':
    print("packer start")
    packerFoler(imagedir, imagedir)
    print("packer end")
