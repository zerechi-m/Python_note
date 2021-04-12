# 入出力について

# 7.1 ) 手の込んだ入出力

year = 2021
event = 'Happy new Year'
print( f'{event}, {year}')   # f'......{x}' のfもしくはFを使用することで変数やリテラル値を参照
 
 # f'..{x}' にせずに '..{x}' とすると、 出力 ...{x} となって変数が参照できない

 # str.format()について

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)

print('{:-9} YES votes {:.2%}'.format(yes_votes, percentage))

# 7.1.1 ) フォーマット済み文字列リテラル

 # フォーマット済み文字列リテラル(f文字列)は、文字列(f'')とすることにより、{}内の式を展開する

import math
print(f'πの値はおよそ{math.pi:.3f}である')  # {式：書式設定}


# 7.1.2 ) 文字列のformatメソッド

print('We are the {} who say "{}!"'.format('knight', 'Ni'))
  # str.format(x0, x1)でformatメソッドに渡された引数を{}にオブジェクトを置き換える

 # formatメソッドにキーワード引数をとり、{}内の参照を{key}とすることもできる
print('This {food} is {adjective}.'.format(food='hamberger', adjective='absolutely horrible'))
 
 # 位置引数とキーワード引数は自由自在に混在できる
print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred', other='George'))

 # 分割したくない文字列はdictを使用する
table = {'Jack': 4098, 'Sjoerd': 4127, 'Dcab': 86372}
print('Sjoerd: {0[Sjoerd]:d}, Jack: {0[Jack]:d}, Dcab: {0[Dcab]:d}'.format(table))

 # **tableを使用すると
print('Sjoerd: {Sjoerd:d}, Jack: {Jack:d}, Dcab: {Dcab:d}'.format(**table))


# 7.1.3 ) 手動での文字列フォーマッティング

