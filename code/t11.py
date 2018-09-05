# url 错误
from urllib.request import *
from urllib.error import *
try:
    response = urlopen("https://cuiqingcai.com/index.htm")
except URLError as e:
    print(e.reason)


"""
输出:

Not Found

"""