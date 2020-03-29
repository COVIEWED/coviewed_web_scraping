# -*- coding: utf-8 -*-
__title__ = 'coviewed_web_scraping'
__author__ = 'Dietrich Trautmann'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020, Dietrich Trautmann'

import argparse
from newspaper import Article

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-u",
            "--url",
            help="please provide a web url to scrape",
            required=True,
            type=str
            )
    parser.add_argument(
            "-o",
            "--output_file",
            help="please provide name for the ouput_file",
            required=True,
            type=str
            )
    parser.add_argument(
            "-v",
            "--verbose",
            help="shows output",
            type=bool
            )
    args = parser.parse_args()
    
    article = Article(args.url)
    article.download()
    article.parse()
    
    with open(args.output_file, "w") as f:
        f.writelines(article.title)
        f.writelines("\n\n")
        f.writelines(article.text)

    if args.verbose:
        print(args.url)
        print(args.output_file)
        print(article.title)
        print(article.text)
    
