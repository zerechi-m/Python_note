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
