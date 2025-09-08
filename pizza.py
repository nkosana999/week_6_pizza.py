import sys
import csv
from tabulate import tabulate
def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:].lower() != ".csv":
        sys.exit("Not a csv file")
    else:
        try:
            print(table(sys.argv[1]))
        except FileNotFoundError:
            sys.exit("File does not exist")

def table(file_name):

    prices_headers = []
    with open(file_name) as file:
        header_list = csv.reader(file)
        for row in header_list:
            prices_headers.append(row)
    headers = prices_headers[0]
    prices = prices_headers[1:]

    return tabulate(prices,headers,tablefmt="grid")




if __name__ == "__main__":
    main()

