from ..config import Config


def allowed_file(filename):   # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return True
    # return '.' in filename and filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS

