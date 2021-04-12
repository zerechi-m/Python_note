## エラーと例外

# 8.1 ) 構文エラー

 #syntax error 構文エラー

# 8.2 ) 例外 exception

 # 式や文が正しくてもエラーが起こる。実行中に検知されるエラーは例外(exception)と呼ばれ
 # 例外のほとんどはプログラムでは処理されず、エラーメッセージに現れる

# TypeError -- 型エラー
# NameError -- 名前エラー

# 8.3 ) 例外の処理 ----------------------------------------------

 # プログラムは選択した例外を処理するように書くことができる
 # 以下は有効な整数が入力されるまで入力を促し続ける.

while True:
    try:
        # x = int(input('数字を入力してください:'))
        break
    except ValueError:
        print('これは有効な数字ではありません')

  # try文の説明 
    # 最初にtry節が読み込まれる ( 上記: try ~ exceptまで)
    # 例外が送り出されなければ、except節はスキップされてtry文の実行が終わる
    # try節の実行中に例外が発生すると,try節中の残りの処理はスキップされる
    # 発生したexcept文の条件式と一致すればexcept節が実行されて、その後try文の処理へと移る
    # 例外の型がexcept節と一致しないと送り出された例外はさらに外側にあるtry文に渡される
    # ハンドラが見つからないと 未処理例外 となってエラーが発生する
  
  #except節には 複数のバンドラを設ける事ができる

   # except (RuntimeError, TypeError, NameError) のように

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in (B,C,D):
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')

 # except節に何も記載しないことで、ワイルドカード(全エラー)にすることができる
import sys 

try:
    f = open('text.txt', 'r')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OS error: {0}'.format(err))
except ValueError:
    print('データが整数に変換できません')
except:
    print('予期せぬエラー:', sys.exc_info()[0])   # <--- ただし、デバッグが難しくなるので使用に気をつける
    raise

 # except節にelse文の使用方法
  # elseを用いることにより、例外が発生しない場合のみ、コードを記載できる

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')           #<-- try節にコードを追加するよりも else節に記載
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'Lines')  #<-- 例外処理が発生しない場合のみelseが読まれ処理が行われる
        f.close()

 # 発生した例外の引数の引き出しついて

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))          #<-- 例外インスタンスの型
    print(inst.args)           #<-- .argsに格納された引数

    print(inst)                #<-- __str_により引数は直接表示可能であるが、これは例外のサブクラスでオーバーライドされ得る引数のアンパック
    x, y = inst.args           #<-- inst.argsを展開
    print('x = ', x)
    print('y = ', y)

# 8.4 ) 例外の送り出し
  # raise文にて 指定の例外を強制的に発生させることができる
# raise NameError("Hi There")    #  出力  raise NameError("Hi There") \n NameError: Hi There

 #デバッグの際に 例外が送出されるか確認したいが、try文に処理を記載する前などに使用

# try:
#     raise NameError('Hi there')
# except NameError:
#     print('例外が飛んでいきましたよ')
#     raise

# 8.5 ) 例外の連鎖 ------------------------------------------------------------------------

 # raise文にはオプションfromを付加する事ができる.
 # これは送出された例外 __cause__属性をセットすることで例外の連鎖を可能にするものだ

# raise RuntimeError from OSError

# def func():
#     raise IOError

# try:
#     func()
# except IOError as exc:
#     raise RuntimeError('データベースのオープンに失敗しました') from exc

 # 例外連鎖が自動的に起こる場合がある。例外ハンドラやfinally節の内部で例外が送出された時である
 # 例外連鎖を止めるには慣例記法の from None を使用する

try:
    open('database.sqlite')
except IOError:
    raise RuntimeError from None
 