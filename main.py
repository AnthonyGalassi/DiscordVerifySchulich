import csv
print('DiscordVerifySchulich')

# should remove last column from csv file, aka grad year

""" count = 0
# Header list for column names in csv file
header = []

# Opens csv file reader
file = open('schulich.csv')
type(file)
csvreader = csv.reader(file)

# Reads header row initially
header = next(csvreader)

# List for Schulich Leader data
data = []

# Reads in remaining data from csv file
for row in csvreader:
    data.append(row)
    count = count + 1

file.close()

print(header)
print(count)
print(data[-1]) """

# issue with ' in csv file where it turns into a ?, needs to be fixed
# issue is with csv file provided, gotta clean the data

data = []
data.append(['Jessica', 'Dean', 'University of New Brunswick', '2020', 'Engineering', ''])
data.append(['Anthony', 'Galassi', 'Queen?s University', '2019', 'Science', ''])

for leader in data:
    leader[2] = leader[2].replace("?", "'") #Specific to Queen's University
    print(leader)
