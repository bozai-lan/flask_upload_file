# @Time    : 2020/3/6 13:06
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : main.py
# Software : PyCharm
from flask_upload_file import app


def main():
    app.run(host='127.0.0.1', port='8848', debug=True)


if __name__ == "__main__":
    main()

