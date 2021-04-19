# 標準ライブラリめぐり 2

# 11.1 ) 出力整形

 # reprlibモジュールはrepr()の別のバージョンである。巨大で深く入れ子になったコンテナオブジェクトを省略して表示

import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

 # pprintモジュールを使用するとビルトインオブジェクトにユーザー定義オブジェクトにも使える洗練された出力制御が使える
 # 出力はインタープリタが読める形になっており、出力結果が二行以上になる場合はデータ構造をクリアに示すようにこのプリティプリンタは行を途中で切ってインデントを追加する。

import pprint

t = [[[['black', 'cyan'], 'white',['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)    # widthでしていた幅で出力を行う

 # textwrapモジュールはテキストの各段落を指定の幅に納まるように整形する

import textwrap
doc = """The wrap() method is just like fill() except that it 
returns a list of strings instead og one big string with newlines to separate the wrapped lines"""

print(textwrap.fill(doc, width=40))  # textwrapはテキストの各段落を指定の幅に納まるように整形する


 # localeモジュールは文化固有のデータフォーマットのデータベースにアクセスするものだ。
 # localeのformat 関数にあるオプション引数 grouping を使用すると数値を桁区切りに整形できる

import locale
# print(locale.setlocale(locale.LC_ALL, 'English_United states.1252'))

conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))


# 11.2 ) テンプレート

 # stringモジュールにはエンドユーザーが編集するのに向いた構文 Templateクラスがあるこれを使用すればアプリを書き換えずにカスタマイズできる
 # 整形ではプレースホルダーとして$の後ろにPythonで有効な識別子をつけた物を使用する

from string import Template
t = Template('${village}folk send $$10 to $cause.')     # ${} か $ の後ろに文字列をおく $$で$文字がエスケープされる
print(t.substitute(village='Nottingham', cause='the ditch fund'))

 # substituteメソッドはプレースホルダーをディクショナリかキーワード引数で渡さないとKeyErrorを送り出す。
 # こうした置き換えスタイルのアプリケーションではユーザーからのデータは不完全かもしれないので、safe_substituteメソッドを使用した方がいいかもしれない


n = Template('Return the $item to $owner')
d = dict(item='unladen swallow')           # $owner のキーに該当する値を渡してないのでkeyエラーになる
# print(n.substitute(d))

print(n.safe_substitute(d))                # safe_substitute を使用すると $owner キーがないと $ownerのまま出力される

 # Templateのサブクラスでは区切り文字デリミタを変えられる
 # 例えば以下のようなフォトブラウザ向けバッチ処理リネームユーティリティでは現在の日付・画像番号・ファイル形式などのプレースホルダーに%を使用しい

# import time, os.path

# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

# class BatchRename(Template):
#     delimiter = '%'

# fmt = "yud_%n_%f"

# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))

# 11.3 ) バイナリデータレコードの処理
 
 # structモジュールは可変長のバイナリレコードを処理する関数である pack() と unpack()を提供する
 # 以下はzipfileモジュールを使わずにZIPファイルの各ヘッダ情報にループをかける例である。

# import struct

# with open('myfile.zip', 'rb') as f:
#     data = f.read()

# start = 0
# for i in range(3):
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)
    
#     start += extra_size + comp_size

# 11.4 ) マルチスレッド

  # スレッディングは順序通りに進めなくても良いタスクを分割する技法の一つ
  # 以下のコードは高水準のthreadingモジュールを利用することでメインのプログラムを走らせたままバックグラウンド処理ができることを示す

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('メインプログラムは面で動き続けています。')

background.join()
print('メインプログラムはバックグラウンド処理の終了まで待っていました。')

# 11.5 ) ログ取り

 # loggingモジュールは機能万全かつ柔軟なログ記録システムである
 # ログメッセージはファイルまたはsys.stderrに送られる

import logging

print(logging.debug('Debugging information'))
print(logging.info('Informational message'))
print(logging.warning('Warning:config file %s not found', 'server.conf'))
print(logging.error('Error occurred'))
print(logging.critical('Critical error -- shutting down'))

 # デフォルトではデバッグメッセージとINFO が抑制されており出力先は標準エラー出力になっている。
 # 出力オプションとしては他にEmail・データグラム・ソケット・HTTPサーバーへの転送などがある。

# 11.6 ) 弱参照

 # pythonはメモリ管理を自動的に行う。参照数がゼロになればメモリは解放される
 # 稀にオブジェクト群を他から使われている間にだけ追跡しなければならないという場合がたまにある。
 # ところが追跡とは参照を行うことであり、これがオブジェクトを永続させてしまう。
 # weakrefモジュールでは参照を生成せずにオブジェクトを追跡するツールを提供する。
 # 不要になったオブジェクトは自動的に弱参照表から除かれ弱参照オブジェクトへコールバックが起こる。

import weakref, gc

class A:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print( d['primary'] )    #<-- オブジェクトが生きていればとってくる
  
del a                    #<-- 参照を削除
print(gc.collect())      #<-- ガべージコレクションを実行
# print(d['primary'])      #<-- エントリは自動的に削除されているためエラーになる


# 11.7 ) リストの操作ツール

 # 多くのデータ構造はビルトインのリスト型で実現できるがライブラリを利用して、パフォーマンス上のトレードオフをのあり方を変える
 # array（配列)モジュールは同質のデータのみをコンパクトに収めるリストのオブジェクトarrayを提供する。

from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

 # collections モジュールは左端部へのappendやpopはリストより高速だが、中央部のルックアップは低速であるdequeオブジェクトをもたらす
 # このオブジェクトはキューや幅優先ツリー検索を実装するのに最適だ

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# unsearched = deque([starting_node])

# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

 # ライブラリにはこうした別実装のリストの他、ソート済みリストを操作する関数を持つbisectモジュールなども備えている

import bisect
scores = [(100, 'peal'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

 # heapqモジュールは通常のリストをベースにヒープを実装する関数を提供する。
 # ヒープでは最小値のエントリが常に位置ぜろに入る。これは完全なソートは不要だが最小の要素に何度もアクセスするアプリケーションには有用

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)           # リストをヒープ順に並べる
print(list(data))

heappush(data, -5)      # エントリの追加
print(list(data))

print([heappop(data) for i in range(3)])  # 最小のエントリから三つ取得


# 11.8 ) 10進数の浮動小数点計算

 # decimalモジュールは不動小数点10進数で計算するためのデータ型Decimalをもたらす
 # 以下のような用途ではビルトインfloatの不動小数点2進数よりもクラスの方が楽

# ・財務アプリケーションなど10進数の厳密な表現を要求される場合
# ・精度を制御する場合
# ・法や条例に沿った丸め規則が必要な場合
# ・小数点以下の有効数字を追う必要がある場合
# ・手計算と結果が一致することをユーザーが期待するようなアプリケーション

# 例えば70セントの商品に5％の税金を加える計算は浮動10進数と2進数で異なる場合がある

from decimal import *
print( round(Decimal('0.70') * Decimal('1.05'), 2 ) )

print( round(.70 * 1.05, 2))

# Decimalでは手計算を模した数学処理を行うが、浮動小数点2進数が10進数を厳密に表現できないために起きる問題を回避できる
# Decimalクラスではその厳密な表現により、余剰の計算や等値判定など2進数に向かないことを可能にする。

print( Decimal('1.00') % Decimal('0.10') )  # 0.00
print( 1.00 % 0.10 )                        # 0.999999999999999999999995  ２進数

print(sum([Decimal('0.1')] * 10) == Decimal('1.0')) # True
print(sum([0.1] * 10) == 1.0 )                      # false