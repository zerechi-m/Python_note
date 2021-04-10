# 標準入力について -----------------------------

# print(input("入力 : "))  # 標準入力、文字列で渡される

int("5")    # 文字列を整数に変更する int = integer

#-------------------------------------------

# 演算子 ------------------------------------

# print( 4 / 2 )    # 2.0 と除算は浮動小数点での出力
# print( 5 // 2 )   # 2 と浮動小数点を切り下げて表示
# print( 2 ** 3 )   # 2の3乗  ** n で n乗

# 文字列の入力と出力 ----------------------------

str = 'python'
# print(str[-1])    # 文字列に対してインデックスを渡すことでスライスができる。 n が出力

# ------------------------------------------

# list 配列について ---------------------------

# list() は組込ライブラリの為、変数にlistは使用しない

list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[1:4])  # [ 始点 : 終点 ] 始点のindexは含み、終点のindexは含まない = [b,c,d]

list1.append('zz')  # array.append() で配列の最後に値を挿入
print(list1)

print(len(list1))   # len(array) で配列の数を出力

# join関数について -----------------------------

test = ['ab', 'c', 'de']
result = '/'.join(test)   #join関数によってlistもjoinすることができる

print(result)  # 出力結果 ab/c/de

# stripメソッドについて

string = "xxxHello, Pythonxxx"
print(string.strip("x"))   # xが全て削除される  また大文字・小文字の区別はされる

fruit = ["   a", "bb  ", " c c "]           # 各要素の文字の前後にあるスペースを削除
print(  list(f.strip() for f in fruit)   )  # リストの要素


# lstrip ・ rstrip メソッドについて
string = "pPythonp"

newLStr = string.lstrip("p")  # l(left) 先頭から該当する文字一つ目だけ削除
newRStr = string.rstrip("p")  # r(right) 末尾から該当する文字一つ目だけ削除

print(newLStr)
print(newRStr)