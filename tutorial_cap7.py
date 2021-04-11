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
print(f'')