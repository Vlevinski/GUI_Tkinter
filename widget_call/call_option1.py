
# call #1
def normal():
    def action():
        return spam
    spam = 'ni'
    return action
act = normal()
print(act())

# call #2
def weird():
    spam = 42
    return (lambda: spam * 2)       # remembers spam in enclosing scope
act = weird()
print(act())

# call #3
def weird():
    tmp = (lambda: spam * 2)        # remembers spam
    spam = 42                       # even though not set till here
    return tmp
act = weird()
print(act())                        # prints 84


def weird():
    spam = 42
    handler = (lambda: spam * 2)    # func doesn't save 42 now

    spam = 50
    print(handler())                # prints 100: spam looked up now

    spam = 60
    print(handler())                # prints 120: spam looked up again now

weird()

