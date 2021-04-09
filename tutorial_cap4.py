# 4.1 ) if 文 -------------------------

# x = int( 0 )

# if x < 0:                      # 条件式の終わりに「：」をつける
#   print('負数')
# elif x > 0:                    # elif == else if の略
#   print('正数')


# # 4.2 ) for 文 ------------------------

# words = ['cat', 'window', 'defenestrate']

# for w in words:                #words のindex の順番に一つずつ取り出して w に格納
#   print( w , len( w ))


# 4.3 ) for 文 と range関数 ------------------------

# for i in range(1 ,10, 2):             # range(5) = 0,1,2,3,4 ※ 終点は含まない
#   print(i)                            # range( 2, 5 ) = 2,3,4  第一引数: 始点, 第二引数: 終点
#                                       # range(0, 10, 2) = 0,2,4,6,8 第一引数 : 始点, 第二引数: 終点, 第三引数: ステップ(増分)

# a = ['a', 'b', 'c', 'd', 'e']
# for i in range( len(a) ):             # rangeでlistのインデックスの数を指定して、i に順番に代入していく
#   print(i, a[i])

# 4.4 ) for文の break と continue文

# for n in range(2, 10):
#   for x in range(2, n):
#     if n % x == 0:
#       print(n, 'equals', x, '*', n // x)
#       break
#   else:                                    # 32行目のfor文(2回目)の反復可能体を使い果たすかFalseになるとelse文が実行される
#     print(n, 'is a print number')

# 4.5 ) pass文 ---------------------------------------

  # while True:
    # pass        # <---- pass文は構文的な文が必要なのにプログラム的には何もする必要がないときに使う
                # 新しくコードを記載しているときや関数や条件の本体にプレースホルダとして置いておく
                # ctrl + c で復帰

# 4.6 ) 関数の定義 --------------------------------------

# def fib(n):
#     """nまでのフィボナッチ級数を表示する"""      # docstring ユーザーが使用しやすいように説明書を入れる

#     a,b = 0, 1
#     while a < n:
#         print(a, end=', ')
#         a,b = b, a+b
#     print()
  
# # fib(100)

#  # 関数のCall

# f = fib         #関数の呼び出しである fib を f に代入することで、f(200)とすることで実引数を渡して関数を呼び出すことができる 
# print(f(200))    # print( 関数 )とすると、処理を Noneと返す

# # 4.7.1 ) 関数定義について

# # i = 6

# # def f(arg=i):      #実引数の中で値を代入することもできる
# #     print(arg)      #この場合の出力は 5 になる。
# # i = 5

# # f()
#    # -------------------

# # def f(a, L=[]):   # 実引数に []を使用すると、コール間で渡される値を蓄積されてしまう. <-- f(1)の出力を継承する。
# #   L.append(a)
# #   return L

# # print(f(1))   # 出力例 - [1]
# # print(f(2))   # 出力例 - [1,2]

#    # -------------------

# # def f(a, L=None):   # デフォルト値の共有を防ぐ場合は スコープ内にて[]を設定する
# #   L = []
# #   L.append(a)
# #   return L

# # print(f(1))
# # print(f(2))

# # 4.7.2 ) キーワード引数

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):  #キーワード引数は仮引数に書いてあるもののみ値を与えることができる。
#   print("-- This parrot wouldn't", action, end=' ')
#   print("if you put", voltage, "volts through it.")
#   print("-- Lovely plumage, the", type)
#   print("-- it's", state, "!")

# parrot(1000)                                         #位置引数1個
# parrot(voltage=1000)                                 #キーワード引数1個
# parrot(voltage=100000, action="Vooooom")             #キーワード引数 2個
# parrot(action="Vooooom", voltage=10000000)           #キーワード引数 2個
# parrot('a million', 'bereft of life', 'jump')        #位置引数3個
# parrot('a thousand', state='pushing up the daisies') #位置引数1個 キーワード引数2個

# キーワード引数の関数呼びだしエラー例
# parrot()                    #<--- 位置引数があるにも関わらず、実引数を渡していない
# parrot(voltage=5, 'dead')   #<--- キーワード引数の後に非キーワード引数
# parrot(110, voltage=220)    #<--- 同じ引数に2度引数を与えた
# parrot(actor='John')        #<--- 未知のキーワード引数に値を与えることはできない

# 仮引数に **名前とすることで、仮引数にない値も仮引数として利用できる

# def cheeseshop(kind, *arguments, **keyword):         # *argumentsは仮引数にない、位置指定型引数を全て含んだタプル
#   print("-- Do you have any", kind, "?")             # **keywordはディクショナリを受け取る 仮引数にない全てのキーワード引数を扱える。
#   print("-- I'm sorry, we're all out of", kind)
#   for arg in arguments:
#     print(arg)
#   print("-" * 20)
#   for kw in keyword:
#     print(kw, keyword[kw])

# cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny sir.",   # Limburger以外の位置指定引数は仮引数に表示がない為、※argumentにリストで格納
#             shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch") #キーワード引数は仮引数に該当がない為、**keywordにリストで格納

# 4.7.3 ) 特殊引数

  # pythonの関数の引数は、位置渡しと明示的なキーワード指定渡しがデフォルト

  # def f (pos1, pos2, /, pos_or_kwd, *,kwd1, kwd2):
        #    位置引数   位置またはキーワード    キーワードのみ      引数内の / , * は関数への渡され方が明示的である

# 4.7.3.4 ) 関数のその他の例

def standard_arg(arg):  #スタンダードな引数の渡し方 ＊位置引数もしくはキーワード引数
  print(arg)

standard_arg(arg=1) #もしくは standard_arg(1)でも可能

def pos_only_arg(arg, /): #関数定義に / が入っているため位置引数のみ渡せる。
  print(arg)

pos_only_arg(2) # pos_only_arg(arg=2) ではキーワード引数エラーになる

def kwd_only_arg(*, arg): #関数定義に * が入っているためキーワード引数のみ渡せる
  print(arg)

kwd_only_arg(arg=3) #kwd_only_arg(3) では位置引数のみの為、変数エラーになる。

def combined_example(pos_only, /, standard, *, kwd_only): #関数定義に/ ,* がある   /より左辺は位置引数のみ、 *より右辺はキーワード引数のみ
  print(pos_only, standard, kwd_only)

combined_example(5, 6, kwd_only=7)

# 4.7.6 ) lambda式について

add_lambda = lambda a, b: a + b  #小さな無名関数がかける

print(add_lambda(2,6))


def make_incrementer(n):      # n = 42 実引数が該当
  return lambda x: x + n      # x には f(0)の実引数が該当する

f = make_incrementer(42)
print(f(1))

# 4.7.7 ) ドキュメンテーション文字列(docstring)

def function():        #pythonの慣習で大文字から始める
  """A aaaaaaaaa         

  Bbbbbbbbbbbb"""
print(function.__doc__)  #関数名.__doc__ ドキュメンテーションを表示する

# 4.7.8 ) 関数注釈 (関数アノテーション)

  #関数における、属性と変数が受け取った引数の表示を行う
  #注釈は _annotations__属性にディクショナリとして格納

def f(ham: str, eggs: str = 'eggs'):
  print("Annotations:", f.__annotations__)  # hamとeggsの属性を表示
  print("Arguments:", ham, eggs)            # hamとeggsの変数を表示
  return ham + ' and ' + eggs

f('spam')

# 4.8 ) 幕間つなぎ：コーディングスタイル

# 1: インデントはスペース4つとして、タブは使用しない
# 2: 79文字以下で行を折り返す  *小型ディスプレイの視認性
# 3: 関数やクラスさらには関数内の大きめのブロックを分離するのに空白行を使用する
# 4: 可能であれば、コメント行は独立させる
# 5: docstring を使用    """ これがdocstringです """
# 6: 演算子やカンマの後ろにはスペースを入れるが、前には使用しない 【OK a(b, x)】【NG a( b, x )】 
# 7: クラスは関数には一貫した命名を行う。 クラスには UpperCamelCase を使用する   メソッドには lower_method スネークケース
# 8: 