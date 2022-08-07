from RSS_Creator import Token_Path
from os import path, listdir
import requests


def num_files(SomePath):
    num_files = sum(path.isfile(path.join(SomePath, f)) for f in listdir(SomePath))
    return num_files

def Token_Sender(URL):
    number = num_files(Token_Path)
    for i in range(0, number):
        requests.post(URL, Token_Path + str(i) + ".json")

    return 0
