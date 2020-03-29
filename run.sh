#!/usr/bin/sh sh

while read p; do
    echo "python3 src/scrape.py -u=$p"
    python3 src/scrape.py -u=$p
done <data/news_urls.txt
