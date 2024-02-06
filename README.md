Used Pandas to solve both problems

**Problem 1**
Calculate the max,mean and min score of each movie

**MoviesPython.py** is used to to read the scores for all the movies, find the max, average and min score for each and putt everything in one dataframe

The program first calculates the scores separately for each movie, each on a different dataframe and then joins the dataframes

I used the **pd.concat** function to join the dataframes before finding out about the **join** command

Finally I used the **dict** function to replace the Movie IDs with the actual titles to make the final dataframe more presentable


**Problem 2**
Filter out the 3 top movies for each user based on their ratings

**User Favourites.py** is used to read the user scores for all movies and find the 3 highest scoring movies for each user

I used the **groupby** and **rank** functions to create the needed dataframe

I chose to allow _ties_ for movies, so if more than 3 movies are tied for top place for a user, the program will output more than 3.
This, in most cases, results in the code outputting all of the movies that a user has scored with a 5 since most users have given 5/5 to more than three movies.
The **nlargest** function is still in the code as a comment in case we need only 3 movies per user but the selection for top 3 will be random.

As before the Movie IDs are finally replaced by the title of the movies to allow for better readability
