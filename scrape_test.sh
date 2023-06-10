#!/bin/bash
set -euxo pipefail
cd ./scraper
scrapy crawl laptops -a links_file=../datasets/test_links.txt
python ./jsonl_to_csv.py -i ./data.jsonl -o ../datasets/test_data.csv
rm ./data.jsonl