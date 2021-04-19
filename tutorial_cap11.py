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