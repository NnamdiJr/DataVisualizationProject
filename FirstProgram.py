__author__ = 'Nnamdi'

import pandas

data = pandas.read_csv('marscrater_pds.csv', low_memory=False)

print "Number of rows:", len(data) # Number of rows
print "Number of columns:", len(data.columns) # Number of columns

c1 = data['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=True)
p1 = data['LATITUDE_CIRCLE_IMAGE'].value_counts(sort=True, normalize=True)
print "Counts for LATITUDE_CIRCLE_IMAGE:", c1
print "Probability for LATITUDE_CIRCLE_IMAGE:", p1

c2 = data['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=True)
p2 = data['LONGITUDE_CIRCLE_IMAGE'].value_counts(sort=True, normalize=True)
print "Counts for LONGITUDE_CIRCLE_IMAGE:", c2
print "Probability for LONGITUDE_CIRCLE_IMAGE:", p2

c3 = data['DIAM_CIRCLE_IMAGE'].value_counts(sort=True)
p3 = data['DIAM_CIRCLE_IMAGE'].value_counts(sort=True, normalize=True)
print "Counts for DIAM_CIRCLE_IMAGE:", c3
print "Probability for DIAM_CIRCLE_IMAGE:", p3