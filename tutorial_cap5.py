## データ構造  ##

# 5.1 ) リストについての補足 -------------------------
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

# 5.1.2 ) リストをキューとして使用する ------------------------

from collections import deque  #python 標準ライブラリ collection deque型を使用する、リスト末尾・先頭の要素追加・削除が簡易的になる

queue = deque(["Eric", "John", "Michael"]) #deque型で変数に格納
queue.append("Terry")            #append(x)で末尾に要素追加
queue.appendleft("Graham")       #appendleft(x)で先頭に要素追加
print(queue.popleft())           #popleft()で先頭の要素削除と取り出し
print(queue.pop())               #pop()で末尾の要素削除と取り出し
print(queue)

# 5.1.3 ) リストを内包する ------------------------

squares1 = []
for x in range(10):
    squares1.append(x ** 2)

print(squares1)

  # 上記の式を一行でまとめると            # listは組み込み関数にもあるため、変数名にlistを使用するとlist()が呼べない
squares2 = list(map(lambda x : x ** 2, range(10)))
print(squares2)

squares3 = [x**2 for x in range(10)]  # 
print(squares3)

# より高度なリスト内包
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# abs関数を適用 => abs関数 絶対値を返す
print([ abs(x * 2) for x in [-4, -2, 0, 2, 4]])

# 負の数を除去
print([ x for x in [-4, -2, 0, 2, 4] if 0 <= x ])

# 各リストの要素にメソッドをコール
f = ["  banana", "strawberry   ", "passion fruits  "]
print([ fruits.strip() for fruits in f ])    

# 2乗のタプルリストを作成
print( [(x, x**2) for x in range(1, 8)] ) 

# forを2つ使用してリストを一次元化する
vec = [[1,2,3], [4,5,6], [7,8,9]]
print( [num for elem in vec for num in elem] ) 

# 5.1.4 ) 入れ子のリストの内包------------------------------------

matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]

print([[ row[i] for row in matrix] for i in range(4)])
 
 # この一文は 以下と等価である

trans = []
for i in range(4):
    trans.append([row[i] for row in matrix])

print(trans)

 # 上記の文を手順を追って記述を行うと

trans = []
for i in range(4):
    trans_a = []
    for row in matrix:
          trans_a.append(row[i])
    trans.append(trans_a)

print(trans)

 # 実際に上記のフローは複雑なためビルトイン関数zipを使用する

print(list(zip(*matrix)))

# 5.2 ) del文 ----------------------------------------------

# リストのアイテムを削除する際にインデックスを指定するのが del文 である
# del文にて削除すると、削除した値を返さないところが pop() との違いになる。

a = [0,1,2,3,4]
del a[0]          #リストの先頭を削除
print(a)

 # スライスによる削除
del a[1:3]
print(a)
 
 # リスト内全削除
del a[:]
print(a)

# 5.3 ) タプルとシーケンス ---------------------------------------

 # タプルは , で区切られた値からなる
t = 123, 'abc'
print(t)      #<-- 出力 (123, 'abc')
 
 # タプルには入れ子にすることが可能
u = t, ('x', 'y', 'z')
print(u)      #<-- 出力 ((123, 'abc'),('x', 'y', 'z'))
 
 # タプルは変更することができない
# t[0] = 456    #<-- タプルは 変更することができない  error
# タプルは immutable(不変体) の為、変数の書き換えができない

 # 要素数が0,1の時のタプルへの変換
z = 123,       #<-- 値の後ろに , を使用する
print(z)       #<-- 出力 (123, )

 # タプルのシークエンス・アンパッキング(開梱)
a, b = t       #<-- タプルの要素を一つずつ変数に入れる
print(a)       #<-- 出力 123

 # ネストしたタプルのシークエンス・アンパッキング(開梱)
(a,b),(c,d,e) = u   #<-- ネストされてあるタプル毎に()で囲むことで展開することができる
print(a,b,c,d,e)

# 5.4 ) 集合 (set) -----------------------------------------
 
 # 集合とは重複しないPythonには集合の為のデータ型まである。
 # 基本的な用途としては存在判定(membership testing)や重複エントリの排除がある。
 # 集合オブジェクトは 和(+)・交差・差(-)・対称差といった数学的演算をサポート

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # 集合には {}を使用する
print(basket)  #<-- 出力 {'orange', 'pear', 'apple', 'banana'}
 
print('orange' in basket)  #<-- 集合内の存在判定

# 二つの単語から非重複文字をとって集合演算を実演
a = set('abracadabra')    # set(x) で集合を新規作成。
b = set('attribute')
print(a, b)

 # aに存在して b には存在しない文字
print(a - b)         # aとbの重複した文字を減算し差を出力 *これは集合にしか対応していない
 
 # a または b または両者に存在する文字
print( a | b)

 # a にも b にも存在する文字
print(a & b)
 
 # a または b に共通しない文字
print( a ^ b)

 # リストの内包に似たサポートも行う
a = { x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 5.5 ) ディクショナリ  Rubyのハッシュ構造 ----------------------------------------------------------------

# Pythonでは { 'key' : 'value'}の構造で 数値や文字列は常に key として使用可能、
# タプルもキーとして使用できるが、タプル内に可変型のオプジェクトが含まれている場合は改変の可能性がある為 key として使用できない

tel = {'jack': 4098, 'sape': 4139}     # ディクショナリの作成
tel['guido'] = 4127                    # ディクショナリに追加  dic['key'] = value

print(tel['jack'])                     # ディクショナリの値の取り出し  dic['key']で取り出し

del tel['sape']                        # ディクショナリのkey を指定して削除
print(tel)

print(list(tel))                       # ディクショナリをリストに変換  ['jack', 'guido']とkeyのみがリストに変換される

print(sorted(tel))                     # key名をソートしてリストに変換
 
# dict() コンストラクタについて
    # 「 key: value」のペアのタプルから成るシーケンスからディクショナリが生成できる
              
constructor = dict([('name', 'zerechi'), ('age', 28)])
print(constructor)

    # キーワード引数でペアを指定することも可能
constructor = dict(name='Yu',age=30 )
print(constructor)


# 5.6 ) for文のループテクニック

 # ディクショナリにループをかけるときにitems()メソッドを使用すると key , value を取得

knight = { 'galand': 'the pure', 'robin': 'the brave'}
for k, v in knight.items():
    print(k, v)             #<-- 出力 galand the pure ...

 # シーケンスにループをかけるとき、 enumerate() 関数を使うと位置インデックスとそれに対応した値を同時に取得できる
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)             #<-- 出力 0 tic , 1 tac, 2 toe

 # 2つ以上のシーケンスを同時にループをかけるときは zip()関数を使用すると両者のエントリを同時に取得できる。
questions = ['name', 'quest', 'favorite']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answer):
    print('What is your {0}? It is {1}.'.format(q, a) )

 # reversed()関数を使用して逆順で出力
for i in reversed(range(1, 10, 2)):
    print(i)

 # sorted()関数  シーケンスをソート順にループする
basket = ['apple', 'pear', 'orange', 'apple']
for i in sorted(basket):
    print(i)

print(basket)  # sorted()関数はコピーをとって行う為、基のシーケンスに変更を加えない



