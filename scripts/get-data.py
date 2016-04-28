import datetime

with open('./output/results.csv', 'w') as out:
    out.write(str(datetime.datetime.now()))
    out.write('\n\n')
    out.write('This is the data.')

