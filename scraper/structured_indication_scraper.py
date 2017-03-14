"""
Extracts structured indicators from
Drug bank
Example usage
dbe = DrugBankExtractor()
df = pd.read_csv('/Users/edwardcannon/Desktop/DrugBankIds.csv')
print(dbe.extract_structured_indications('DB00624'))
for index, row in df.iterrows():
        print(dbe.extract_structured_indications(row['Ids']))

"""
import requests
import pandas as pd

__author__ = 'edwardcannon'



class DrugBankExtractor(object):
    """
    Container for Drug Bank Extraction
    """
    start = '<span class="glyphicon glyphicon-info-sign"> </span></a></th><td><ul><li>'
    end = '<th>Pharmacodynamics'
    base_url = 'https://www.drugbank.ca/drugs/'

    def __init__(self):
        pass

    def extract_structured_indications(self, drug_id):
        html = requests.get(self.base_url+drug_id).text
        start_pt = html.find(self.start)
        end_pt = html.find(self.end)
        subset = html[start_pt:end_pt].split('</a>')
        structured_indications = []
        for val in subset:
            if "/indications" in val:
                structured_indication = val.split('">')[1]
                structured_indications.append(structured_indication)
        return drug_id, structured_indications

if __name__ == '__main__':
    pass

