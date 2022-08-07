import json


def Json_Creator(article, link, data):
    #tag = ''
    # article = []
    # link = []
    # data = []
    data = {
        #"tag": tag,
        "article": article,
        "link": link,
        "data": data,
        }
    return json.dumps(data)
