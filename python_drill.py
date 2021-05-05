x = ["a","b","c","d","e"]
print(x[0:-3])     # x[0:-4] はx[0:2]と等価
print(x[0:2])


# 文字数出力

d = 'dive\ninto\ncode\t'

print(len(d))  

# ディクショナリ内での計算
dic = {'Noro': 1, 'Nakao': 2, 'Miyaoka': 3}

dic['Miyaoka'] = str(5)  # dic[key] += でも演算は可能
dic['Miyaoka'] += 'あか'
print(dic)

name1,name2,name3,name4= '', 'suzuki','tanaka','sato'
selected_name = name1 or name2 or name3 or name4    
print(selected_name)


# タプルについて
t = 123,456,'test'
print(t)

# アンパックについて

dic = [
    ['Noro', 'Nakao', 'Miyaoka'],
    ['Kimura', 'Miyashita', 'Shibata'],
    ['Matsumoto', 'Tanaka', 'Ivan'],
]

print(list(zip(*dic)))

 # repr()について

import datetime
a = datetime.date.today()
print(repr(a))

# input_line = int(input())
# for i in range(input_line):
#     a = input().split()
#     hour = int(a[0][:2])
#     min = int(a[0][3:])
    
#     if min + int(a[2]) >= 60:
#         hour = hour + 1 + int(a[1])
#         min = str(min + int(a[2]) - 60)
#     else:
#         hour = str(hour + int(a[1]))
#         min = str(min + int(a[2]))
    
#     if int(hour) >= 24:
#         hour = str(int(hour) - 24)

#     if len(hour) == 1:
#         hour = '0' + hour
#     if len(min) == 1:
#         min = '0' + min
        
#     print(hour + ':' + min)

# 複数行の標準入力 例)入力：i_1 i_2


# 多重ループ

# m = int(input())
# a = [input() for i in range(m)]

# n = int(input())
# b = [input() for i in range(n)]

# for a in a:
#     for str in b:
#         if a in str:
#             print('YES')
#         else:
#             print('NO')

# for i in range(20):
#     if i%3 == 0:
#         print("{}は3で割り切れます".format(i), end=' ')
#     elif i>8 and i%2 == 0:
#         break
#     else:
#         continue 

# i = 8
# if i%3 == 0:
#    print("{}は3で割り切れます".format(i), end=' ')
# elif i>8 and i%2 == 0:
#     break
# else:
#     continue 

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# input_line = int(input())
# ele1 = 0
# ele2 = 0

# for i in range(input_line):
#     # a = input().split()
#     if 'SET' in a:
#         if a[1] == '1':
#             ele1 = int(a[2])
#         elif a[1] == '2':
#             ele2 = int(a[2])
            
#     if 'ADD' in a:
#         ele2 = ele1 + int(a[1])
    
#     if 'SUB' in a:
#         ele2 = ele1 - int(a[1])

# print(ele1, ele2)

# # H = int(input())

# p = [0, 1, 1]
# m = [0, 1, 1]
# dmg = 2
# num = 2

# while dmg < H:
#     p[0] = p[1]
#     p[1] = p[2]
    
#     m[0] = m[1]
#     m[1] = m[2]
    
#     p[2] = m[0] + m[1]
#     m[2] = p[0] + 2 * p[1]
    
#     dmg += m[2]
    
#     num += 1
    
# print(num)

# H, W, N = [ int(i) for i in input().split()] 
# a = []
# for i in range(H):
#     [b] = [ reco for reco in input().split()]
#     c = [z for z in b]
#     a.append(c)
    

for i in range(N):
    num = [int(cou) for cou in input().split()] 
    print(a[num[0]][num[1]])

n = input().split()
MM, dd = int(n[0][0:2]),int(n[0][-2:]) 
hh, mm = int(n[1][:2]), int(n[1][-2:])

if hh >= 24:
    dd += hh // 24 
    hh %= 24

print('{0:0>2}/{1:0>2} {2:0>2}:{3:0>2}'.format(MM, dd, hh, mm))

input_line = int(input())
point = 0

for i in range(input_line):
    a = input().split()
    ans = [ z for z in a[0]]
    que = [ x for x in a[1]]
    
    if que == ans:
        point += 2
    elif len(que) == len(ans):
       sabun = [ y for x, y in zip(ans, que) if x != y]
       if len(sabun) == 1:
           point += 1
           
print(point)
        