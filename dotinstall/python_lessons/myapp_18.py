class User:
  count = 0
  def __init__(self,name):
    User.count += 1
    self.__name = name

  def say_hi(self):
    print("hi {0}".format(self.name))

  @classmethod
  def show_info(cls):
    print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

#print(tom.__name)
print(tom._User__name)