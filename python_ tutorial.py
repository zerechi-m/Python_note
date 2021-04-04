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

# 4.4 ) for文の break と continue文

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n // x)
      break
  else:                                    # 32行目のfor文(2回目)の反復可能体を使い果たすかFalseになるとelse文が実行される
    print(n, 'is a print number')

# 4.5 ) pass文 ---------------------------------------

  # while True:
    # pass        # <---- pass文は構文的な文が必要なのにプログラム的には何もする必要がないときに使う
                # 新しくコードを記載しているときや関数や条件の本体にプレースホルダとして置いておく
                # ctrl + c で復帰

# 4.6 ) 関数の定義 --------------------------------------

def fib(n):
    """nまでのフィボナッチ級数を表示する"""      # docstring ユーザーが使用しやすいように説明書を入れる

    a,b = 0, 1
    while a < n:
        print(a, end=', ')
        a,b = b, a+b
    print()
  
# fib(100)

 # 関数のCall

f = fib         #関数の呼び出しである fib を f に代入することで、f(200)とすることで実引数を渡して関数を呼び出すことができる 
print(f(200))    # print( 関数 )とすると、処理を Noneと返す
