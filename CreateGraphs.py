__author__ = 'Nnamdi'

import pandas
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv('marscrater_pds.csv', low_memory=False)

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

seaborn.distplot(data['LATITUDE_CIRCLE_IMAGE'], kde=False);
plt.xlabel('Latitudes')
plt.title('Mars Crater Data Latitudes Histogram')
desc1 = data['LATITUDE_CIRCLE_IMAGE'].describe()
print desc1

seaborn.distplot(data['LONGITUDE_CIRCLE_IMAGE'], kde=False);
plt.xlabel('Longitudes')
plt.title('Mars Crater Data Longitudes Histogram')
desc2 = data['LONGITUDE_CIRCLE_IMAGE'].describe()
print desc2

seaborn.distplot(data['DIAM_CIRCLE_IMAGE'], kde=False);
plt.xlabel('Diameters')
plt.title('Mars Crater Data Diameters Histogram')
desc3 = data['DIAM_CIRCLE_IMAGE'].describe()
print desc3
print data['DIAM_CIRCLE_IMAGE'].mode()
print data['DIAM_CIRCLE_IMAGE'].median()

scat1 = seaborn.regplot(x="LATITUDE_CIRCLE_IMAGE", y="DIAM_CIRCLE_IMAGE", data=data)
plt.xlabel('Craters Latitudes')
plt.ylabel('Craters Diameters')
plt.title('Scatterplot for Association Between Crater Diameter and Latitudes')