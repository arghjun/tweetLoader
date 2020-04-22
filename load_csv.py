import pandas 

data = pandas.read_csv('test.csv', error_bad_lines=False)

print(data.head())

