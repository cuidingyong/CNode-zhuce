import os

def getpath(wenjianming):
    wenjianjia = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(wenjianjia,wenjianming)