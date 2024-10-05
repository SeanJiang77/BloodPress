import os
import secrets
secret_key = secrets.token_hex(8)  # 生成一个8字节的简单密钥
print(secret_key)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://bloodpressuser:SzXPGJf4GTaJzvYH2by4gz0Ku9hiF6iN@dpg-cs0qvqogph6c73adlsrg-a.oregon-postgres.render.com:5432/bloodpressdb') + '?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

