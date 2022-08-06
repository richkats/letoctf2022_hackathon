import pymongo
import json
import string
import random
import hashlib
import re


def check_email(email):
    if re.search('.*@.*\..{2,4}', email):
        return True
    else:
        return False


class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://MediaConeDB:zI88i5LmlIQDdQ81@cluster0.6gmfovn.mongodb.net/?retryWrites=true&w=majority")
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

    def get_user_id(self, email):
        criteria = {'email': email}
        return self.users_col.find_one(criteria)['_id']

    def new_user(self, email, password, name, surname, role, city):
        if check_email(email):
            if self.get_user_id(email):
                salt = self._create_salt()
                pass_sha256 = hashlib.sha256(bytes(password + salt, encoding='UTF-8')).hexdigest()
                user = {'email': email, 'password_hash': pass_sha256, 'salt': salt,
                        'surname': surname, 'name': name, 'city': city, 'role': role}

                return self._insert_document(self.users_col, user)
            else:
                return 0
        else:
            return 0

    def get_users(self, **kwargs):
        cursor = self.users_col.find(kwargs)

        result = []
        for user in cursor:
            result.append(user)
        return result

    def get_user(self, **kwargs):
        user = self.users_col.find_one(kwargs)
        return user

    def remove_user(self, email='', **kwargs):
        if email:
            criteria = {'email': email}.update(kwargs)
        else:
            criteria = kwargs

        if self.users_col.count_documents(criteria) == 1:
            return self.users_col.delete_one(criteria)
        else:
            return 0

    def remove_users(self, **kwargs):
        if self.users_col.count_documents(kwargs) >= 1:
            return self.users_col.delete_one(kwargs)
        else:
            return 0

    #-----------------TASKS------------------

    def new_task(self, user, task_title, task_content, tags):
        task = {'user': user, 'title': task_title, 'content': task_content, 'tags': tags}
        return self._insert_document(self.tasks_col, task)

    def get_tasks_by_user(self, email=''):

        criteria = {'user': email}
        cursor = self.users_col.find(criteria)

        result = []
        for user in cursor:
            result.append(user)
        return result

