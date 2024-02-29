def watch_time_to_sec(df_master, column_name):
    seconds_list=[]
    for i in range(len(df_master[column_name])):
        split_list=df_master[column_name].iloc[i].split('.')
        try: #inly going to use days where something is recorded
            if len(split_list)!=2: #if there is only one number(no decimals)
                total_sec=int(split_list[0])*60
            elif len(split_list)==2: #if there is a number with a decimal
                total_sec=int(split_list[0])*60+int(split_list[1])
        except ValueError:
            print('not recorded: ', df_master['year'].iloc[i],
                  df_master['month'].iloc[i], df_master['day_num'].iloc[i])

        #adding second value to list
        seconds_list+=[total_sec]

    #adding list to dataframe
    df_master[column_name +'_sec']=seconds_list
    #adding a normalized seconds list
    df_master[column_name +'_sec_norm']=df_master[column_name +'_sec']/max(seconds_list)
    
    return df_master