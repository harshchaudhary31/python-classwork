"""WAP a program that take the CSV file and store it in a 2D list"""

filename = "spreadSheet.csv"


def read_csv(file_name):
    file_handle = open(file_name, "r")
    data = file_handle.read()

    table = data.split("\n")

    for i in range(0, len(table)):
        row = table[i]
        table[i] = row.split(",")

    op = table

    return op


if __name__ == "__main__":
    recievedData = read_csv(filename)
    print(recievedData)
# print(type(recievedData))
