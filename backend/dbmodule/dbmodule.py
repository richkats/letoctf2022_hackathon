import pymongo
import string
import random
import hashlib
import re
from db_creds import DB_PASS
# from letoctf2022_hackathon.backend.Parser.parser import parser



def check_email(email):
    if re.search('.*@.*\..{2,4}', email):
        return True
    else:
        return False


class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient(
            f"mongodb+srv://MediaConeDB:{DB_PASS}@cluster0.6gmfovn.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client.mediacone_db
        self.users_col = self.db.users
        self.tasks_col = self.db.tasks
        self.top_news_col = self.db.top_news


    @staticmethod
    def _insert_document(collection, data):
        """ Function to insert a document into a collection and
        return the document's id.
        """
        return collection.insert_one(data).inserted_id

    @staticmethod
    def _create_salt(length=15):
        letters = string.digits
        salt = ''.join(random.choice(letters) for i in range(10))
        return salt

    @staticmethod
    def count_documents(collection, **kwargs):
        print(kwargs)
        return collection.count_documents(kwargs)

    # -----------------USERS------------------

    def get_user_id(self, **kwargs):
        criteria = kwargs
        if self.users_col.count_documents(criteria) == 1:
            try:
                return str(self.users_col.find_one(criteria)['_id'])
            except TypeError:
                return 0
        else:
            return 0

    def new_user(self, email, password, name, surname, role, city):
        if check_email(email):
            if not self.get_user_id(email=email):
                salt = self._create_salt()
                pass_sha256 = hashlib.sha256(bytes(password + salt, encoding='UTF-8')).hexdigest()
                user = {'email': email, 'password_hash': pass_sha256, 'salt': salt,
                        'surname': surname, 'name': name, 'city': city, 'role': role}

                return self._insert_document(self.users_col, user)
            else:
                return 0
        else:
            return 0

    def check_login(self, email, password):
        user = self.get_user(email=email)
        if user:
            salt = user['salt']
            salted_hash = hashlib.sha256(bytes(password + salt, encoding='UTF-8')).hexdigest()

            if salted_hash == user['password_hash']:
                return True
            else:
                return False
        else:
            return False



    def get_users(self, **kwargs):
        cursor = self.users_col.find(kwargs)

        result = []
        for user in cursor:
            result.append(user)
        return result

    def get_user(self, _id='', **kwargs):
        user = self.users_col.find_one(kwargs)
        user.update({'_id': str(user['_id'])})
        return user

    def remove_user(self, remove_connected=True, **kwargs):
        criteria = kwargs

        if self.users_col.count_documents(criteria) == 1:
            if remove_connected:
                email = self.get_user(**kwargs)['email']
                self.remove_tasks(user=email)
            return self.users_col.delete_one(criteria)
        else:
            return 0

    def remove_users(self, **kwargs):
        if self.users_col.count_documents(kwargs) >= 1:
            return self.users_col.delete_one(kwargs)
        else:
            return 0

    #-----------------TASKS------------------

    def new_task(self, user_id, task_title, task_content, tags):
        if self.get_user(_id=user_id):
            task = {'user_id': user_id, 'title': task_title, 'content': task_content, 'tags': tags}
            return self._insert_document(self.tasks_col, task)
        else:
            return 0

    def get_tasks_by_user(self, _id=''):

        criteria = {'user_id': _id}
        cursor = self.tasks_col.find(criteria)

        result = []
        for task in cursor:
            task.update({'_id': str(task['_id'])})
            result.append(task)
        return result

    def remove_task(self, **kwargs):
        criteria = kwargs

        if self.tasks_col.count_documents(criteria) == 1:
            return self.tasks_col.delete_one(criteria)
        else:
            return 0

    def remove_tasks(self, **kwargs):
        return self.tasks_col.delete_many(kwargs)

    # def collect_news(self, user_id):
    #     news = parser()
    #
    #     result = []
    #     a = 0
    #     for tag in news:
    #         for i in range(len(news[a]['tag']['article'][0])):
    #             title = news[tag]['article'][0][i].decode()
    #             news_tag = tag
    #             url = news[tag][1][i]
    #             date = news[tag][2][i]
    #             result.append({'title': title, 'tag': news_tag, 'url': url, 'date': date})
    #         a+=1
    #
    #     for task in result:
    #         self.new_task(user_id, task['title'], task['date'], task['tag'])

if __name__ == '__main__':
    db = MongoDB()


