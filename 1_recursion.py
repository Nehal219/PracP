import sys
sys.setrecursionlimit(20)

i = 1
def rec():
    global i
    i += 1
    print(i)
    rec()

rec()