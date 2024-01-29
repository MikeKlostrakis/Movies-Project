import pandas as pd

#Create the DataFrame for the Ratings

    #Add Columns to the DataFrame

columns = ['UserID', 'MovieID', 'Rating', 'TimeStamp']

df = pd.read_csv("/Users/mike/Desktop/MoviesProject/ratings.dat", names = columns, header = None, delimiter="::")

#Remove the TimeStamp column since it is not needed

df = df[['MovieID', 'Rating']]

#Create the max,min and mean groups

groupedmean = df.groupby(['MovieID'], as_index=False).mean().round(1)
groupedmean.dropna(subset=['MovieID'])
groupedmean.set_index('MovieID', inplace = True, drop = True)

groupedmax = df.groupby(['MovieID'], as_index=False).max()
groupedmax.dropna(subset=['MovieID'])
groupedmax.set_index('MovieID', inplace = True, drop = True)

groupedmin = df.groupby(['MovieID'], as_index=False).min()
groupedmin.dropna(subset=['MovieID'])
groupedmin.set_index('MovieID', inplace = True, drop = True)

final = pd.concat([groupedmax, groupedmin, groupedmean], axis=1,)
final = final.reset_index()
final.columns = ['Title', 'Max Rating', 'Min Rating', 'Average Rating']


#Create the DataFrame for the Movies

    #Add Columns to the DataFrame

columns2 = ['MovieID', 'Title', 'Gender']

df2 = pd.read_csv("/Users/mike/Desktop/MoviesProject/movies.dat", encoding = "ISO-8859-1", names = columns2, header = None, delimiter="::")

#Remove the Gender column since it is not needed

df2 = df2[['MovieID', 'Title']]
df2.dropna(subset=['MovieID'])

dict = df2.set_index('MovieID')['Title'].to_dict()

final.replace({'Title': dict}, inplace=True)

print(final)

final.to_csv ('out2.csv')