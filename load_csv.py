import pandas 

data = pandas.read_csv('outexp.csv', error_bad_lines=False)

print(data.head())

