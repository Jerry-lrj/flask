from flask import Flask

# 创建核心app函数
def create_app():
    app = Flask(__name__,template_folder='views')
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    # 注册蓝图
    register_blueprint(app)
    return app

# 注册蓝图
def register_blueprint(app):
    from app.controller import web
    app.register_blueprint(web)