import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr=[]
    w , h = 0,0
    w_index, h_index = 0,0

    for i in range(6):
        a,b = map(int,input().split())
        arr.append((a, b))

        if a == 1 or a==2:
            if (w < b):
                w = b
                w_index = i
        elif a== 3 or a==4:
            if (h < b):
                h = b
                h_index = i

    s_h = abs(arr[(w_index - 1)%6][1] - arr[(w_index + 1)%6][1])
    s_w = abs(arr[(h_index - 1)%6][1] - arr[(h_index + 1)%6][1])

    print(((w * h) - (s_w*s_h)) * n)

