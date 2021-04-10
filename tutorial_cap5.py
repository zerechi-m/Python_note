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

# sorted(list1)                  #リストにコピーを行いソートを行う、変数に代入を行うことができる
new_list1 = sorted(list1)
print(new_list1)

# list1.reverse()                # リストをコピーを行わず降順にソートを行う
list1.reverse()
print(list1)

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

# 5.1.2 ) リストを内包する ------------------------

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