from app.core.db import User,Message

# 添加用户
def user_add(uname, pwd):
    return  User.insert(name=uname,passwd=pwd).execute()

# 判断用户是否存在
def show_user(uname, pwd):
    try:
        # 获取用户id
        uid = User.select().where(User.name == uname, User.passwd==pwd).get().id
        return uid
    except:
        uid = 0
        return uid

# 添加留言
def massage_add(content, uid):
    return Message.insert(massage=content, users_id=uid).execute()

# 展示留言
def show_massage():
    return Message.select()

