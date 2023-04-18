import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_sq = data[data["Primary Fur Color"] == "Gray"]
grey_sq_count = len(grey_sq)
print(grey_sq_count)
black_sq = data[data["Primary Fur Color"] == "Black"]
black_sq_count = len(black_sq)

data_dict = {
    "Fur Color": ["Gray", "Black"],
    "Count": [grey_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")