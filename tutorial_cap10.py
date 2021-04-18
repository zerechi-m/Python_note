# 標準ライブラリ巡り

# 10.1 ) OSインターフェイス

import os
print(os.getcwd())  # カレントディレクトリを返す

# os.chdir( " ディレクトリ ") ディレクトリ移動

# os.system('mkdir today') # カレントディレクトリにシステム側のシェルでmkdirを実行＊フォルダ作成

# print(dir(os))  # import os のモジュールの関数が全て入ったリストを返す。

# print(help(os)) # モジュールのdocstringから生成された詳細なマニュアルを返す

 # 日々のファイルやディレクトリの管理には shutil モジュールによる使いやすい高水準のインタフェースが良い

# import shutil
# shutil.copyfile('data.db', 'archive.db')

# 10.2 ) ファイルのワイルドカード

 # globモジュールはディレクトリをワイルドカード検索してファイル名のリストを返す関数を提供する。

import glob
print(glob.glob('*.py'))  # .pyの拡張子ファイルを全て検索して返す。

# 10.3 ) コマンドライン引数

 # ユーティリティスクリプトではコマンドライン引数を処理する場合が多い
 # 引数はsysモジュールのargv属性にリストとして格納されている。
 # 以下はコマンドラインでpython demo.py を実行した状態にある。

import sys
print(sys.argv)

 # argparseモジュールはコマンドライン引数の処理に洗練されたメカニズムを提供する。
 # 以下のスクリプトは一個以上のファイル名とオプションとして表示行数をとる。

# import argparse

# parser = argparse.ArgumentParser(prog='top', description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# 10.4 ) エラー出力のリダイレクトとプログラムの終了

 # sysモジュールにはstdin stdout stderr といった属性もついている。最後のstderr は stdoutがリダイレクトされている際にも警告やエラーメッセージが見えるように
 # するのに便利だ

import sys
print(sys.stderr.write('Warning'))

sys.exit() # 直接的な方法でスクリプトを終了したい時に使用する。

# 10.5 ) 文字列パターンマッチング

