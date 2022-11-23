from faker import Faker
from faker_biology.physiology import CellType
import pandas as pd
import random
import argparse

# initialite parser
parser = argparse.ArgumentParser()

parser.add_argument("-SALESMAN_ROWS", "--Output", help = "Show Output")

args = parser.parse_args()

# initiate a faker instance
fake = Faker()
fake.add_provider(CellType)

def main(SALESMAN_ROWS = 100, PRODUCT_ROWS = 500, MANUFACTURER_ROWS = 40, FACT_ROWS = 5000, LAST_YEARS = 5):
    salesman_ids = [x for x in range(0, SALESMAN_ROWS)]
    product_ids = [x for x in range(0, PRODUCT_ROWS)]
    manufacturer_ids = [x for x in range(0, MANUFACTURER_ROWS)]
    fact_ids = [x for x in range(0, FACT_ROWS)]

    df_salesman = pd.DataFrame.from_dict(
        data=
            {
            'salesman_id': salesman_ids,
            'first_name': [fake.first_name() for x in salesman_ids],
            'last_name': [fake.last_name() for x in salesman_ids],
            'city': [fake.city() for x in salesman_ids],
            'country': "US",
            'state': [fake.address().split(' ')[-2] for x in salesman_ids],
            'ssn': [fake.ssn() for x in salesman_ids],
            }
    )

    df_product = pd.DataFrame.from_dict(
        data=
            {
            'product_id': product_ids,
            'barcode': [fake.ean() for x in product_ids],
            'colour': [fake.safe_color_name() for x in product_ids],
            'target_cell': [fake.celltype() for x in product_ids],
            'manufacturer_id': [random.randint(0, MANUFACTURER_ROWS) for x in product_ids]
            }
    )

    df_manufacturer = pd.DataFrame.from_dict(
        data=
            {
            'manufacturer_id': manufacturer_ids,
            'name': [fake.unique.company() for x in manufacturer_ids],
            'coordinates': [fake.unique.location_on_land(coords_only = True) for x in manufacturer_ids],
            }
    )

    df_facts = pd.DataFrame.from_dict(
        data=
            {
            'id': fact_ids,
            'product_id': [random.randint(0, MANUFACTURER_ROWS) for x in fact_ids],
            'salesman_id': [random.randint(0, SALESMAN_ROWS) for x in fact_ids],
            'date': [fake.date_between(start_date=f'-{LAST_YEARS}y') for x in fact_ids],
            'net_sale_value': [fake.pricetag().replace('$', '') for x in fact_ids],
            }
    )

    counter = 0
    for df in [df_salesman, df_product, df_manufacturer, df_facts]:
        df.to_csv(f'{counter}.csv')
        counter += 1
    return None