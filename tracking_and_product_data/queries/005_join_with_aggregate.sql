SELECT count(1) num_pageviews, products.seller_name
FROM pageviews, products
WHERE pageviews.product_id = products.id
GROUP BY products.seller_id
ORDER BY num_pageviews DESC;
