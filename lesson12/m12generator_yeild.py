def generator_function():
    my_str = 'First string'
    yield my_str
    # freeze here
    # new next call
    my_str = 'Second string'
    yield my_str
    # second new next call
    my_str = 'Third string'
    yield my_str


if __name__ == "__main__":
    gen = generator_function()
    for g in gen:
        print(g)
        break
    # end of cycle
    # new next call
    print(next(gen))
    # second new next call
    print(next(gen))
