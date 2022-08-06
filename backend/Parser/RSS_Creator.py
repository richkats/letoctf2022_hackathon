import feedparser
from ErrorLogger import Error_Writter_txt
from main import File_Lists_Path

def Main_Parser_Func():
    def Main_Part(Feed_Keys, length, Feed_List):
        #feed_entries = Feed_Keys[0].entries
        #feed_entries = []
        #a = [i for i in range(1, 15)]
        #feed.entries
        print(length)
        Feed_List_Parsed = []
        Feed_List_Titles = []
        Feed_List_Entries = []
        for i in range(0, length):
            Feed_List_Parsed.append(feedparser.parse(Feed_List[i]))
            Feed_List_Entries.append(Feed_List_Parsed[i].entries)
            #print("FLP: ", Feed_List_Parsed[i])
            #print("FLE: ", Feed_List_Entries[i])

        for i in range(0, length):
            for entry in Feed_List_Entries[i]:
                article_title = entry.title
                article_link = entry.link
                article_published_at = entry.published  # Unicode string
                article_published_at_parsed = entry.published_parsed  # Time object
                # article_author = entry.author  DOES NOT EXIST
                content = entry.summary
                # article_tags = entry.tags  DOES NOT EXIST

                print("{}[{}]".format(article_title, article_link))
                print("Published at {}".format(article_published_at))
                # print ("Published by {}".format(article_author))
                print("Content {}".format(content))
                # print("catagory{}".format(article_tags))

    def Feed_Keys_Creator(Feed_List):
        length = len(Feed_List)
        #Feed_Headers = []
        Feed_Keys = []
        flag = True
        counter = 0
        try:
            File_List_Dict_Keys = open(File_Lists_Path + "File_List_Dict_Keys.txt", 'r')
            for i in File_List_Dict_Keys:
                counter += 1
            if counter == length:
                flag = False
            File_List_Dict_Keys.close()
        except:
            File_List_Dict_Keys = open(File_Lists_Path + "File_List_Dict_Keys.txt", 'w')
            File_List_Dict_Keys.close()

        print(flag)
        if flag:
            File_List_Dict_Keys = open(File_Lists_Path + "File_List_Dict_Keys.txt", 'a')
            for i in range(counter, length):
                Feed_Keys.append(feedparser.parse(Feed_List[i]).keys())
                print(Feed_Keys[i])
                File_List_Dict_Keys.write(str(Feed_Keys[i]) + '\n')
            File_List_Dict_Keys.close()
        else:
            for i in range(0, length):
                Feed_Keys.append(feedparser.parse(Feed_List[i]).keys())
                print(Feed_Keys[i])

        Main_Part(Feed_Keys, length, Feed_List)


    def List_Reader_Feed_List_Creator():
        try:
            # File_List_URL = open("News_URL.txt", 'r')
            File_List_URL = open(File_Lists_Path + "News_URL_Test.txt", 'r')
            Feed_List = []
            for lines in File_List_URL.readlines():
                Feed_List.append(str(lines))
            File_List_URL.close()
            Feed_List_Set = list(set(Feed_List))
            Feed_Keys_Creator(Feed_List_Set)

        except Exception as e:
            Error_Writter_txt(e, File_Lists_Path + "Errors.txt")


    List_Reader_Feed_List_Creator()
    return

try:
    Main_Parser_Func()
except Exception as e:
    Error_Writter_txt(e, File_Lists_Path + "Errors_Main_Parser_Func.txt")



    # feed = feedparser.parse("https://finance.yahoo.com/rss/")
    #
    # # feed_title = feed['feed']['title']  # NOT VALID
    # feed_entries = feed.entries
    #
    # for entry in feed.entries:
    #     article_title = entry.title
    #     article_link = entry.link
    #     article_published_at = entry.published  # Unicode string
    #     article_published_at_parsed = entry.published_parsed  # Time object
    #     # article_author = entry.author  DOES NOT EXIST
    #     content = entry.summary
    #     # article_tags = entry.tags  DOES NOT EXIST
    #
    #     print("{}[{}]".format(article_title, article_link))
    #     print("Published at {}".format(article_published_at))
    #     # print ("Published by {}".format(article_author))
    #     print("Content {}".format(content))
    #     # print("catagory{}".format(article_tags))
    #


