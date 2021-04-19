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
 