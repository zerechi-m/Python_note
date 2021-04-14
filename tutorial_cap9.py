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


# 9.3.5 ) クラス変数とインスタンス変数

 # クラス変数はそのクラスから生成された全てのインスタンスが共有する属性やメソッド
 # インスタンス変数は それぞれのインスタンスかに固有のデータ

class Dog:
    kind = 'canine'             #<-- クラス変数のため全てのインスタンスで共有

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
c = Dog('Buddy')
print( d.kind )    #<-- 'canine'
print( c.kind )    #<-- 'canine'
print( d.name )    #<-- "Fido"     インスタンス変数の為、固有
print( c.name )    #<-- "Buddy"    インスタンス変数の為、固有

class Dog2:
    tricks = []

    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog2("Ai")
c = Dog2("Sony")
d.add_trick("転がる")
c.add_trick("伏せ")

print( d.tricks )    # 出力 ['転がる', '伏せ'] とクラスインスタンスなので tricks がクラス共有となる
print( c.tricks )

 # 上記の場合は インスタンス変数を使用すれば インスタンスに固有したデータになる。

class Dog3:
    def __init__(self, name):
        self.name = name
        self.tricks = []             #<-- 上記のクラス変数とは違いインスタンス毎にリストが作成される
    
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog3("Ai")
c = Dog3("Sony")
d.add_trick("転がる")
c.add_trick("伏せ")

print( d.tricks )    # 出力 ['転がる'] とクラスインスタンスなので d に固有したデータとなる
print( c.tricks )    # 出力 ['伏せ'] とクラスインスタンスなので c に固有したデータとなる
