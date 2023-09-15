import pandas as pd

genre_year = pd.read_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\genre_year.csv')                        
# print(genre_year.head())

gen_out = pd.DataFrame(columns=['type', 'release_year', 'genre', 'genres_yearly_count'])
tv_out = pd.DataFrame(columns=['type', 'release_year', 'genre', 'genres_yearly_count'])
movie_out = pd.DataFrame(columns=['type', 'release_year', 'genre', 'genres_yearly_count'])

years = set(genre_year['release_year'])


for year in years:
    gen_df = genre_year[genre_year['release_year'] == year]
    tv_df = gen_df[gen_df['type'] == 'TV Show']
    movie_df = gen_df[gen_df['type'] == 'Movie']

    gen_df = gen_df.sort_values(by=['genres_yearly_count'], ascending=False)
    tv_df = tv_df.sort_values(by=['genres_yearly_count'], ascending=False)
    movie_df = movie_df.sort_values(by=['genres_yearly_count'], ascending=False)

    gen_df = gen_df.iloc[:3,:]
    tv_df = tv_df.iloc[:3,:]
    movie_df = movie_df.iloc[:3,:]
    
    # Gen
    counter = 0
    for row_n in range(len(gen_df)):
        if(gen_df.iloc[row_n,3] == 1):
            counter = counter + 1
    if(len(gen_df) > 2 and counter < 2):
        frames = [gen_df, gen_out]
        gen_out = pd.concat(frames)
        
    # TV
    counter = 0
    for row_n in range(len(tv_df)):
        if(tv_df.iloc[row_n,3] == 1):
            counter = counter + 1
    if(len(tv_df)>2 and counter < 2):
        frames = [tv_df, tv_out]
        tv_out = pd.concat(frames)
        
    # print(tv_out)
        
    # Movie
    counter = 0
    for row_n in range(len(movie_df)):
        if(movie_df.iloc[row_n,3] == 1):
            counter = counter + 1
    if(len(movie_df) > 2 and counter < 2):
        frames = [movie_df, movie_out]
        movie_out = pd.concat(frames)
        
gen_out.to_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\gen_year.csv')     
tv_out.to_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\tv_year.csv')     
movie_out.to_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\movie_year.csv')     
        
    
        
    
        