# -*- coding: utf-8 -*-
__title__ = 'coviewed_web_scraping'
__author__ = 'Dietrich Trautmann'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020, Dietrich Trautmann'

import hashlib 
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
            help="provide an alternative name for the ouput_file",
            type=str
            )
    parser.add_argument(
            "-v",
            "--verbose",
            help="shows output",
            type=bool
            )
    args = parser.parse_args()

    if args.output_file:
        output_file = args.output_file
    else:
        output_file = hashlib.md5(args.url.encode()).hexdigest() + '.txt'

    article = Article(args.url)
    article.download()
    article.parse()
    
    with open(output_file, "w") as f:
        f.writelines(args.url)
        f.writelines("\n\n")
        f.writelines(article.title)
        f.writelines("\n\n")
        f.writelines(article.text)

    if args.verbose:
        print(output_file)
        print(args.url)
        print(args.output_file)
        print(article.title)
        print(article.text)
    
