import feedparser
from Error_Logger import Error_Writter_txt
from Tag_Creator import Tag_Creator
from Json_Creator import Json_Creator

File_Lists_Path = "File_Lists\\"
Token_Path = "Tokens\\"
File_URLS_Name_Test = "News_URL_Test.txt"
File_URLS_Name = "News_URL.txt"

def Main_Parser_Func():

    def Main_Part(Feed_List):
        Feed_List_Parsed = []
        Feed_List_Entries = []

        article = []
        link = []
        data = []

        for i in range(0, len(Feed_List)):
            Feed_List_Parsed.append(feedparser.parse(Feed_List[i]))
            Feed_List_Entries.append(Feed_List_Parsed[i].entries)
            tag = Tag_Creator(File_Lists_Path + File_URLS_Name)
            for entry in Feed_List_Entries[i]:
                article_title = entry.title
                article_link = entry.link
                article_published_at = entry.published

                #print("{}[{}]".format(article_title, article_link))
                article.append("{}".format(article_title))
                link.append("[{}]".format(article_link))
                data.append("{}".format(article_published_at))

            js = Json_Creator(tag[i], article, link, data)
            f = open(Token_Path + str(i) + '.json', 'w')
            f.write(js)
            f.close()

    def Feed_Keys_Creator(Feed_List):
        Feed_Keys = []
        flag = True
        counter = 0
        try:
            File_List_Dict_Keys = open(File_Lists_Path + "File_List_Dict_Keys.txt", 'r')
            for i in File_List_Dict_Keys:
                counter += 1
            if counter == len(Feed_List):
                flag = False
            File_List_Dict_Keys.close()
        except:
            File_List_Dict_Keys = open(File_Lists_Path + "File_List_Dict_Keys.txt", 'w')
            File_List_Dict_Keys.close()
        if flag:
            File_List_Dict_Keys = open(File_Lists_Path + "File_List_Dict_Keys.txt", 'w')
            for i in range(0, len(Feed_List)):
                Feed_Keys.append(feedparser.parse(Feed_List[i]).keys())
                File_List_Dict_Keys.write(str(Feed_Keys[i]) + '\n')
            File_List_Dict_Keys.close()
        else:
            for i in range(0, len(Feed_List)):
                Feed_Keys.append(feedparser.parse(Feed_List[i]).keys())

        Main_Part(Feed_List)


    def List_Reader_Feed_List_Creator():
        try:
            File_List_URL = open(File_Lists_Path + File_URLS_Name, 'r')
            Feed_List = []
            for lines in File_List_URL.readlines():
                Feed_List.append(str(lines))
            File_List_URL.close()
            Feed_List_Set = list(set(Feed_List))
            Feed_Keys_Creator(Feed_List_Set)

        except Exception as e:
            Error_Writter_txt(e, File_Lists_Path + "Errors.txt")

    List_Reader_Feed_List_Creator()
