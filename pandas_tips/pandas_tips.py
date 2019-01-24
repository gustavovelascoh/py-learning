import pandas as pd


def create_df():
    '''
    Credits to Amir (https://medium.com/@rafieian)
    '''
    df = pd.DataFrame([["Chandler Bing","party","2017-08-04 08:00:00",51],
     ["Chandler Bing","party","2017-08-04 13:00:00",60],
     ["Chandler Bing","party","2017-08-04 15:00:00",59],
     ["Harry Kane","football","2017-08-04 13:00:00",80],
     ["Harry Kane","party","2017-08-04 11:00:00",90],
     ["Harry Kane","party","2017-08-04 07:00:00",68],
     ["John Doe","beach","2017-08-04 07:00:00",63],
     ["John Doe","beach","2017-08-04 12:00:00",61],
     ["John Doe","beach","2017-08-04 14:00:00",65],
     ["Joey Tribbiani","party","2017-08-04 09:00:00",54],
     ["Joey Tribbiani","party","2017-08-04 10:00:00",67],
     ["Joey Tribbiani","football","2017-08-04 08:00:00",84],
     ["Monica Geller","travel","2017-08-04 07:00:00",90],
     ["Monica Geller","travel","2017-08-04 08:00:00",96],
     ["Monica Geller","travel","2017-08-04 09:00:00",74],
     ["Phoebe Buffey","travel","2017-08-04 10:00:00",52],
     ["Phoebe Buffey","travel","2017-08-04 12:00:00",84],
     ["Phoebe Buffey","football","2017-08-04 15:00:00",58],
     ["Ross Geller","party","2017-08-04 09:00:00",96],
     ["Ross Geller","party","2017-08-04 11:00:00",81],
     ["Ross Geller","travel","2017-08-04 14:00:00",60]],
     columns=["name","activity","timestamp","money_spent"])
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    return df

def main():
    df = create_df()
    # 1. String commands
    df["name"] = df.name.str.split(" ", expand=True)
    
    # 2. Group by and value_counts
    df.groupby('name')["activity"].value_counts()
    # name      activity
    # Chandler  party       3
    # Harry     party       2
    #           football    1
    # Joey      party       2
    #           football    1
    # John      beach       3
    # Monica    travel      3
    # Phoebe    travel      2
    #           football    1
    # Ross      party       2
    #           travel      1
    
    # 3.Unstack
    df.groupby('name')['activity'].value_counts().unstack().fillna(0)
    # activity  beach  football  party  travel
    # name                                    
    # Chandler    0.0       0.0    3.0     0.0
    # Harry       0.0       1.0    2.0     0.0
    # Joey        0.0       1.0    2.0     0.0
    # John        3.0       0.0    0.0     0.0
    # Monica      0.0       0.0    0.0     3.0
    # Phoebe      0.0       1.0    0.0     2.0
    # Ross        0.0       0.0    2.0     1.0
    
    # 4. groupby, diff, shift, and loc + A great tip for efficiency
    df = df.sort_values(by=['name','timestamp'])
    #         name  activity           timestamp  money_spent
    # 0   Chandler     party 2017-08-04 08:00:00           51
    # 1   Chandler     party 2017-08-04 13:00:00           60
    # 2   Chandler     party 2017-08-04 15:00:00           59
    # 5      Harry     party 2017-08-04 07:00:00           68
    # 4      Harry     party 2017-08-04 11:00:00           90
    # 3      Harry  football 2017-08-04 13:00:00           80
    # 11      Joey  football 2017-08-04 08:00:00           84
    # 9       Joey     party 2017-08-04 09:00:00           54
    # 10      Joey     party 2017-08-04 10:00:00           67
    # 6       John     beach 2017-08-04 07:00:00           63
    # 7       John     beach 2017-08-04 12:00:00           61
    # 8       John     beach 2017-08-04 14:00:00           65
    # 12    Monica    travel 2017-08-04 07:00:00           90
    # 13    Monica    travel 2017-08-04 08:00:00           96
    # 14    Monica    travel 2017-08-04 09:00:00           74
    # 15    Phoebe    travel 2017-08-04 10:00:00           52
    # 16    Phoebe    travel 2017-08-04 12:00:00           84
    # 17    Phoebe  football 2017-08-04 15:00:00           58
    # 18      Ross     party 2017-08-04 09:00:00           96
    # 19      Ross     party 2017-08-04 11:00:00           81
    # 20      Ross    travel 2017-08-04 14:00:00           60
    df['time_diff'] = df.groupby('name')['timestamp'].diff()
    #         name  activity           timestamp  money_spent time_diff
    # 0   Chandler     party 2017-08-04 08:00:00           51       NaT
    # 1   Chandler     party 2017-08-04 13:00:00           60  05:00:00
    # 2   Chandler     party 2017-08-04 15:00:00           59  02:00:00
    # 5      Harry     party 2017-08-04 07:00:00           68       NaT
    # 4      Harry     party 2017-08-04 11:00:00           90  04:00:00
    # 3      Harry  football 2017-08-04 13:00:00           80  02:00:00
    # 11      Joey  football 2017-08-04 08:00:00           84       NaT
    # 9       Joey     party 2017-08-04 09:00:00           54  01:00:00
    # 10      Joey     party 2017-08-04 10:00:00           67  01:00:00
    # 6       John     beach 2017-08-04 07:00:00           63       NaT
    # 7       John     beach 2017-08-04 12:00:00           61  05:00:00
    # 8       John     beach 2017-08-04 14:00:00           65  02:00:00
    # 12    Monica    travel 2017-08-04 07:00:00           90       NaT
    # 13    Monica    travel 2017-08-04 08:00:00           96  01:00:00
    # 14    Monica    travel 2017-08-04 09:00:00           74  01:00:00
    # 15    Phoebe    travel 2017-08-04 10:00:00           52       NaT
    # 16    Phoebe    travel 2017-08-04 12:00:00           84  02:00:00
    # 17    Phoebe  football 2017-08-04 15:00:00           58  03:00:00
    # 18      Ross     party 2017-08-04 09:00:00           96       NaT
    # 19      Ross     party 2017-08-04 11:00:00           81  02:00:00
    # 20      Ross    travel 2017-08-04 14:00:00           60  03:00:00    
    df['time_diff'] = df.time_diff.dt.total_seconds()
    df['row_duration'] = df.time_diff.shift(-1)
    #         name  activity      ...      time_diff  row_duration
    # 0   Chandler     party      ...            NaN       18000.0
    # 1   Chandler     party      ...        18000.0        7200.0
    # 2   Chandler     party      ...         7200.0           NaN
    # 5      Harry     party      ...            NaN       14400.0
    # 4      Harry     party      ...        14400.0        7200.0
    # 3      Harry  football      ...         7200.0           NaN
    # 11      Joey  football      ...            NaN        3600.0
    # 9       Joey     party      ...         3600.0        3600.0
    # 10      Joey     party      ...         3600.0           NaN
    # 6       John     beach      ...            NaN       18000.0
    # 7       John     beach      ...        18000.0        7200.0
    # 8       John     beach      ...         7200.0           NaN
    # 12    Monica    travel      ...            NaN        3600.0
    # 13    Monica    travel      ...         3600.0        3600.0
    # 14    Monica    travel      ...         3600.0           NaN
    # 15    Phoebe    travel      ...            NaN        7200.0
    # 16    Phoebe    travel      ...         7200.0       10800.0
    # 17    Phoebe  football      ...        10800.0           NaN
    # 18      Ross     party      ...            NaN        7200.0
    # 19      Ross     party      ...         7200.0       10800.0
    # 20      Ross    travel      ...        10800.0           NaN    
    
    # 5. Cumcount and Cumsum
    df2 = df[df.groupby('name').cumcount()==1]
    #         name activity      ...      time_diff  row_duration
    # 1   Chandler    party      ...        18000.0        7200.0
    # 4      Harry    party      ...        14400.0        7200.0
    # 9       Joey    party      ...         3600.0        3600.0
    # 7       John    beach      ...        18000.0        7200.0
    # 13    Monica   travel      ...         3600.0        3600.0
    # 16    Phoebe   travel      ...         7200.0       10800.0
    # 19      Ross    party      ...         7200.0       10800.0
    df3 = df[df.groupby('name').cumcount()==2]
    #         name  activity      ...      time_diff  row_duration
    # 2   Chandler     party      ...         7200.0           NaN
    # 3      Harry  football      ...         7200.0           NaN
    # 10      Joey     party      ...         3600.0           NaN
    # 8       John     beach      ...         7200.0           NaN
    # 14    Monica    travel      ...         3600.0           NaN
    # 17    Phoebe  football      ...        10800.0           NaN
    # 20      Ross    travel      ...        10800.0           NaN
    df['money_spent_so_far'] = df.groupby('name')['money_spent'].cumsum()
    #         name  activity         ...         row_duration  money_spent_so_far
    # 0   Chandler     party         ...              18000.0                  51
    # 1   Chandler     party         ...               7200.0                 111
    # 2   Chandler     party         ...                  NaN                 170
    # 5      Harry     party         ...              14400.0                  68
    # 4      Harry     party         ...               7200.0                 158
    # 3      Harry  football         ...                  NaN                 238
    # 11      Joey  football         ...               3600.0                  84
    # 9       Joey     party         ...               3600.0                 138
    # 10      Joey     party         ...                  NaN                 205
    # 6       John     beach         ...              18000.0                  63
    # 7       John     beach         ...               7200.0                 124
    # 8       John     beach         ...                  NaN                 189
    # 12    Monica    travel         ...               3600.0                  90
    # 13    Monica    travel         ...               3600.0                 186
    # 14    Monica    travel         ...                  NaN                 260
    # 15    Phoebe    travel         ...               7200.0                  52
    # 16    Phoebe    travel         ...              10800.0                 136
    # 17    Phoebe  football         ...                  NaN                 194
    # 18      Ross     party         ...               7200.0                  96
    # 19      Ross     party         ...              10800.0                 177
    # 20      Ross    travel         ...                  NaN                 237
    
    # 6. groupby, max, min for measuring the duration of activities
    df['activity_change'] = (df.activity!=df.activity.shift()) | (df.name!=df.name.shift())
    df['activity_num'] = df.groupby('name')['activity_change'].cumsum()
    #         name  activity      ...      activity_change  activity_num
    # 0   Chandler     party      ...                 True           1.0
    # 1   Chandler     party      ...                False           1.0
    # 2   Chandler     party      ...                False           1.0
    # 5      Harry     party      ...                 True           1.0
    # 4      Harry     party      ...                False           1.0
    # 3      Harry  football      ...                 True           2.0
    # 11      Joey  football      ...                 True           1.0
    # 9       Joey     party      ...                 True           2.0
    # 10      Joey     party      ...                False           2.0
    # 6       John     beach      ...                 True           1.0
    # 7       John     beach      ...                False           1.0
    # 8       John     beach      ...                False           1.0
    # 12    Monica    travel      ...                 True           1.0
    # 13    Monica    travel      ...                False           1.0
    # 14    Monica    travel      ...                False           1.0
    # 15    Phoebe    travel      ...                 True           1.0
    # 16    Phoebe    travel      ...                False           1.0
    # 17    Phoebe  football      ...                 True           2.0
    # 18      Ross     party      ...                 True           1.0
    # 19      Ross     party      ...                False           1.0
    # 20      Ross    travel      ...                 True           2.0
    activity_duration = df.groupby(['name','activity_num','activity'])['row_duration'].sum()
    #     name      activity_num  activity
    # Chandler  1.0           party       25200.0
    # Harry     1.0           party       21600.0
    #           2.0           football        0.0
    # Joey      1.0           football     3600.0
    #           2.0           party        3600.0
    # John      1.0           beach       25200.0
    # Monica    1.0           travel       7200.0
    # Phoebe    1.0           travel      18000.0
    #           2.0           football        0.0
    # Ross      1.0           party       18000.0
    #           2.0           travel          0.0
    activity_duration.reset_index().groupby('name').max()
    #               activity_num activity  row_duration
    # name                                         
    # Chandler           1.0    party       25200.0
    # Harry              2.0    party       21600.0
    # Joey               2.0    party        3600.0
    # John               1.0    beach       25200.0
    # Monica             1.0   travel        7200.0
    # Phoebe             2.0   travel       18000.0
    # Ross               2.0   travel       18000.0
        
    return activity_duration

if __name__ == "__main__":
    main()
    
    