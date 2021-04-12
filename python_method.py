# 標準入力について -----------------------------

# print(input("入力 : "))  # 標準入力、文字列で渡される

int("5")    # 文字列を整数に変更する int = integer

#-------------------------------------------


# 演算子 ------------------------------------

# print( 4 / 2 )    # 2.0 と除算は浮動小数点での出力
# print( 5 // 2 )   # 2 と浮動小数点を切り下げて表示
# print( 2 ** 3 )   # 2の3乗  ** n で n乗

# 文字列の入力と出力 ----------------------------

str1 = 'python'
# print(str1[-1])    # 文字列に対してインデックスを渡すことでスライスができる。 n が出力

# ------------------------------------------

# list 配列について ---------------------------

# list() は組込ライブラリの為、変数にlistは使用しない

list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[1:4])  # [ 始点 : 終点 ] 始点のindexは含み、終点のindexは含まない = [b,c,d]

list1.append('zz')  # array.append() で配列の最後に値を挿入
print(list1)

print(len(list1))   # len(array) で配列の数を出力

list1 = ['a', 'b', 'c']

# list1.append('x')             #list1の末尾にアイテムを追加
list1.append('x')
print(list1)

# list1.extend(iterable)         #list1の末尾に反復可能体の全アイテムを追加 iterable = list1など
list1.extend(['x', 'y', 'z'])
print(list1)

# list1.insert(i , x)             #list1のインデックスi に アイテムx を追加
list1.insert(2 , 'z') 
print(list1)

# list1.remove(x)                # list1内でアイテムxに等しい、最初のアイテムを削除する
list1.remove('z')                # list1内に対象のアイテムがなければエラーを返す  ValueError
print(list1)

# list1.pop([i])                # 指定されたインデックスi のアイテムを削除し、削除したアイテムを返す
print(list1.pop(1))

# list1.index(x[, start[, end]])  # 値がxに等しい最初のアイテムのインデックスを返す
print(list1.index('a'))

# list1.count(x)                 # リストの中で引数のアイテムx と合致したアイテムの個数を返す
print(list1.count('x'))

# list1.sort(key=None, reverse=False)  # リストをコピーを行わずソートを行う, keyがある場合は指定
list1.sort()                      # reverse= Falseで昇順, reverse=Trueで降順 
print(list1)

# list1.reverse()                # リストをコピーを行わず降順にソートを行う
list1.reverse()
print(list1)

# sorted(list1)                  #リストにコピーを行いソートを行う、変数に代入を行うことができる
new_list1 = sorted(list1)
print(37, list1)
print(37, new_list1)

# list1.copy()                  #リストのシャローコピー(浅いコピー)を返す
copy_list1 = list1.copy()        # 変数に格納する場合は 変数にlist1.copyを使用
print(copy_list1)

# list1.clear                 # リストから全てのアイテムを削除する
list1.clear()
print(list1)

# --------------------------------------------------------------------------------------------

# join関数について -----------------------------

test = ['ab', 'c', 'de']
result = '/'.join(test)   #join関数によってlistもjoinすることができる

print(result)  # 出力結果 ab/c/de

# stripメソッドについて

string = "xxxHello, Pythonxxx"
print(string.strip("x"))   # xが全て削除される  また大文字・小文字の区別はされる

fruit = ["   a", "bb  ", " c c "]           # 各要素の文字の前後にあるスペースを削除
print(  list(f.strip() for f in fruit)   )  # リストの要素 strip()で全角/半角スペースを除去


# lstrip ・ rstrip メソッドについて
string = "pPythonp"

newLStr = string.lstrip("p")  # l(left) 先頭から該当する文字一つ目だけ削除
newRStr = string.rstrip("p")  # r(right) 末尾から該当する文字一つ目だけ削除

print(newLStr)
print(newRStr)

# アンパックについて ----------------------------------------
 # タプルやリストの要素を展開して複数の変数に代入できる。

t = [0, 1, 2]
a,b,c = t       #リストやタプルの要素の数と変数の数が一致しないと引数エラーになる

print(a, b, c)

  # ネストしたリスト・タプルのアンパック
t = (0, 1, (2,3,4))
a,b,c = t
print( a, b, c)   # これではネスト分はタプルに格納されたままである

a,b,(c,d,e) = t  # ネストしている部分をタプルは(), リストは[]で囲む
print(a, b, c, d, e)  # <--  要素を展開して取得できる

  # *を使用したアンパック  python3以降のみ
t = (0,1,2,3,4)
a,b, *c = t          # a=0, b=1, c=[2,3,4] と*以下はlistにまとめられる
print(a, b, c)        

# zip関数について ----------------------
names = ["Alice", "Bob", "Charlie"]
ages = [24, 50, 18, 5] 

for name, age in zip(names, ages):   # for文の中で複数のリストの要素を同時に取得できる 
    print(name, age)

# zip関数ではそれぞれのリストの要素が異なる際、要素数が一致している部分までを返し、多い分は無視される


# map関数について --------------------------------

  # map( 関数[ lambda式 ] , iterable[反復可能体])

list_a = list(range(1, 10))
mapped_list = map(lambda x: x * 2, list_a) 
print(list(mapped_list))

# formatメソッドについて -----------------------------

print('{0}さんの身長は{1}cm・体重は{2}kgです'.format('田中', 169, 62))
  
  # string.format(位置引数, )で string内のインデックスに入れ込む
  # インデックスは省略できるため、{}{}{} でも左から参照する。

# formatメソッドの各種書式設定
 # {i : 設定} になる i はインデックスで省略可能  .1fは小数点第一位
print('{0}さんの身長は{1:1.2%}cm・体重は{2:<10.1f}kgです'.format('田中', 1, 62))

# {: s}  文字列 *デフォルトの設定
# {: d}  整数(10進数)
# {: b}  2進数
# {: x}  16進数
# {: .2e}  浮動小数点(指数表記)    小数点の第2位か入力
# {: .3f}  浮動小数点(小数点表記)  小数点の第3位か入力
# {: .4%} % 表記に変更   四捨五入を行い小数点第4位に入力 
# {: ,}  千位に , をつける  <-- 10,000
# {: .x} 文字列にxを2にすると "AAAA" <-- "AA" と最大文字数を指定する
# {: 10.2f} 最小幅10に指定すると '    100.00' と半角スペース10個分を取得する
#           < で左詰に指定 / > で右詰に指定 空白を任意の文字で埋める場合は 不等号の左に任意の一文字を入力

# ----------------------------------------------------------------------------------------------

# rjustメソッドについて

print(repr(7).rjust(5))  # str.rjust は指定の幅に右よせ rjust(5) スペース5個分の幅

# repr() と str() の表示の違いについて

import datetime
today = datetime.date.today()
print(str(today))           #<--- ユーザー用の出力のため、読みやすい文字列で表示
print(repr(today))          #<--- オブジェクトに返して出力するため、デバック用

