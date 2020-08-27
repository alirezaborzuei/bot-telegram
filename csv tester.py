import csv



if __name__ == '__main__':
    filename = "11.csv"
    header = (
        'ProductId', 'Category', 'NameProduct', 'NameImage', 'Price',
        'Link pay', 'Description', 'timestamp'
    )
    data = [
        (1, 9.2, "The Shawshank Redemption(1994)"),
        (2, 9.2, "The Godfather(1972)"),
        (3, 9, "The Godfather: Part II(1974)"),
        (4, 8.9, "Pulp Fiction(1994)")
    ]
    data2 = [
        (1, 9.2, "The Shawshank Redemption(1994)"),
        (2, 9.2, "The Godfather(1972)"),
        (3, 9, "The Godfather: Part II(1974)"),
        (4, 8.9, "Pulp Fiction(1994)")
    ]
    with open(filename, "w+", newline="") as csvfile:
        movies = csv.writer(csvfile)
        movies.writerow(header)
        for x in data:
            movies.writerow(x)

    with open(filename, "a", newline="") as csvfile:
        movies = csv.writer(csvfile)

        for x in data2:
            movies.writerow(x)