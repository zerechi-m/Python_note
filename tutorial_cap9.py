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


# 9.3.1 ) クラス定義の構文

# class Name:
#    """A simple example class"""
#
#     def __init__():         クラスインスタンスが作成されると最初に処理される initialize
#         self.data = []

# x = Name()  でクラスのインスタンスを生成する

# __init__() がクラス内に定義されてあると新規作成されたインスタンスに対して
# 自動的に __init__() がコールされる為、特殊メソッドが定義できるようになっている。

# 9.3.2 ) クラスオブジェクト

class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# 9.3.3 ) インスタンスオブジェクト

 # インスタンスオブジェクトが理解できる操作は属性参照のみで属性名として有効なのは データ属性とメソッド

class MyClass:
    def counter():
        counter = 0

x = MyClass()
x.counter = 1

while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
del x.counter

# 9.3.4 ) メソッドオブジェクト

 # 通常 x.f() は結合後、すぐに実行されるが
 # xf = x.f() とxf に格納でき, xf を読み込むことで実行を開始する。

 

