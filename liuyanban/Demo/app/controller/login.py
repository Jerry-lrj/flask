# from app.controller import web
# from flask import render_template
# @web.route('/')
# def login():
#     return render_template('login.html')

from app.controller import web
from flask import render_template,request,jsonify,session,redirect
from app.code.code import StatusCode
from app.helper.func import ajaxReturn,check_username_legitimate
from app.model.massage import show_user
#登录
@web.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('name').strip() if request.form.get('name') else ''
        password = request.form.get('password').strip() if request.form.get('password') else ''
        if not username or not password:
            return ajaxReturn(StatusCode.A10001)
        # 验证用户名的合法性
        data = check_username_legitimate(username)
        if not data:
            # 用户名不合法
            return ajaxReturn(StatusCode.A10003)
        # 验证用户名和密码
        data = show_user(username,password)
        if not data:
            # 用户名或者密码错误
            return ajaxReturn(StatusCode.A10002)
        session['uid'] = data
        return ajaxReturn(StatusCode.A10000)
    return render_template("login.html")

# 注册
@web.route('/reg',methods=['GET','POST'])


# 退出
@web.route('/logout')
def logout():
    session['uid'] = 0
    return redirect('/login')


