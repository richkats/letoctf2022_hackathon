from os import path, listdir, walk


def Get(SomePath):
    num_files = sum(path.isfile(path.join(SomePath, f)) for f in listdir(SomePath))
    filelist = []
    for root, dirs, files in walk(SomePath):
        for file in files:
            filelist.append(path.join(root, file))

    strList = []
    for i in range(0, num_files):
        f = open(filelist[i], 'r')
        strList.append(f.read())
        f.close()
    return strList
