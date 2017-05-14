import pandas as pd
import click

@click.command()
@click.argument('cf-csv', type=click.Path(exists=True))
def get_data(cf_csv):
    df = pd.read_csv(cf_csv)
    print(df)

if __name__ == '__main__':
    get_data()
