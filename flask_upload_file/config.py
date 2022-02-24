import os


class Config(object):

    # mysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ch1315203091@150.158.85.169:3306/cxm_develop"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc'])   # 允许上传的文件类型

    UPLOAD_FOLDER = os.path.join(os.getcwd(), "file")
