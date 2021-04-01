import os
filedir = "E:\\idris\\effect"

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

if __name__ == '__main__':
    print("packer start")
    list = get_filelist(filedir, [])
    for fileName in list:
        os.rename(fileName, fileName+"1")
    print("packer end")