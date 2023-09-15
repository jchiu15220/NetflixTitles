import pandas as pd

actor_genre = pd.read_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\actor_genre.csv')
# print(actor_genre)                  
out = pd.DataFrame(columns=actor_genre.columns.values)
print(out)

genres = set(actor_genre['genre'])     
# print(genres) 

for genre in genres:
    genre_df = actor_genre[actor_genre['genre']==genre]
    
    genre_df = genre_df.sort_values(by=['actor_genre_count'], ascending=False)
    genre_df = genre_df.iloc[:3,:]
    
    # print(genre_df)

    counter = 0
    for row_n in range(len(genre_df)):
        if(genre_df.iloc[row_n,2]==1):
            print('found 1')
            counter = counter + 1
            
    if(len(genre_df)>2 and counter < 2):
        frames = [genre_df, out]
        out = pd.concat(frames)  
        
print(out)
out.to_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\actor_genre_out.csv') 
        
    