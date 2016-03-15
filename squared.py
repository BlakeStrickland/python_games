def squared(arg):
    try:
        arg = int(arg)
        return arg ** 2
    except:
        arg = str(arg)
        return arg * len(arg)


print(squared(5))
print(squared('2'))
print(squared('tim'))
