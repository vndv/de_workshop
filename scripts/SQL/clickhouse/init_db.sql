CREATE DATABASE IF NOT EXISTS superstore ENGINE = Atomic;


CREATE TABLE IF NOT EXISTS superstore.orders (
   Row_ID        UInt32 
  ,Order_ID      String
  ,Order_Date    String  
  ,Ship_Date     String  
  ,Ship_Mode     String
  ,Customer_ID   String
  ,Customer_Name String
  ,Segment       String
  ,Country       String
  ,City          String
  ,State         String
  ,Postal_Code   Int32 
  ,Region        String
  ,Product_ID    String
  ,Category      String
  ,SubCategory   String
  ,Product_Name  String
  ,Sales         Float32
  ,Quantity      Int32
  ,Discount      Float32
  ,Profit        Float32 
)
ENGINE = MergeTree()
ORDER BY Order_Date;