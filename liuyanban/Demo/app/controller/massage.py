from app.controller import web
from flask import render_template, request, session, redirect
from app.helper.func import get_ip
from geetest import *
from app.code.code import StatusCode
from app.helper.func import ajaxReturn
from app.core.db import red
from app.model.massage import show_massage,massage_add
from app.libs.verification import login_required

@web.route('/message')
def massage():
    data = show_massage()
    try:
        uid = session['uid']
    except:
        uid = 0
    return render_template('Message.html',data=data,id=uid)


@web.route('/message/add',methods=['GET','POST'])
@login_required
def message_add():
    if request.method == "POST":
        # 用户提交的消息
        content = request.form.get('content')
        # 获取用户ip地址
        user_ip = get_ip()
        print(user_ip)
        r = red.connect()
        # 判断是否频繁发布
        if red.get_data(r,'ip'):
            # massage_add(content,uid)
            return ajaxReturn(StatusCode.A10001)
        else:
            uid = session['uid']
            massage_add(content,uid)
            red.set_data(r, 'ip', user_ip)
            return ajaxReturn(StatusCode.A10000)
    return render_template('Message.html')


captach_id = "7982db09811fc65bb0172e65feda8181"
private_key = "e9d4fc300d39c013e85c631ed791af3b"

@web.route('/getcaptcha', methods=["GET"])
@login_required
def get_captcha():
    user_id = session['uid']
    gt =  GeetestLib(captach_id, private_key)
    status = gt.pre_process(user_id)
    session[gt.GT_STATUS_SESSION_KEY] = status
    session["user_id"] = user_id
    response_str = gt.get_response_str()
    return response_str

@web.route('/validate', methods=["POST"])
@login_required
def validate_capthca():
    gt = GeetestLib(captach_id, private_key)
    status = session[gt.GT_STATUS_SESSION_KEY]
    challenge = request.form[gt.FN_CHALLENGE]
    validate = request.form[gt.FN_VALIDATE]
    seccode = request.form[gt.FN_SECCODE]
    user_id = str(session["user_id"])
    if status:
        result = gt.success_validate(challenge, validate, seccode, user_id)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    if result:
        content = request.form.get('msg')
        uid = session['uid']
        massage_add(content, uid)
        return redirect('/message')
    else:
        return 'fail'