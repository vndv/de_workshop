shipping_dim = '''
SELECT cityHash64(Ship_Mode,Row_ID) AS ship_id,
       Ship_Mode
       FROM SAE.orders
       ORDER BY ship_id;
'''

customer_dim = '''
SELECT cityHash64(Customer_ID,Row_ID) AS cust_id,
       Customer_ID,
       Customer_Name
       FROM SAE.orders;
'''

geo_dim = '''
SELECT cityHash64(Postal_Code,Row_ID) AS geo_id,
       Country,
       City,
       State,
       Postal_Code
       FROM SAE.orders;
'''

product_dim = '''
SELECT cityHash64(Product_ID,Row_ID) AS prod_id,
       Product_ID,
       Product_Name,
       Category,
       SubCategory,
       Segment
       FROM SAE.orders;
'''

sales_fact = '''
SELECT
      cityHash64(Order_ID,Row_ID) 
     ,cityHash64(Customer_ID,Row_ID)
     ,toInt64(Order_Date)
     ,toInt64(Ship_Date)
     ,cityHash64(Product_ID,Row_ID)
     ,cityHash64(Ship_Mode,Row_ID)
     ,cityHash64(Postal_Code,Row_ID)
     ,Order_ID
     ,Sales
     ,Profit
     ,Quantity
     ,Discount
FROM SAE.orders;
'''

returns_fact = '''
SELECT 
cityHash64(Returned,Order_id) as internal_id,
Returned,
Order_id
FROM SAE.returns;
'''