__author__ = 'romulo'
from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table

dict_pmus = {36: 'UFJF', 45: 'UFAC', 54: 'UFAM', 63: 'UFBA', 72: 'UFRGS', 81: 'UNIFAP', 90: 'UNIFEI', 99: 'UNB',
             108: 'COPPE', 117: 'UFC', 126: 'USP-SC', 135: 'UTFPR', 144: 'UFSC', 153: 'UNIR', 162: 'UFMT',
             171: 'UNIPAMPA', 180: 'UFMG', 189: 'UFMS', 198: 'UFPE', 207: 'UFT',828: '01_ILS_BAU', 871: 'AT-98012',
             898: '02_BAU_ILS_2', 925: 'RU-98012', 952: '03_BAU_CAV_1', 979: 'TU-98013', 1006: '04_CAV_BAU_1',
             1041: '05_CAV_BOJ', 1068: 'QRDP', 1095: 'RDP_CAV', 1110: 'RDP_BAU', 1149: 'ARARAQUARA', 1394: 'JGR_RDP1',
             1421: 'JGR_RDP2'}


def update_DynamoDB():
    PMU_Dict = Table('PMU_Dict', schema=[
        HashKey('PMU_Code')
    ])
    for key in dict_pmus.keys():
        PMU_Dict.put_item(data={
            'PMU_Code': str(key),
            'PMU_Name': dict_pmus[key]
        })

if __name__ == '__main__':
    update_DynamoDB()
