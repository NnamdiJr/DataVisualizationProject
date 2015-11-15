__author__ = 'Nnamdi'

import pandas

data = pandas.read_csv('marscrater_pds.csv', low_memory=False)

data["LAT_RANGES"] = pandas.qcut(data['LATITUDE_CIRCLE_IMAGE'], 4, labels=['1=25%tile', '2=50%tile', '3=75%tile',
                                                                           '4=100%tile'])
c4 = data["LAT_RANGES"].value_counts(sort=False)
print "Counts of Latitude Ranges:", c4

data["LONG_RANGES"] = pandas.qcut(data['LONGITUDE_CIRCLE_IMAGE'], 4, labels=['1=25%tile', '2=50%tile', '3=75%tile',
                                                                           '4=100%tile'])
c5 = data["LONG_RANGES"].value_counts(sort=False)
print "Counts of Longitude Ranges:", c5

data["DIAM_RANGES"] = pandas.cut(data['DIAM_CIRCLE_IMAGE'], [0,100,200,300,400,500,600,700,800,900,1000,1200])
c6 = data["DIAM_RANGES"].value_counts(sort=False)
print "Counts of Diameter Ranges:", c6

#print pandas.crosstab(data["DIAM_CIRCLE_IMAGE"], data["DIAM_RANGES"])