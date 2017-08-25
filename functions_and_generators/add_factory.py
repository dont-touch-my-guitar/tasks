def add_factory(num):
    def inner(x):
        return x + num
    return inner

add5 = add_factory(5)
print(add5(10))
