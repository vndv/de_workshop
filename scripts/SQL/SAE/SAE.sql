CREATE DATABASE IF NOT EXISTS SAE ENGINE = Atomic;

CREATE TABLE IF NOT EXISTS SAE.returns(
   Returned   VARCHAR NOT NULL 
  ,Order_id   VARCHAR NOT NULL
)
ENGINE = MergeTree()
ORDER BY Order_id;


CREATE TABLE IF NOT EXISTS SAE.orders (
   Row_ID        UInt32 NOT NULL
  ,Order_ID      String NOT NULL
  ,Order_Date    Date  NOT NULL 
  ,Ship_Date     Date  NOT NULL
  ,Ship_Mode     String NOT NULL
  ,Customer_ID   String NOT NULL
  ,Customer_Name String NOT NULL
  ,Segment       String NOT NULL
  ,Country       String NOT NULL
  ,City          String NOT NULL
  ,State         String NOT NULL
  ,Postal_Code   UInt32  
  ,Region        String NOT NULL
  ,Product_ID    String NOT NULL
  ,Category      String NOT NULL
  ,SubCategory   String NOT NULL
  ,Product_Name  String NOT NULL
  ,Sales         Decimal(6,4)
  ,Quantity      UInt32
  ,Discount      Decimal(6,4)
  ,Profit        Decimal(6,4)  
)
ENGINE = MergeTree()
ORDER BY Order_Date;