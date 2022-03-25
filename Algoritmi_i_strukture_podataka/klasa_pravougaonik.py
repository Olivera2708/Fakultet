class Rectangle(object):
    def __init__(self, a, b):
            self._a = a
            self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, new_value):
        self._a = new_value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_value):
        self._b = new_value

    def obim(self):
        return 2*(self._a + self._b)

    def povrsina(self):
        return self._a * self._b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    

if __name__ == "__main__":
    pravougaonik = Rectangle(3,4)
    kvadrat = Square(5)
    print(kvadrat.povrsina())
