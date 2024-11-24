x = 10


def outer_function():
    x = 20

    def inner_fucntion():
        x = 30
        print(x)

    inner_fucntion()
    print(x)


if __name__ == "__main__":
    outer_function()
    print(x)
