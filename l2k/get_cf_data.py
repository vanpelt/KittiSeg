import pandas as pd
import click
import json

import urllib

def download_data(cf_csv):
    df = pd.read_csv(cf_csv)

    annotation = [json.loads(a) for a in df['annotation']]
    gt_urls = [a['url'] for a in annotation] # so pythonic...
    for i, url in enumerate(gt_urls):
        urllib.urlretrieve (url, str(i)+"_gt.png")

    image_url = [json.loads(a) for a in df['url']]
    for i, url in enumerate(image_urls):
        urllib.urlretrieve (url, str(i)+".png")

@click.command()
@click.argument('cf-csv', type=click.Path(exists=True))
def get_data(cf_csv):
    download_data(cf_csv)




if __name__ == '__main__':
    get_data()
