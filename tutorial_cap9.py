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


# 9.4 ) その他色々

class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


class Bag:
    def __init__(self):
        self.data = []
    
    def add(self,x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

bag = Bag()
bag.addtwice(2)
print(bag.data)


# 9.5 ) 継承

 # 下記は、der が baseを継承している

class base():
    def a(self):
        print('私の名前はbase.aです。base.bをコールします')
        self.b()
    
    def b(self):
        print('私の名前はbase.bです。der.bでオーバーライドされます')

class der(base):   #<-- class baseの派生クラス
    def b(self):
        print('ウッヒョ！オイラはder.bだぜ')

b = base()
d = der()
b.a()
d.a()       # 基底クラスと派生クラスの関数名が 被った際には派生クラスの関数が実行される オーバーライド

 #クラスの継承で使用ができるビルトイン関数

 # ◯ インスタンスの型をチェックするには isinstance()を使用する。
 #   isinstance(obj, int) では obj.__class が int またはその派生クラスである場合にのみTrueがかえる

 # ◯ クラス継承のチェックに issubclass()を使用。 
 #   issubclass(bool, int) はTrue 返るがこれはboolがintのサブクラスであるからだ
 #   issubclass(float, int) は floatがintのサブクラスでないため Falseとなる。


# 9.5.1 ) 多重継承

 # Python では多重継承の一形態もサポートしている。複数の基底クラス定義はこのようになる。
 # 基本的に 左から右に読まれる

# class DerivedClassName(Base1, Base2, Base3):
   # 処理

# 9.6 ) プライベート変数

 # オブジェクト内部からしかアクセスできない「プライベート」インスタンス変数はPythonには存在しない。
 # ほとんどのPythonコードで守られている慣習がある。 _(アンダースコア)で設置された名前 (_spam)などはAPIの
 # 非公開部である。

# class Mapping:
#     def __init__(self, iterable):
#         self.item_list = []
#         self.__update(iterable)
    
#     def update(self, iterable):
#         for item in iterable:
#             self.item_list.append(item)

# mapping = Mapping()
# __update = update()    # update()メソッドのプライベートコピー

# class MappingSubclass(Mapping):
#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.item_list.append(item)

# 9.7 ) 残り物あれこれ

 # PascalのレコードやCの構造体のように名前のついたデータアイテムを集めておくデータ型であれば時に便利である。
 # これには空の定義を使うのがうまい

class Employee:
    pass

john = Employee() # 空のインスタンスを生成

john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.name)
 
 # 特定のデータ形を想定したPythonコードにそのデータ型のメソッドをエミュレートしたクラスを
 # 渡すことはよくある。
 # 例えば文字列バッファからデータを得るクラスにread(), readline()メソッドを定義すると
 # ファイルオブジェクトからデータを受け取って整形捨関数に引数として渡せるようになる。
 
 # インスタンスメソッドオブジェクトにも属性がある。メソッドm()に対してインスタンスオブジェクトは
 # m.__self__であり、メソッドに対応した関数オブジェクトはm.__func__である。


# 9.8 ) 反復子 (iterator)

for element in (1,2,3):
    print(element)

for key in {'one': 1, 'two': 2}:
    print(key)

 # コンテナオブジェクトの多くはfor文でループでき、このアクセススタイルはクリアで簡潔だ。反復子の利用は
 # Pythonを征服し、統一した。しかし舞台裏では for文 はコンテナオブジェクトにiter()をコールするように
 # なっている。この関数は反復オブジェクトを返し、反復子オブジェクトにはコンテナの要素に一つずつアクセスする。
 # __next__()はStopiterationの例外を送り出して終了する。

s = 'abc'
it = iter(s)

print(next(it))  # 出力 a
print(next(it))  # 出力 b
print(next(it))  # 出力 c
# print(next(it))  # StopIterationエラー

 # 自作クラスに反復子の振る舞いを追加するのは簡単である。
 # __next__()メソッドのついたオプジェクトを返す __iter__()メソッドを定義すれば良い

class Reverse:
    "シーケンスを逆順にループする反復子"
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)

while True:
    print(next(rev))