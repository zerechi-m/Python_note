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
        x = int(input('数字を入力してください:'))
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