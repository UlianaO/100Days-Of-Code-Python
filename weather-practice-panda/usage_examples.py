# Pandas Documentation: https://pandas.pydata.org/docs/
import pandas

data = pandas.read_csv("weather_data.csv")
# Two primary DS of pandas - Series(1dim), DataFrame(2-dim).
# type(data) gives the type <class 'pandas.core.frame.DataFrame'>
print(type(data))
print(data["Temp"].mean())  # specify the name of the column, find the mean.
#  or
print(data.Temp.mean())

print(data[data.Temp == "Monday"])
#
#       Day  Temp Condition
# 0  Monday    12      Rain

print(data[data.Temp == data.Temp.max()])  # prints out a row where temp is a max temp
print("***********************")

monday = data[data.Day == "Monday"]
print(monday.Condition) # == print(data[data.Day == "Monday"].Condition)

temp = int(monday.Temp.iloc[0])  # iloc[0] get rid of the warning
tempF = temp* 9/5 + 32

# Create a dataframe from scratch if you have a dictionary
data_dict = {
    "students": ["Amy", "Nora"],
    "scores": [76, 94]
}
data_from_dict = pandas.DataFrame(data_dict)  # Creates a Data Frame
data.to_csv("new_data.csv")  # puts the data into the file