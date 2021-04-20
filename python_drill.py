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