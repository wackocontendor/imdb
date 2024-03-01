import requests
import gzip
import io
import pandas as pd
import os

url_prefix = "https://datasets.imdbws.com/"

def extract_tsv(url):
    response = requests.get(url)
    gzipped_content = response.content
    return gzip.decompress(gzipped_content).decode('utf-8')

def create_dataframe(content):
    return pd.read_csv(io.StringIO(content), sep='\t', dtype=str)

def extract_and_load(suffix):
    url = url_prefix + suffix
    tsv_content = extract_tsv(url)
    return create_dataframe(tsv_content)

def export_to_csv(df):
    outname = 'test.csv'
    outdir = './output'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fullname = os.path.join(outdir, outname)    
    return df.to_csv(fullname, index=False)

# title_akas = extract_and_load("title.akas.tsv.gz")
# title_basics = extract_and_load("title.basics.tsv.gz")
# title_crew = extract_and_load("title.crew.tsv.gz")
# title_episodes = extract_and_load("title.episode.tsv.gz")
# title_principals = extract_and_load("title.principals.tsv.gz")
title_ratings = extract_and_load("title.ratings.tsv.gz")
# name_basics = extract_and_load("name.basics.tsv.gz")

export_to_csv(title_ratings)
