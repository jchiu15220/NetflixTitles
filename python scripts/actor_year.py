import pandas as pd

actor_year = pd.read_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\actor_year.csv', 
                 encoding='cp1252')                        

out = pd.DataFrame(columns=actor_year.columns.values)

years = set(actor_year['release_year'])
print(years)

for year in years:
    year_df = actor_year[actor_year['release_year']==year]
    year_df = year_df.sort_values(by=['actors_yearly_count'], ascending=False)
    year_df = year_df.iloc[:3,:]
    print(year_df)
    
    counter = 0
    for row_n in range(len(year_df)):
        if(year_df.iloc[row_n,2]==1):
            print('found 1')
            counter = counter + 1
            
    if(len(year_df)>2 and counter < 2):
        frames = [year_df, out]
        out = pd.concat(frames)         
    
print(out)

out.to_csv(r'C:\Users\jasmn\Documents\Personal Projects\Netflix\datasets\actor_year_out.csv')                        
