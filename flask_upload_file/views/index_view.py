from .. import db
from ..models import User
from flask import Blueprint, request, render_template, session, redirect
from ..services.help_func import base_query
from werkzeug.security import generate_password_hash, check_password_hash

index_view = Blueprint("index_view", __name__)


@index_view.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@index_view.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get('username')
    passwd = request.form.get('password')

    user = base_query(User).filter_by(name=name).first()
    if user is not None:
        return "用户名重复"
    else:
        passwd = generate_password_hash(passwd)   # hash加密
        user = User()
        user.name = name
        user.passwd = passwd
        db.session.add(user)
        db.session.commit()

    return "注册成功，请返回登录"


@index_view.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    name = request.form.get('username')
    passwd = request.form.get('password')

    user = base_query(User).filter_by(name=name).first()
    if user is not None:
        user_passwd = user.passwd
        if check_password_hash(user_passwd, passwd):   # hash解密
            session["user_id"] = user.id
            return redirect("/cxm/upload")
    
    return "用户名或密码错误，重新登录"


