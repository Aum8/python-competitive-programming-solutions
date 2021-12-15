class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)

class sq(rect):
    def __init__(self,a):
        super().__init__(a,a)
