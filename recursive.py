#Indirect recursion
def bye():
    print("bye")
    hello()
def hello():
    print("hello")
    bye()
hello()

#recursion
def helloo():
    print("hello")
    helloo()
helloo()
