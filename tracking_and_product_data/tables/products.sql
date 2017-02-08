CREATE TABLE products (
  `id` uint64,
  `seller_id` uint64,
  `seller_name` string,
  `cents` double,
  `currency` string,
  `category_id` uint64,
  `created_at` datetime,
  `valid_from` datetime,
  `valid_to` datetime,
  `rating` double,
  `sku` string,
  `is_valid` bool,
  PRIMARY KEY (id),
) WITH
  write_consistency_level = "RELAXED";
