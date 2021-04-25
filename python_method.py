# 標準入力について -----------------------------

# print(input("入力 : "))  # 標準入力、文字列で渡される

int("5")    # 文字列を整数に変更する int = integer

# 複数行の標準入力 例)入力：i_1 i_2

# i = list(map(int, input().split())) #i_1 i_2を取得し、iに値を入れる
# print(i[0]) #出力：i_1
# print(i[1]) #出力：i_2

# # 標準入力の複数行にわたる入力

# i = [input() for z in range(3)]
# print(i)

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
print('{0}さんの身長は{1:1.2%}cm・体重は{2:@<10.1f}kgです'.format('田中', 1, 62))

{: s}  文字列 *デフォルトの設定
{: d}  整数(10進数)
{: b}  2進数
{: x}  16進数
{: .2e}  浮動小数点(指数表記)    小数点の第2位か入力
{: .3f}  浮動小数点(小数点表記)  小数点の第3位か入力
{: .4%} % 表記に変更   四捨五入を行い小数点第4位に入力 
{: ,}  千位に , をつける  <-- 10,000
{: .x} 文字列にxを2にすると "AAAA" <-- "AA" と最大文字数を指定する
{: 10.2f} 最小幅10に指定すると '    100.00' と半角スペース10個分を取得する
{: @<15}          < で左詰に指定 / > で右詰に指定 空白を任意の文字で埋める場合は 不等号の左に任意の一文字(@)を入力

# ----------------------------------------------------------------------------------------------

# rjustメソッドについて

print(repr(7).rjust(5))  # str.rjust は指定の幅に右よせ rjust(5) スペース5個分の幅

# repr() と str() の表示の違いについて

import datetime
today = datetime.date.today()
print(str(today))           #<--- ユーザー用の出力のため、読みやすい文字列で表示
print(repr(today))          #<--- オブジェクトに返して出力するため、デバック用

a = 'aaaa'
print(a, repr(a))   #<-- reprで出力させることで、入力値をまんま出力する

# str.zfill()メソッドについて

print('使用方法'.zfill(50))  #<---  zfill(x) xの数値に合わせた幅で出力する。空白を0で埋める


# open() メソッドについて-----------------------------

 # open(ファイル名, モード, エンコーディング)
# f = open('text.txt', 'a', encoding='utf-8')    
# f.write('s書き込みマッスル\n')    #write()で書込み
# f.close()                     #.close()で保存
  # w は書き出し専用, 
  # r は読込専用, 
  # a は書込みデータがファイル末尾に自動的に記載される, 
  # r+ は読書き両用
  # x は新規作成
  # b はバイナリモードで開く

# r = open('text1.txt', 'r', encoding='utf-8')
# print(r.read())          #r.read()でファイルのテキストを表示
# r.close()


# 型について  --------------------------------------------------------------

print(type(10))  # type() とすることでカッコ内の型を出力する。 int
print(type(1.2)) # type = float
print(type('こんにちは')) # type = str

a = ['a', 'b', 'c']
print(type(a))      # type = list

  # 文字列型と数値型は結合できない
print('a' + str(12) )  # 12 は数字型なのでstrで文字列型に変更して結合

 
# or と and について --------------------------------------------------------

 # or と and のプール演算子は条件分岐意外にも使用できる

name1, name2, name3 = '', 'bbb', 'ccc'
selected_name = name1 or name2 or name3   # or の左が真の場合、左の値を返す 偽の場合右の値を返す
                                          # pythonでは一文字以上を真・0文字を偽とする

print(selected_name)   # 出力 bbb

 # and は True and True でtrue それ以外は False
  # and の左が「真」の場合、右の値を返す
  # and の左が「偽」の場合、左の値を返す

name1, name2, name3 = 1, 0, 3      # 数値の 0 は偽
selected_num = name1 and name2 and name3  # 左辺から比べて、偽の数字があれば偽を返す
print(selected_num)  # 出力 


# replace メソッド ------------------------
 
 # 文字列の置き換えに使用できる。数値(int型)には使用ができずエラーになる
 # .replace("対象の文字", "置換える文字", 回数) 第3引数には置換える回数を記載

a = 'アイウエオ アイウエオ 1'
b = a.replace('ア', 'aa', 1)  # 対象の文字に該当しなければスルーされる（エラーが出ない
c = a.replace('ウ', '')       # 第二引数に空文字を指定すると対象の文字を削除する
print(b, c )


# 大文字・小文字の変換 -----------------------------

a = 'abcd'
print( a.upper())  # str.upper()で小文字を大文字変換

b = 'ABCD'
print( b.lower())  # str.lower()で大文字を小文字変換

# リストの値変更について

[a, b] = '1','2'   # 変数に値を渡す際には
a = int(a)         # a = int(a) のように直接アクセスできる
b = int(b)
c = [a, b]
print(c)

# del 文  -------------------------------
  
  # list型に対してのdel文 
a = [1, 2, 3, 4, 5]    
del a[3]   # インデックスを指定して削除する

print(a)   # [1,2,3,5]

  # dict型に対してのdel文
b = {1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd'}
del b[2]   # キーを指定して削除を行う。

print(b)  # {1: 'aa', 3: 'cc', 4: 'dd'}