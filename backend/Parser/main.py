from RSS_Creator import Main_Parser_Func, File_Lists_Path
from Error_Logger import Error_Writter_txt


def main():
    try:
        Main_Parser_Func()
    except Exception as e:
        Error_Writter_txt(e, File_Lists_Path + "Errors_Main_Parser_Func.txt")


if __name__ == "__main__":
    main()