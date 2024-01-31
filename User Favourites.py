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

print(userhighest)

userhighest.to_csv ('UserRanks.csv')