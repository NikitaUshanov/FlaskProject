class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@172.17.0.1:1235/db_1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ThisIsSecretKey_1234"
    BABEL_DEFAULT_LOCALE = "en"
