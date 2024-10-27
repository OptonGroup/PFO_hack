"""
Functions for processing and analyzing company data.
"""

import os
import pandas as pd

comanies_info = dict()
def get_trafic_data(trafic_file_path):
    """
    Process traffic data from Excel file and update global comanies_info.

    Args:
        trafic_file_path (str): Path to the traffic Excel file
    """
    global comanies_info
        
    header = pd.read_excel(trafic_file_path, nrows=1)
    last_col = len(header.columns)
    
    
    trafic_df = (pd.read_excel(trafic_file_path, usecols='A:D', skiprows=2))
    trafic_df = trafic_df.fillna('NAN')
    
    info_df = (pd.read_excel(trafic_file_path, skiprows=2, usecols=range(5, last_col)))
    info_df = info_df.fillna('NAN')
    info_headers = info_df.columns
    
    date_df = (pd.read_excel(trafic_file_path, usecols=range(5, last_col), nrows=1))
    date_df = date_df.T
    date_df = date_df.reset_index()
    for i in range(len(trafic_df)):        
        el = trafic_df.iloc[i].to_dict()
        
        for j in range(0, len(date_df), 2):
            for k in range(j, j+1):
                ne = dict()
                ne['Месяц'] = int(date_df[0][j].split('/')[0])*12 + int(date_df[0][j].split('/')[1])
                if int(info_df[info_headers[k]][i]) > 0:
                    ne['Перевозка'] = 1
                else:
                    ne['Перевозка'] = 0
                    
                comanies_info[el['ID']]['trafic'].append(ne)
                

def get_data(interests_file_path, appeals_file_path, trafic_file_path, ms_files_path):
    """
    Collect and process data from various sources.

    Args:
        interests_file_path (str): Path to interests Excel file
        appeals_file_path (str): Path to appeals Excel file
        trafic_file_path (str): Path to traffic Excel file
        ms_files_path (str): Path to marketing segment files directory

    Returns:
        dict: Processed company information
    """
    global comanies_info
    
    get_trafic_data(trafic_file_path=trafic_file_path)
    
    interests_df = pd.read_excel(interests_file_path).fillna('NAN')
    for i in range(len(interests_df)):
        
        el = interests_df.iloc[i].to_dict()
        ne = dict()
        ne['Месяц'] = int(el['Дата'].split('.')[1]) + int(el['Дата'].split('.')[2].split(' ')[0])*12
        if el['Состояние'] == 'Завершен неудачно':
            ne['Состояние'] = 0
        else:
            ne['Состояние'] = 1
                
        comanies_info[int(interests_df['ID'][i])]['interests'].append(ne)
    
    dc = {
        'Крупный бизнес': 4,
        'Средний бизнес': 3,
        'Малый бизнес': 2,
        'Микробизнес': 1,
        'NAN': 0
    }
    
    ms_files_names = [f for f in os.listdir(ms_files_path) if os.path.isfile(os.path.join(ms_files_path, f))]
    for ms_file_name in ms_files_names:
        marketing_list_df = (pd.read_excel(ms_files_path+ ms_file_name)).fillna('NAN')
        
        for i in range(len(marketing_list_df)):
            el = marketing_list_df.iloc[i].to_dict()
            
            comanies_info[int(marketing_list_df['ID'][i])]['Размер компании.Наименование'] = dc[el['Размер компании.Наименование']]
            comanies_info[int(marketing_list_df['ID'][i])]['Локация'] = ms_file_name.split('_')[1].split('.')[0]
    
    return comanies_info


def main():
    """
    Main function to process data and generate output.

    Returns:
        dict: Processed and analyzed company data
    """
    df = pd.read_excel('./РЖД train/Привязка ID.xlsx')
    for i in range(len(df)+1):
        comanies_info[i] = dict()
        comanies_info[i]['interests'] = list()
        comanies_info[i]['trafic'] = list()
        comanies_info[i]['appeals'] = list()
        comanies_info[i]['marketing_list'] = list()    
    
    data = get_data(
        interests_file_path='РЖД train/data/Интересы.xls',
        appeals_file_path='РЖД train/data/Обращения.xls',
        trafic_file_path='РЖД train/data/Объёмы перевозок.xls',
        ms_files_path='РЖД train/ms/'
    )

    out = dict()
    for i in range(1, 21730):
        out[i] = dict()
        data[i]['trafic'].sort(key=lambda x: -x['Месяц'])
        for j in range(len(data[i]['trafic'])):
            if data[i]['trafic'][j]['Перевозка']:
                out[i]['T'] = 24296 - data[i]['trafic'][j]['Месяц'] + 1
                break
        else:
            out[i]['T'] = 12
            
        try:
            if data[i]['Размер компании.Наименование'] != 0:
                out[i]['B'] = data[i]['Размер компании.Наименование']
            else:
                out[i]['B'] = 1
        except:
            out[i]['B'] = 1
        
        out[i]['C1'] = 0
        out[i]['C2'] = 0
        out[i]['C3'] = 0
        
        out[i]['M1'] = 12
        out[i]['M2'] = 12
        out[i]['M3'] = 12
        try:
            out[i]['Location'] = data[i]['Локация']
        except:
            out[i]['Location'] = 'underfined'
        
        data[i]['interests'].sort(key=lambda x: -x['Месяц'])
        
        for j in range(0, min(3, len(data[i]['interests']))):
            out[i][f'C{int(j)+1}'] = data[i]['interests'][j]['Состояние']
            out[i][f'M{int(j)+1}'] = 24296-data[i]['interests'][j]['Месяц'] + 1
                    
    return out
        
        
if __name__ == "__main__":
    import time
    ts = time.time()
    main()
    print(time.time() - ts)