# coding: utf-8
import time


if __name__ == '__main__':
    now_time = str(time.strftime("%Y%m%d%H%M"))
    current = now_time[4:]
    diff_time = str(int(current) + 1)
    print(current, diff_time)
