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

# import sys
# print(sys.stderr.write('Warning'))

# sys.exit() # 直接的な方法でスクリプトを終了したい時に使用する。

# 10.5 ) 文字列パターンマッチング

 # reモジュールは高度な文字列処理を行う正規表現ツールを提供する。正規表現は複雑なマッチングや操作に簡潔で最適化された解を与える。

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# 10.6 ) 数学
 
 # mathモジュールを使用すると浮動小数点数数学用の下層のCライブラリ関数にアクセスできる。

import math
print(math.cos(math.pi / 4))

print(math.log(1024, 2))

 # randomモジュールは無作為抽出のツールを提供する

import random
print(random.choice(['apple', 'pear', 'banana'])) #<-- リストの中の要素を無作為に一つ選ぶ

print(random.sample(range(100), 10))              #<-- 0ー100までの数を10個無作為に選ぶ

print( random.randrange(6))         # 0-5までの数字を無作為に一つ選択

 # statistticsモジュールは数値データの基本統計量（平均・中央値・分散など）を求める

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print( statistics.mean(data) ) # 平均

print( statistics.median(data) )  # 中央値

print( statistics.variance(data)) # 分散

# 10.7 ) インターネットのアクセス

 # さまざまなインターネットプロトコルを処理してインターネットにアクセスするモジュールがある
 # 特にシンプルなのは URL にあるデータを取得する urllib.request と メールを送る smtplibだ

# from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
# as response:
#     for line in response:
#         line = line.decode('utf-8')   # バイナリデータをテキストにデコード
#         if 'EST' in line or 'EDT' in line:   # 頭部標準時を探す
#           print(line)

# 10.8 ) 日付と時間

 # datetimeモジュールは日付と時間を簡単にも複雑にも処理できる一連のクラスを提供する。
 # 日付と時間の計算をサポートしつつも実装の焦点は出力の整形や操作のために効果的に要素抽出することに当てられている。

from datetime import date
now = date.today()
print(now)

print(now.strftime('%Y年 %m月 %d日'))

# 10.9 ) データ圧縮

 # データのアーカイブ化と圧縮でよく使われるフォーマットの直接的なサポートが
 # zlib, gzip, bz2, lzma, zipfile といったモジュールにより提供されている

import zlib
s = b'witch witch has witch witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))

# 10.10 ) パフォーマンス計測

 # timeitモジュールは小さな処理速度の差を素早く示してくれる

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())     # この変数処理への速度
print(Timer('a,b= a,b', 'a=1; b=2').timeit())          # ダブルパッキングでの変数処理

 # timeitが微細な粒度レベルを見るのに対して、profile及びpstatsモジュールは大きめのコードブロックを律速
 # している部分を見つけるためのツールを提供する。


# 10.11 ) 品質管理
 
 # 高品質のソフトウェアを開発する方法の一つに関数を書くときにテストも一緒に書いておき開発中にテストを実行していく
 # doctestモジュールはモジュールをスキャンしてdocstringに埋め込まれたテストを検証するツールを提供する。

 # テストの構築について
 # 一般的なコールとその結果を docstring にコピー＆ペーストをするだけだ。
 # このようにするとユーザーに用例を提供してドキュメントを改善できる上に、doctestモジュールにドキュメントの正しさを補償させる

def average(values):
    """ 数値のリストから算術平均を計算
    print(average([20, 30, 40]))
    30.0
    """

    return sum(values) / len(values)

import doctest
print(doctest.testmod())

 # unittest モジュールは包括的な一連テストを別ファイルに持っておくことができる

import unittest

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
      self.assertEqual(average([20,30,70]), 40.0)
      self.assertEqual(round(average([1,5,7]), 1), 4.3)
      with self.assertRaises(ZeroDivisionError):
          average([])
      with self.assertRaises(TypeError):
          average(20, 30, 70)

unittest.main()     # コマンドラインからコールする全テストが呼び出される

