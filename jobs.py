from flask_rq2 import RQ
import time

rq = RQ()


@rq.job
def calculate(x, y):
    for i in range(x+y):
        print("开始执行-----")
        print("==========:{}".format(i))
        time.sleep(2)
    print("-------end-----")
    return x + y