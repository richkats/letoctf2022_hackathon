import json


def Json_Creator(tag, article, link, data):
    #tag = ''
    # article = []
    # link = []
    # data = []
    data = {
        tag: {
        "article": article,
        "link": link,
        "data": data,
        }
        }
    return json.dumps(data)
