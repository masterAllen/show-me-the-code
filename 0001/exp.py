import random
import string

base = string.ascii_lowercase + string.ascii_uppercase + string.digits

def gen_random(count):
    # 1. Python 随机数(上面还有个base)
    return "".join(random.sample(base,count))

def gen_code(count, group):
    return "-".join([gen_random(count) for i in range(group)])

if __name__ == '__main__':
    for i in range(200):
        print(gen_code(5,4))
