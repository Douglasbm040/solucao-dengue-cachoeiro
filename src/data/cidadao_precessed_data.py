from bs4 import BeautifulSoup
import pandas as pd

def processar_cidadao_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find('table', {'class': 'table table-striped table-hover'})
    rows = tables.find_all('tr')
    
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
 
    dataset={}
    
    for d in data:
        dataset[d[0]] = d[1]
          
    return dataset


