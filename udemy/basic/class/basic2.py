#インスタンス変数、クラス変数

class SampleA():
    class_val = 'class val' #クラス変数

    def set_val(self):
        self.instance_val = 'instance val' #インスタンス変数

    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

isinstance_a = SampleA() #インスタンス化
isinstance_a.set_val()
print(isinstance_a.instance_val)
isinstance_a.print_val()
print(SampleA.class_val)
print(isinstance_a.__class__.class_val) #クラス変数
isinstance_b = SampleA() #インスタンス化
isinstance_b.set_val()
isinstance_b.print_val()
isinstance_a.__class__.class_val = ' class val 2'
isinstance_b.print_val()

print('*'*100)
print(id(isinstance_a.__class__.class_val))
print(id(isinstance_a.__class__.class_val))