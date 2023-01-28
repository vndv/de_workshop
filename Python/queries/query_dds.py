shipping_dim = '''
SELECT cityHash64(Ship_Mode) AS ship_id,
       Ship_Mode
       FROM (SELECT DISTINCT Ship_Mode FROM SAE.orders);
'''

customer_dim = '''
SELECT cityHash64(Customer_ID) AS cust_id,
       Customer_ID,
       Customer_Name
       FROM (SELECT DISTINCT Customer_ID, Customer_Name FROM SAE.orders);
'''

geo_dim = '''
SELECT cityHash64(City,Postal_Code) AS geo_id,
       Region,
       Country,
       City,
       State,
       Postal_Code
       FROM (SELECT DISTINCT Country, City, State, Region,
       Postal_Code FROM SAE.orders);
'''

product_dim = '''
SELECT cityHash64(Product_ID,Product_Name,Segment) AS prod_id,
       Product_ID,
       Product_Name,
       Category,
       SubCategory,
       Segment
       FROM (SELECT DISTINCT Product_ID, Product_Name, Category, SubCategory, Segment FROM SAE.orders);
'''

sales_fact = '''
SELECT
      cityHash64(Order_ID) 
     ,cityHash64(Customer_ID)
     ,Order_Date
     ,Ship_Date
     ,cityHash64(Product_ID,Product_Name,Segment)
     ,cityHash64(Ship_Mode)
     ,cityHash64(City,Postal_Code)
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