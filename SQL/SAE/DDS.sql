CREATE DATABASE IF NOT EXISTS DDS ENGINE = Atomic;

/*-----------------------------------------------*/
--- Create DDS.shipping_dim table
/*-----------------------------------------------*/

CREATE TABLE IF NOT EXISTS DDS.shipping_dim(
   ship_id   UInt64 NOT NULL 
  ,ship_mode String NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (ship_id)
ORDER BY ship_id;

/*-----------------------------------------------*/
--- Create DDS.customer_dim table
/*-----------------------------------------------*/

CREATE TABLE IF NOT EXISTS DDS.customer_dim(
   cust_id       UInt64 NOT NULL,
   customer_id   String NOT NULL,
   customer_name String NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (cust_id)
ORDER BY cust_id;

/*-----------------------------------------------*/
--- Create DDS.geo_dim table
/*-----------------------------------------------*/
 
CREATE TABLE IF NOT EXISTS DDS.geo_dim(
     geo_id      UInt64 NOT NULL,
     country     String NOT NULL,
     city        String NOT NULL,
     state       String NOT NULL,
     postal_code UInt32 NULL
)
ENGINE = MergeTree()
PRIMARY KEY (geo_id)
ORDER BY geo_id;
 
/*-----------------------------------------------*/
--- Create DDS.product_dim table
/*-----------------------------------------------*/

DROP TABLE IF EXISTS DDS.product_dim ;

CREATE TABLE IF NOT EXISTS DDS.product_dim(
     prod_id      UInt64 NOT NULL, 
     product_id   String NOT NULL,  
     product_name String NOT NULL,
     category     String NOT NULL,
     sub_category String NOT NULL,
     segment      String NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (prod_id)
ORDER BY prod_id;
   
/*-----------------------------------------------*/
--- Create DDS.sales_fact table
/*-----------------------------------------------*/
 
 
 CREATE TABLE IF NOT EXISTS DDS.sales_fact
(
 sales_id      UInt64 NOT NULL,
 cust_id       UInt64 NOT NULL,
 order_date    Date NOT NULL,
 ship_date     Date NOT NULL,
 prod_id       UInt64 NOT NULL,
 ship_id       UInt64 NOT NULL,
 geo_id        UInt64 NOT NULL,
 order_id      String NOT NULL,
 sales         Decimal(9,4) NOT NULL,
 profit        Decimal(9,4) NOT NULL,
 quantity      UInt64 NOT NULL,
 discount      Decimal(9,4) NOT NULL
)
ENGINE = MergeTree()
PRIMARY KEY (sales_id)
ORDER BY (sales_id,cust_id);

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

/*-----------------------------------------------*/
   