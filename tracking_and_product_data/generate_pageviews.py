#!/usr/bin/env python
import argparse
import csv
import random

TIMERANGE_BEGIN = 1483228800
TIMERANGE_LIMIT = 1485907200
PRODUCT_ID_MIN = 500000
PRODUCT_ID_MAX = 600000

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
REFERRER = [
  "http://google.com",
  "http://twitter.com"
]

def main():
  flag_parser = argparse.ArgumentParser()
  flag_parser.add_argument("-o", "--output", type=str, help="Output file")
  flag_parser.add_argument("-n", "--num_rows", type=int, help="Number of rows")
  flags = flag_parser.parse_args()
  write_file(flags.output, flags.num_rows);


def generate_time():
  return random.randrange(TIMERANGE_BEGIN, TIMERANGE_LIMIT) * 1000000


def generate_sid():
  return random.randrange(30000000000, 30000006000)


def generate_request_id():
  return random.randrange(90000000000, 90006000000)


def generate_user_agent():
  return USER_AGENT


def generate_referrer():
  return REFERRER[random.randrange(0, len(REFERRER))]


def generate_product_id():
  return random.randrange(PRODUCT_ID_MIN, PRODUCT_ID_MAX)


def generate_url(product_id):
  return "/product/" + str(product_id) + "-my-fancy-product?blah"


def generate_time_on_page():
  return random.random() * 120.0


def generate_screen_width():
  return 1440


def generate_screen_height():
  return 900


def generate_is_logged_in():
  return False


def write_file(filename, nrows):
  outfile = csv.writer(open(filename, 'w'))

  # write header
  outfile.writerow([
    "time",
    "sid",
    "request_id",
    "url",
    "user_agent",
    "referrer",
    "product_id",
    "time_on_page",
    "screen_width",
    "screen_height",
    "is_logged_in",
  ])

  for i in range (0, nrows):
    product_id = generate_product_id();

    outfile.writerow([
      generate_time(),
      generate_sid(),
      generate_request_id(),
      generate_url(product_id),
      generate_user_agent(),
      generate_referrer(),
      generate_time_on_page(),
      product_id,
      generate_screen_width(),
      generate_screen_height(),
      generate_is_logged_in()
    ])

main();
