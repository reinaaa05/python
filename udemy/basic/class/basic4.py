#インスタンスメソット,　クラスメソット,スタティックメソット

class Human:

    class_name = 'Human' #クラス変数

    def __init__(self, name, age): #コンストラクタ
        self.name = name 
        self.age = age

    def print_name_age(self):#インスタンスメゾット
        print('インスタンスメソット実行')
        print('name = {}, age = {}'.format(self.name,self.age))

    @classmethod
    def print_class_name(cls,msg): #クラスメソット
        print('クラスメソット実行')
        print(cls.class_name)
        print(msg)
    
    @staticmethod
    def print_msg(msg): #スタティックメソット
        print('スタティックメソット実行')
        print(msg)


Human.print_class_name('こんにちは')
man = Human('桜木',18)
man.print_name_age()
man.print_msg('Hello static')
Human.print_msg('Hello static')