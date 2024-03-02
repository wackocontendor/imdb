import requests
import gzip
import io
import pandas as pd
import os

url_prefix = "https://datasets.imdbws.com/"

def extract_load_tsv(suffix):
    url = url_prefix + suffix
    response = requests.get(url)
    gzipped_content = response.content
    extracted_tsv = gzip.decompress(gzipped_content).decode('utf-8')
    return pd.read_csv(io.StringIO(extracted_tsv), sep='\t', dtype=str)

def export_to_csv(df):
    outname = 'test.csv'
    outdir = './output'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fullname = os.path.join(outdir, outname)    
    return df.to_csv(fullname, index=False)

# title_akas = extract_load_tsv("title.akas.tsv.gz")
# title_basics = extract_load_tsv("title.basics.tsv.gz")
# title_crew = extract_load_tsv("title.crew.tsv.gz")
# title_episodes = extract_load_tsv("title.episode.tsv.gz")
# title_principals = extract_load_tsv("title.principals.tsv.gz")
title_ratings = extract_load_tsv("title.ratings.tsv.gz")
# name_basics = extract_load_tsv("name.basics.tsv.gz")

export_to_csv(title_ratings)