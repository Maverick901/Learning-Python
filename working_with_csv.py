import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["movie_id", "movie_title", "movie_rating"])
#     writer.writerow([1, "Primal Fear", 8.6])
#     writer.writerow([2, "The Invitation", 8.0])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
