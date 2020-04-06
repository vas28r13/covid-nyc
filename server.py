import pandas as pd
import wget

from flask import Flask
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__, static_url_path='', static_folder='public',)
_PORT = 8080


@app.route('/')
def root():
    return app.send_static_file('index.html')


def load_data():
    scaler = MinMaxScaler()
    url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/tests-by-zcta.csv'
    wget.download(url, out='./public/data')

    tests_df = pd.read_csv('./public/data/tests-by-zcta.csv', dtype={'MODZCTA': str})
    population_df = pd.read_csv('./public/data/population.csv', dtype={'ZIP_CODE': str})

    df = tests_df.merge(population_df, left_on='MODZCTA', right_on='ZIP_CODE', how='inner')
    df['PER_THOUSAND'] = df.apply(lambda x: x['Positive']/x['POPULATION']*1000, axis=1)
    df['PER_THOUSAND_SCALED'] = scaler.fit_transform(df[['PER_THOUSAND']])
    df.to_csv('./public/data/final.csv', encoding='utf-8', index=False)


if __name__ == '__main__':
    load_data()
    app.run(host='0.0.0.0', port=_PORT)
