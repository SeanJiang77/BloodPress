import os
import secrets

# 生成一个8字节的简单密钥（可以用作SECRET_KEY）
secret_key = secrets.token_hex(8)
print(f"Generated SECRET_KEY: {secret_key}")

class Config:
    # SECRET_KEY，优先从环境变量中获取，如果没有则使用生成的密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret_key

    # 数据库连接字符串，优先从环境变量获取
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://bloodpressuser:SzXPGJf4GTaJzvYH2by4gz0Ku9hiF6iN@dpg-cs0qvqogph6c73adlsrg-a.oregon-postgres.render.com:5432/bloodpressdb?sslmode=require'

    # 禁用SQLAlchemy修改追踪，节省内存
    SQLALCHEMY_TRACK_MODIFICATIONS = False


