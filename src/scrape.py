# -*- coding: utf-8 -*-
__title__ = "coviewed_web_scraping with newspaper lib"
__author__ = "Dietrich Trautmann"
__license__ = "MIT"
__copyright__ = "Copyright 2020, Dietrich Trautmann"

import os
import hashlib
import argparse
import requests
from selenium import webdriver
from newspaper import Article
from newspaper.article import ArticleException


def parse_article(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError("URL not found: %s" % url)
    article = Article(url)
    try:
        article.download()
        article.parse()
    except:
        driver = webdriver.Chrome()
        driver.get(url)
        article.download(input_html=driver.page_source)
        article.parse()
        driver.close()
    return article


def write_output(article, output_file, verbose=False):
    if output_file is None:
        output_file = hashlib.md5(args.url.encode()).hexdigest() + ".txt"
        output_file = os.path.join("data", output_file)

    with open(output_file, "w") as f:
        f.writelines(args.url)
        f.writelines("\n\n")
        f.writelines(str(article.publish_date))
        f.writelines("\n\n")
        f.writelines(article.title)
        f.writelines("\n\n")
        f.writelines(article.text)

    if verbose:
        print(output_file)
        print(args.url)
        print(article.title)
        print(article.text)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--url",
        help="please provide a web url to scrape",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output_file",
        help="provide an alternative name for the ouput_file",
        type=str,
    )
    parser.add_argument("-v", "--verbose", help="shows output", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    article = parse_article(args.url)
    write_output(article, args.output_file, args.verbose)
