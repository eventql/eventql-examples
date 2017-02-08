### Step 0: Start EventQL

    $ evqld --datadir /srv/evql/standalone --standalone --listen localhost:9175


### Step 1: Generate fake tracking and products data

    $ ./generate_pageviews.py -o data/pageviews.csv -n 1000000
    $ ./generate_products.py -o products_data.csv -n 500000


### Step 2: Create Tables in EventQL

    $ evql -d test -f tables/pageviews.sql
    $ evql -d test -f tables/products.sql


### Step 3: Import data

    $ evqlctl table-import --host localhost --port 9175 --database test --table pageviews --format csv --file data/pageviews.csv
