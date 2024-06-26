# 项目配置
class Config(object):
    # 是否开启调试模式
    DEBUG = True
    # 项目端口号
    PORT = 5000
    # 请求路径前缀
    URL_PREFIX = "/api"
    # 上传的图片位置
    UPLOAD_PATH = "/upload"


# SQLAlchemy配置
class SQLAlchemyConfig(object):
    # 是否追踪数据变化
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否打印底层执行的SQL
    SQLALCHEMY_ECHO = False


# Jwt配置
class JwtConfig(object):
    # Token过期时间 (单位：天)
    EXPIRE = 10000
    # 自定义秘钥
    SECRET_KEY = "LiuYuYang1024"
    # 加密方式
    ALGORITHM = "HS256"


# 配置基类
class BaseConfig(Config, SQLAlchemyConfig, JwtConfig):
    pass
