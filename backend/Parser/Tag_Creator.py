from Error_Logger import Error_Writter_txt


def Tag_Creator(URL_File):
    try:
        file_text = open(URL_File, 'r')
        URL_Arr = []
        special_word = "/rss/"
        tag_Arr = []
        # for line in file_text.readlines():
        #     for letter in range(0, len(line)):
        #         if (letter == special_word[0]) and \
        #                 ((letter + 1) % len(line) == special_word[1]) and \
        #                 ((letter + 2) % len(line) == special_word[2]):
        #             if (letter + 2) <= len(line):
        #                 letter += 2
        #                 flag = True
        #         if flag:
        #             if letter != '/':
        #                 label += letter
        #             else:
        #                 special_counter += 1
        #             #if special_counter == 2:
        #             #    label.append(text)
        #
        # return label
        for line in file_text.readlines():
            URL_Arr.append(str(line))
        for i in range(0, len(URL_Arr)):
            counter = 0
            slash_counter = 0
            flag = False
            tag = ""
            for j in range(0, len(URL_Arr[i])):
                for g in range(0, len(special_word)):
                    if URL_Arr[j] == special_word[g]:
                        counter += 1
                    else:
                        break
                    if counter == len(special_word):
                        flag = True
                if flag:
                    if j == '/':
                        slash_counter += 1
                    tag += j
                    if slash_counter > 1:
                        tag_Arr.append(tag)
                        return tag


    except Exception as e:
        Error_Writter_txt(e, "Errors_Tag_Creator.txt")

