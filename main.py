import numpy as np
import pandas as pd

def all_events(start_date, end_date):

    df1 = pd.read_excel('все события.xlsx')
    
    needed_cols = ['system_time',
                   'fp_last_use',
                   'rules',
                   'servrules',
                   'message_type_id',
                   'message_mode',
                   'authentication_type',
                   'authentication_result',
                   'basic_field_key',
                   'pan_ucid'
                   ]

    # Convert start_date and end_date to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

     # Filter rows within the date range
    mask = (df1['system_time'].dt.date >= start_date.date()) & (df1['system_time'].dt.date <= end_date.date())
    filtered_df = df1.loc[mask]

    # Construct the output DataFrame
    all_events_list = filtered_df[needed_cols].copy()

    # print(all_events_list) # Test

    return all_events_list

def entries(start_date, end_date):

    df2 = pd.read_excel('входы.xlsx')
    
    needed_cols = ['iris_create_dttm',
                   'device_model_nm',
                   'КВ',
                   'sign_up_method_cd',
                   'A.карта',
                   'A.логин',
                   'A.пасс',
                   'A.КВ',
                   'A.ОТП',
                   'A.ПИН',
                   'program_product_interface_txt',
                   'ip_addr',
                   'web_user_id'
                   ]

    # Convert start_date and end_date to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

     # Filter rows within the date range
    mask = (df2['iris_create_dttm'].dt.date >= start_date.date()) & (df2['iris_create_dttm'].dt.date <= end_date.date())
    filtered_df = df2.loc[mask]

    # Construct the output DataFrame
    entries_list = filtered_df[needed_cols].copy()

    # print(entries_list) # Test

    return entries_list

def miracle_thing(start_date, end_date):

    df3 = pd.read_excel('чудо штучка.xlsx')
    
    needed_cols = ['i022_pos_entry_s1',
                   'ltimestamp',
                   'amount_rur',
                   'otb_amt_center',
                   'i043a_merch_name',
                   'agreement'
                   ]

    # Convert start_date and end_date to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

     # Filter rows within the date range
    mask = (df3['ltimestamp'].dt.date >= start_date.date()) & (df3['ltimestamp'].dt.date <= end_date.date())
    filtered_df = df3.loc[mask]

    # Construct the output DataFrame
    miracle_thing_list = filtered_df[needed_cols].copy()

    # print(miracle_thing_list) # Test

    return miracle_thing_list

def main():
    # Load the data
    print('Введи дату начала фрода в формате YYYY-MM-DD')
    #start_date = input()
    print('Введи дату конца фрода в формате YYYY-MM-DD')
    #end_date = input()
    start_date = '2024-08-12'
    end_date = '2024-08-15'
    # Starting...
    print('Начинаем...')
    
    miracle_thing_out = miracle_thing(start_date, end_date)
    miracle_thing_out = miracle_thing_out.rename(columns={'ltimestamp': 'date'})
    all_events_out = all_events(start_date, end_date)
    all_events_out = all_events_out.rename(columns={'system_time': 'date'})
    entries_out = entries(start_date, end_date)
    entries_out = entries_out.rename(columns={'iris_create_dttm': 'date'})

    # Sort
    merged_df = pd.merge(all_events_out, entries_out, on='date', how='outer')
    merged_df = pd.merge(merged_df, miracle_thing_out, on='date', how='outer')
    
    merged_df = merged_df.sort_values(by='date')

    merged_df = merged_df.fillna('')

    merged_df.to_excel('output.xlsx', index=False)
    
    print('Работа окончена!')
    



if __name__ == "__main__":
    main()