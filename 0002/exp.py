import random
import string

# 照搬0001题目的代码
base = string.ascii_lowercase + string.ascii_uppercase + string.digits
def gen_random(count):
    return "".join(random.sample(base,count))

def gen_code(count, group):
    return "-".join([gen_random(count) for i in range(group)])

for i in range(200):
    print(gen_code(5,4))
