from os import path, listdir, walk


def Get(SomePath):
    num_files = sum(path.isfile(path.join(SomePath, f)) for f in listdir(SomePath))
    filelist = []
    for root, dirs, files in walk(SomePath):
        for file in files:
            filelist.append(path.join(root, file))
    f = open(filelist[0], 'r')
    return f.read()