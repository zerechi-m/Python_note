# 4.1 ) if 文 -------------------------

x = int( 0 )

if x < 0:                      # 条件式の終わりに「：」をつける
  print('負数')
elif x > 0:                    # elif == else if の略
  print('正数')


# 4.2 ) for 文 ------------------------

words = ['cat', 'window', 'defenestrate']

for w in words:                #words のindex の順番に一つずつ取り出して w に格納
  print( w , len( w ))


# 4.3 ) for 文 と range関数 ------------------------

for i in range(1 ,10, 2):             # range(5) = 0,1,2,3,4 ※ 終点は含まない
  print(i)                            # range( 2, 5 ) = 2,3,4  第一引数: 始点, 第二引数: 終点
                                      # range(0, 10, 2) = 0,2,4,6,8 第一引数 : 始点, 第二引数: 終点, 第三引数: ステップ(増分)

a = ['a', 'b', 'c', 'd', 'e']
for i in range( len(a) ):             # rangeでlistのインデックスの数を指定して、i に順番に代入していく
  print(i, a[i])