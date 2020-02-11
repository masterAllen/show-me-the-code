from hashlib import sha256
from hmac import HMAC
import os

# 1. Python 加密方式
def encrypt_password(password,salt=None):
    if not salt:
        salt = os.urandom(8)

    result = password.encode('utf-8')
    for i in range(10):
        result = HMAC(result,salt,sha256).digest()

    return salt + result

def check_password(input_password, righ_hash):
    return righ_hash == encrypt_password(input_password, right_hash[:8])

if __name__ == '__main__':
    password = input('请输入密码: ')
    right_hash = encrypt_password(password)

    input_password = input('请输入密码: ')

    if check_password(input_password, right_hash):
        print('密码正确')
    else:
        print('密码错误')
