import pandas as pd

columns = ['UserID', 'MovieID', 'Rating', 'TimeStamp']

df = pd.read_csv("/Users/mike/Desktop/MoviesProject/ratings.dat", names = columns, header = None, delimiter="::")

df = df[['UserID', 'MovieID', 'Rating']]

#df2=df.groupby(['UserID'])['Rating'].nlargest(3)

df['Rank'] = df.groupby('UserID')['Rating'].rank(ascending = False, method = 'min')

userhighest = df[df['Rank'] <= 3]

userhighest = userhighest[['UserID', 'MovieID', 'Rating']]

#print(df2)

#df2.to_csv ('UserFavs.csv')

#OPTIONAL: Renaming the MovieIDs to the actual Movie Names

columns2 = ['MovieID', 'Title', 'Gender']

df3 = pd.read_csv("/Users/mike/Desktop/MoviesProject/movies.dat", encoding = "ISO-8859-1", names = columns2, header = None, delimiter="::")

#Remove the Gender column since it is not needed

userhighest.columns = ['UserID', 'Title', 'Rating']

df3 = df3[['MovieID', 'Title']]
df3.dropna(subset=['MovieID'])

dict = df3.set_index('MovieID')['Title'].to_dict()

userhighest.replace({'Title': dict}, inplace=True)

print(userhighest)

userhighest.to_csv ('UserRanks.csv')