from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# 这里static_folder="../file"作用是把上级目录file变成一个路由，里面文件直接可生产url
app = Flask(__name__, static_folder='../file')

db = SQLAlchemy()
# config
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'handsome_cxm'  # 设置session加密的密钥

# init ext
db.init_app(app)

with app.app_context():

    from .views import upload_file
    app.register_blueprint(upload_file, url_prefix="/cxm")

    from .views import index_view
    app.register_blueprint(index_view, url_prefix="/cxm")

