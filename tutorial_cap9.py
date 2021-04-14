# クラスについて

# 9.2.1 ) スコープと名前空間の例
 
 # 様々なスコープと名前空間を参照する方法。及び global と nonlocal が変数の結合に与える影響について

def scope_test():
    def do_local():
        spam = 'local spam'
    
    def do_nonlocal():          
        nonlocal spam            #<-- nonlocal代入は spam のバインディングを変化させる
        spam = "nonlocal spam"
    
    def do_global(): 
        global spam              #<-- global代入はモジュールレベルでのバインディングを変更する
        spam = 'global spam'
    
    spam = "test spam"
    do_local()              #<-- ローカル代入はscope_test内での spam のバインディングを変化させない
    print("After local assignment:", spam)     # 出力 "test spam"
    do_nonlocal()           
    print("After nonlocal assignment:", spam)  # 出力 "nonlocal spam"
    do_global()
    print("After global assignment:", spam)    # 出力 "nonlocal spam"

scope_test()
print("In global scope:", spam)  # <-- spamはスコープ外からの呼び出しの為、 global でspam を呼び込まないとならない

