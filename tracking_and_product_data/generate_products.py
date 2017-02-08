#!/usr/bin/env python
import argparse
import csv
import random

TIMERANGE_BEGIN = 1483228800
TIMERANGE_LIMIT = 1485907200
PRODUCT_ID_MIN = 500000
PRODUCT_ID_MAX = 600000

SELLERS = [
  ( 100523, "Carla Columna" ),
  ( 100524, "Vicki Vale" ),
  ( 100525, "Kent Brockman" ),
  ( 100526, "Herb Welch" ),
  ( 100527, "Nicole Walker" ),
  ( 100528, "Paul Templin" ),
  ( 100529, "Brenda Starr" ),
  ( 100531, "Andrea Sachs" ),
  ( 100532, "Miranda Priestly" ),
  ( 100533, "Lou Grant" ),
  ( 100534, "Michelle Capra" ),
  ( 100535, "Ford Perfect" ),
  ( 100536, "Rita Skeeter" ),
  ( 100537, "Borat Sagdiyev" ),
  ( 100538, "Brueno Gerhard" )
]

def main():
  flag_parser = argparse.ArgumentParser()
  flag_parser.add_argument("-o", "--output", type=str, help="Output file")
  flags = flag_parser.parse_args()
  write_file(flags.output);


def generate_seller(product_id):
  return SELLERS[product_id % len(SELLERS)]


def generate_sku(product_id):
  return "MYSHOP-" + str(product_id)


def generate_category_id():
  return random.randrange(1, 10000)


def generate_rating():
  return random.random() * 5.0


def generate_cents():
  return random.randrange(299, 1000)


def generate_date():
  return random.randrange(TIMERANGE_BEGIN, TIMERANGE_LIMIT) * 1000000


def write_file(filename):
  outfile = csv.writer(open(filename, 'w'))

  # write header
  outfile.writerow([
    "id",
    "seller_id",
    "seller_name",
    "cents",
    "currency",
    "category_id",
    "created_at",
    "valid_from",
    "valid_to",
    "rating",
    "sku",
    "is_valid"
  ])

  for product_id in range(PRODUCT_ID_MIN, PRODUCT_ID_MAX):
    seller_id, seller_name = generate_seller(product_id)

    outfile.writerow([
      product_id,
      seller_id,
      seller_name,
      generate_cents(),
      "EUR",
      generate_category_id(),
      generate_date(),
      generate_date(),
      generate_date(),
      generate_rating(),
      generate_sku(product_id),
      "true"
    ])


main();
