import os
import secrets

# 生成一个8字节的简单密钥（可以用作SECRET_KEY）
secret_key = secrets.token_hex(8)
print(f"Generated SECRET_KEY: {secret_key}")

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://bloodpressuser:SzXPGJ14GTaJzvYH2by4gz0Ku9hiF6iN@dpg-cs0qvqogph6c73adlsrg-a.oregon-postgres.render.com:5432/bloodpressdb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


