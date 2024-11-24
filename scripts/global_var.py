counter = 0


def increment():
    global counter
    counter += 1


if __name__ == "__main__":
    increment()
    print(counter)
