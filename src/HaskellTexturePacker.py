import os, sys

folderName = 'battle_original'
imagedir = 'E:\\SeafileSync\\Seafile\\Haskell\\UI\\atlas\\1024\\'
outplistdir = 'E:\\haskell_texture\\2048\\'
texturePackerCmd = 'E:\\TexturePacker\\bin\\TexturePacker.exe'
ktxCmd = 'npx egret-texture-generator --t E:\haskell_texture\TexturePacker -q high --pf canvasalpha --pbpp 4'

def packerFoler(dir, outputDir):
    for s in os.listdir(dir):
        # 如果需要忽略某些文件夹，使用以下代码
        if s == "icon":
            packerFoler(os.path.join(dir, s), outputDir+"icon\\")
            continue
        if s != "1024" and s != "window_ui":
            newDir = os.path.join(dir, s)
            print(newDir)
            cmdTmp = texturePackerCmd + \
                     " --format egret-spritesheet" + \
                     " --data " + outputDir + s + ".json" + \
                     " --sheet " + outputDir + s + ".png" + \
                     " --max-size 2048 --opt RGBA8888 --size-constraints POT" + \
                     " --force-squared" +\
                     " --force-word-aligned" +\
                     " --reduce-border-artifacts" +\
                     " --dpi 72" +\
                     " " + \
                     newDir

            os.system(cmdTmp)


if __name__ == '__main__':
    print("packer start")
    packerFoler(imagedir, outplistdir)
    # os.system(ktxCmd)
    print("packer end")
