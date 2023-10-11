

class Age(object):
    """docstring forAge."""

    def __init__(self, age):
        self.age = age

    def get_age(self, _age):
        if _age < 20:
            print('Hello World')
        else:
            print('hoge')

age1 = Age(10)
age2 = Age(30)
age1.get_age(30)
age2.get_age(10)
