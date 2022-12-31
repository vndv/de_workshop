CREATE DATABASE IF NOT EXISTS DDS ENGINE = Atomic;

/*-----------------------------------------------*/
--- Create DDS.shipping_dim table
/*-----------------------------------------------*/

DROP TABLE IF EXISTS DDS.shipping_dim;

CREATE TABLE IF NOT EXISTS DDS.shipping_dim(
   ship_id   UInt32 NOT NULL 
  ,ship_mode String NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (ship_id)
ORDER BY ship_id;

INSERT INTO DDS.shipping_dim 
SELECT cityHash64(Ship_Mode,Row_ID) AS ship_id,
       Ship_Mode
       FROM SAE.orders
       ORDER BY ship_id;
       
SELECT * FROM DDS.shipping_dim sd;

/*-----------------------------------------------*/
--- Create DDS.customer_dim table
/*-----------------------------------------------*/

DROP TABLE IF EXISTS DDS.customer_dim ;

CREATE TABLE IF NOT EXISTS DDS.customer_dim(
   cust_id       UInt32 NOT NULL,
   customer_id   String NOT NULL,
   customer_name String NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (cust_id)
ORDER BY cust_id;

INSERT INTO DDS.customer_dim 
SELECT cityHash64(Customer_ID,Row_ID) AS cust_id,
       Customer_ID,
       Customer_Name
       FROM SAE.orders;
       
 SELECT * FROM DDS.customer_dim;

/*-----------------------------------------------*/
--- Create DDS.geo_dim table
/*-----------------------------------------------*/
 
DROP TABLE IF EXISTS DDS.geo_dim ;

CREATE TABLE IF NOT EXISTS DDS.geo_dim(
     geo_id      UInt32 NOT NULL,
     country     String NOT NULL,
     city        String NOT NULL,
     state       String NOT NULL,
     postal_code UInt32 NULL
)
ENGINE = MergeTree()
PRIMARY KEY (geo_id)
ORDER BY geo_id;
 
INSERT INTO DDS.geo_dim 
SELECT cityHash64(Postal_Code,Row_ID) AS geo_id,
       Country,
       City,
       State,
       Postal_Code
       FROM SAE.orders;
       
 SELECT * FROM DDS.geo_dim;
 
UPDATE DDS.geo_dim
SET postal_code = '05401'
WHERE city = 'Burlington'  AND postal_code = 0;

SELECT * FROM DDS.geo_dim
WHERE city = 'Burlington'

/*-----------------------------------------------*/
--- Create DDS.product_dim table
/*-----------------------------------------------*/

DROP TABLE IF EXISTS DDS.product_dim ;

CREATE TABLE IF NOT EXISTS DDS.product_dim(
     prod_id      UInt32 NOT NULL, 
     product_id   String NOT NULL,  
     product_name String NOT NULL,
     category     String NOT NULL,
     sub_category String NOT NULL,
     segment      String NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (prod_id)
ORDER BY prod_id;
   
INSERT INTO DDS.product_dim 
SELECT cityHash64(Product_ID,Row_ID) AS prod_id,
       Product_ID,
       Product_Name,
       Category,
       SubCategory,
       Segment
       FROM SAE.orders;
       
 SELECT * FROM DDS.product_dim;
 
/*-----------------------------------------------*/
--- Create DDS.sales_fact table
/*-----------------------------------------------*/
 
 
 CREATE TABLE IF NOT EXISTS DDS.sales_fact
(
 sales_id      UInt32 NOT NULL,
 cust_id       UInt32 NOT NULL,
 order_date_id UInt32 NOT NULL,
 ship_date_id  UInt32 NOT NULL,
 prod_id       UInt32 NOT NULL,
 ship_id       UInt32 NOT NULL,
 geo_id        UInt32 NOT NULL,
 order_id      String NOT NULL,
 sales         Decimal(9,4) NOT NULL,
 profit        Decimal(9,4) NOT NULL,
 quantity      UInt32 NOT NULL,
 discount      Decimal(9,4) NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (sales_id)
ORDER BY (sales_id,cust_id);


INSERT INTO DDS.sales_fact
SELECT
      cityHash64(Order_ID,Row_ID) 
     ,cityHash64(Customer_ID,Row_ID)
     ,toInt32(Order_Date)
     ,toInt32(Ship_Date)
     ,cityHash64(Product_ID,Row_ID)
     ,cityHash64(Ship_Mode,Row_ID)
     ,cityHash64(Postal_Code,Row_ID)
     ,o.Order_ID
     ,Sales
     ,Profit
     ,Quantity
     ,Discount
FROM SAE.orders;


SELECT count(*) FROM DDS.sales_fact;

 
/*-----------------------------------------------*/
--- Create DDS.calendar_dim  table
/*-----------------------------------------------*/
 
DROP TABLE IF EXISTS DDS.calendar_dim ;
CREATE TABLE DDS.calendar_dim(
    dateid      UInt32  NOT NULL,
    year        UInt32 NOT NULL,
    quarter     UInt32 NOT NULL,
    month       UInt32 NOT NULL,
    week        UInt32 NOT NULL,
    date        date NOT NULL,
    week_day    String NOT NULL,
    leap  String NOT NULL,
)

/*-----------------------------------------------*/
--- Create DDS.returns_fact  table
/*-----------------------------------------------*/

DROP TABLE IF EXISTS DDS.returns_fact ;

CREATE TABLE IF NOT EXISTS DDS.returns_fact(
   internal_id  UInt64  NOT NULL
  ,returned   String NOT NULL 
  ,order_id   String NOT NULL
)
ENGINE = MergeTree()
ORDER BY internal_id;

INSERT INTO DDS.returns_fact
SELECT 
cityHash64(Returned,Order_id) as internal_id,
Returned,
Order_id
FROM SAE.returns;

select * from DDS.returns_fact

/*-----------------------------------------------*/
   