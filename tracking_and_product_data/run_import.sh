#!/bin/bash -x

./generate_pageviews.py -o data/pageviews.csv -n 1000000
./generate_products.py -o data/products.csv

evql -d test -e 'DROP TABLE pageviews;'
evql -d test -f tables/pageviews.sql

evql -d test -e 'DROP TABLE products;'
evql -d test -f tables/products.sql

evqlctl table-import --host localhost --port 9175 --database test --table pageviews --format csv --file data/pageviews.csv
evqlctl table-import --host localhost --port 9175 --database test --table products --format csv --file data/products.csv
