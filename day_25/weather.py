import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
red = data[data['Primary Fur Color'] == 'Cinnamon']
gray = data[data['Primary Fur Color'] == 'Gray']
black = data[data['Primary Fur Color'] == 'Black']
frame = {
    'Fur color': ['Gray', 'Black', 'Cinnamon'],
    'Amount': [len(gray), len(black), len(red)]
}
data_frame = pandas.DataFrame(frame)
data_frame.to_csv('Squirrel.csv')

