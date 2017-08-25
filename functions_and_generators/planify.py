class MyList(list):
    def __str__(self):
        return "<MyList>"

seq = ('abc', 3, [8, ('x', 'y'), MyList(range(5)), [100, [99, [98, [97]]]]])
#seq = [[[1, 2, 3], [4, 5]], 6]

def planify(data):
    result = []
    for elem in data:
        if hasattr(elem, '__iter__') and not isinstance(elem, str):
            result.extend(planify(elem))
        else:
            result.append(elem)
    return result

print(planify(seq))

def planify2 (data):
    for elem in data:
        if hasattr(elem, '__iter__') and not isinstance(elem, str):
            for smth in planify2(elem):
                yield smth
        else:
            yield elem


gen = planify2(seq)
print(type(gen))
print(list(gen))