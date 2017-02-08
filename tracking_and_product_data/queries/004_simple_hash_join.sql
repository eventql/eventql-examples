SELECT pageviews.time, pageviews.url, pageviews.product_id, products.seller_id, products.seller_name
FROM pageviews
JOIN products ON pageviews.product_id = products.id
LIMIT 10;
