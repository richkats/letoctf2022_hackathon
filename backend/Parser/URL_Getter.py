from RSS_Creator import File_Lists_Path


def Get_URL(SomeURL):
    f = open(File_Lists_Path + "News_URL_Test.txt", "w")
    f.write(SomeURL)
    f.close()
    return 0