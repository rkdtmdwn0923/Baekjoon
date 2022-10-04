import sys

input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    arrn = list(map(int,input().split()))
    m = int(input())
    arrm = list(map(int,input().split()))

    _dict={}

    for i in arrn:
        if i in _dict:
            _dict[i] = _dict[i]+1
        else:
            _dict[i] = 1

    for i in arrm:
        if i in _dict:
            print(_dict[i],end=' ')
        else:
            print("0",end=' ')








