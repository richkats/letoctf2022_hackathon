from RSS_Creator import Main_Parser_Func, File_Lists_Path, Token_Path
from Error_Logger import Error_Writter_txt
from Token_Getter import Get

def parser():
    try:
        Main_Parser_Func()
    except Exception as e:
        print(Error_Writter_txt(e, File_Lists_Path + "Errors_Main_Parser_Func.txt"))
    return Get(Token_Path)

if __name__ == "__main__":
    print(main())
