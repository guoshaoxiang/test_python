import json
import os
import re
image_path = 'S:\\workspace\\haskell\\haskell_client\\resource\\assets'

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
        searchFile = re.search(r'.*\.png', fileName, re.I)
        if searchFile :
            output = fileName.replace(".png", ".pvr.ktx")
            cmd = "texture-compressor -i "+fileName+" -t pvrtc -c PVRTC1_4 -q pvrtchigh -o "+output+" -vb"
            os.system(cmd)
    print("end")