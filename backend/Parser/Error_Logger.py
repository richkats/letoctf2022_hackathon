from datetime import datetime


def Error_Writter_txt(e, name="Some_Errors_List.txt"):
    try:
        errors_list = open(name, "a")
        errors_list.write(datetime.now().strftime("%H.%M") + ": ")
        errors_list.write(str(e) + '\n')
    except:
        errors_list = open(name, "w")
        errors_list.write(datetime.now().strftime("%H.%M"))
        errors_list.write(str(e) + '\n')
