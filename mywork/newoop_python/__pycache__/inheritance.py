class A:
    def intro(self):
        print("Hey, my friends in the house.")


class B(A):
    def barking(self):
        print("Most dogs do bark while I'm in the house.")


b = B()
b.intro()
b.barking()
