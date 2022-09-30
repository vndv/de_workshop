my_sql_extract = """
                     SELECT Returned, 
                            Order_id
                       FROM returns;

                 """

pg_extract = """
                 SELECT
                    row_id,
                    order_id,
                    order_date,
                    ship_date,
                    ship_mode,
                    customer_id,
                    customer_name,
                    segment,
                    country,
                    city,
                    state,
                    postal_code,
                    region,
                    product_id,
                    category,
                    subcategory,
                    product_name,
                    sales,
                    quantity,
                    discount,
                    profit
                FROM
                    orders;

              """