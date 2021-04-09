## データ構造  ##

# 5.1 ) リストについての補足
list = ['a', 'b', 'c']

# list.append('x')             #listの末尾にアイテムを追加
list.append('x')
print(list)

# list.extend(iterable)         #listの末尾に反復可能体の全アイテムを追加 iterable = listなど
list.extend(['x', 'y', 'z'])
print(list)

# list.insert(i , x)             #listのインデックスi に アイテムx を追加
list.insert(2 , 'z') 
print(list)

# list.remove(x)                # list内でアイテムxに等しい、最初のアイテムを削除する
list.remove('z')                # list内に対象のアイテムがなければエラーを返す  ValueError
print(list)

# list.pop([i])                # 指定されたインデックスi のアイテムを削除し、削除したアイテムを返す
print(list.pop(1))

# list.index(x[, start[, end]])  # 値がxに等しい最初のアイテムのインデックスを返す
print(list.index('a'))

# list.count(x)                 # リストの中で引数のアイテムx と合致したアイテムの個数を返す
print(list.count('x'))

# list.sort(key=None, reverse=False)  # リストをコピーを行わずソートを行う, keyがある場合は指定
list.sort()                      # reverse= Falseで昇順, reverse=Trueで降順 
print(list)

# sorted(list)                  #リストにコピーを行いソートを行う、変数に代入を行うことができる
new_list = sorted(list)
print(new_list)

# list.reverse()                # リストをコピーを行わず降順にソートを行う
list.reverse()
print(list)

# list.copy()                  #リストのシャローコピー(浅いコピー)を返す
copy_list = list.copy()        # 変数に格納する場合は 変数にlist.copyを使用
print(copy_list)

# list.clear                 # リストから全てのアイテムを削除する
list.clear()
print(list)

