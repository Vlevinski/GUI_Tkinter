
# lambda #1
def odd():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda: c))
    return funcs # c will be looked up later

# does not remember current c
for func in odd():
    print(func(), end=' ') # OOPS: print 7 g's, not a,b,c,... !

print()

# lambda #2
def odd():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda c=c: c))
    return funcs # force to remember c now

# defaults eval now
for func in odd():
    print(func(), end=' ') # OK: now prints a,b,c,...

# lambda #3
funcs = []
for c in 'abcdefg':
    funcs.append((lambda c=c: c)) # enclosing scope is module

print()

# force to remember c now
# else prints 7 g's again
for func in funcs:
    print(func(), end=' ') # OK: prints a,b,c,...
