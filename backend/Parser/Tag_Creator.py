from Error_Logger import Error_Writter_txt


def Tag_Creator(URL_File):
    try:
        file_text = open(URL_File, 'r')
        URL_Arr = []
        special_word = "/rss/"
        tag = []

        for line in file_text.readlines():
            URL_Arr.append(str(line))

        for i in range(0, len(URL_Arr)):
            numb = URL_Arr[i].find(special_word) + len(special_word)
            text = ""
            for j in range(numb, len(URL_Arr[i])):
                text += URL_Arr[i][j]
            tag.remove('/')

        return tag

    except Exception as e:
        Error_Writter_txt(e, "File_Lists\\" + "Errors_Tag_Creator.txt")
