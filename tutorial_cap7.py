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

 # vars()関数を使用してカラムを整形して表示
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

# 7.1.3 ) 手動での文字列フォーマッティング

 #二乗三乗の表を手動で整形すると以下になる
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x**2).ljust(3),end=' ')  #rjust(x) xの数値分の幅を設定し右詰で表示する。 r = right(右詰). l = left(左詰)
    print(repr(x**3).rjust(4))

  
# 7.1.4 ) 従来形式の文字列フォーマッティング

import math
print('πの値はおおよそ%5.3fである' % math.pi)

# 7.2 ) ファイルの読み書き

 # open(ファイル名, モード, エンコーディング)
f = open('text.txt', 'a', encoding='utf-8')    
f.write('s書き込みマッスル\n')    #write()で書込み
f.close()                     #.close()で保存
  # w は書き出し専用, 
  # r は読込専用, 
  # a は書込みデータがファイル末尾に自動的に記載される, 
  # r+ は読書き両用
  # x は新規作成
  # b はバイナリモードで開く

r = open('text1.txt', 'r', encoding='utf-8')
print(r.read())          #r.read()でファイルのテキストを表示
r.close()

