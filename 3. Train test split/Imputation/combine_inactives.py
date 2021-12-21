import pandas as pd

inactives_1 = pd.read_csv('inactive_1_molecular_descriptors3.csv')
inactives_2 = pd.read_csv('inactive_2_molecular_descriptors2.csv')

#print(inactives_1.head())
#print(inactives_2.head())

frames = [inactives_1, inactives_2]
inactives = pd.concat(frames)

#print(inactives.head())

print(inactives_1.shape, inactives_2.shape, inactives.shape)

inactives.to_csv('inactives.csv')

