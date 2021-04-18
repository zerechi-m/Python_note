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

