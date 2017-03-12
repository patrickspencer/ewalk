import csv
from stockwalk.models import Company, dbsession
from os.path import abspath, dirname, join

data_dir = abspath(join(dirname(__file__), '..', '..', 'data'))
s_and_p_file = join(data_dir, 's_and_p.csv')

def add_company_to_dbsession(company):
    """
    :params company: a dict with keys Symbol, Name, Sector for each company
        in the s&p 500 data file
    """
    if not Company.exists(company['Symbol']):
        dbsession.add(Company(
            symbol=company['Symbol'],
            name=company['Name'],
            sector=company['Sector'],
        ))

l = []
with open(s_and_p_file, newline='') as csvfile:
    companies = csv.DictReader(csvfile, delimiter=',', quotechar='\"')
    for company in companies:
        add_company_to_dbsession(company)

dbsession.commit()
q = dbsession.query(Company).all()
print(q)
