import redis
import pickle
import datetime
from peewee import *


class Redis:
    @staticmethod
    def connect(host='localhost', port=6379, db=0):
        r = redis.StrictRedis(host, port, db)
        return r

    # 将内存数据二进制通过序列号转为文本流，再存入redis
    @staticmethod
    def set_data(r, key, data, ex=10):
        r.set(pickle.dumps(key), pickle.dumps(data), ex)

    # 将文本流从redis中读取并反序列化，返回
    @staticmethod
    def get_data(r, key):
        data = r.get(pickle.dumps(key))
        if data is None:
            return None

        return pickle.loads(data)


red = Redis()
r = red.connect()
# re.set_data(r,'ip','127.0.0.1')
# print(red.get_data(r,'ip'))


# 连接Mysql数据库
settings = {'host': 'localhost', 'password': '', 'port': 3306, 'user': 'root'}
db = MySQLDatabase("website", **settings)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db  # 将实体与数据库进行绑定


class User(BaseModel):  # 继承自BaseModel，直接关联db，并且也继承了Model。Model有提供增删查改的函数
    name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
    passwd = CharField(verbose_name='密码', max_length=20, null=False)


class Message(BaseModel):
    massage = CharField(verbose_name='留言信息', max_length=255, null=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    users = ForeignKeyField(User)


User.create_table()
Message.create_table()

