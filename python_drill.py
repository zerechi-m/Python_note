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

i = list(map(int, input().split())) #i_1 i_2を取得し、iに値を入れる
print(i[0]) #出力：i_1
print(i[1]) #出力：i_2