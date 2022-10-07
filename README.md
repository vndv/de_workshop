# Data Engineering workshop

## Цели воркшопа
   
   Репозиторий создан для начинающих разработчиков с целью показать процесс ETL
   и потренироваться на реальных данных

    Изначально у нас есть датасет superstore.xls
    В нем находятся данные:
    * по заказам - orders
    * по возвратам - returns
    * по менеджерам - people

    Предпологается, что данные будут находится на разных источниках.
    * orders - PostgreSQL
    * returns - MySQL
    * people - предпологаем, что это данные из CRM и они храняться в CSV/XLS


    Хранилище планируется реализовать на ClickHouse
    В хранилище затягиваем данные из источников -> Extract
    cоздаем схему StarScheme/Snowflake 
    Необходимо написать скрипты для извлечения данных из источников и загрузки в хранилище
    либо воспользоваться любым ETL инструментом Pentaho/Talend/NiFi

  Вводная статья, о том как писать пйплайны на 
  [Python](https://knowtechie.com/how-to-build-etl-pipelines-in-python/)

    Отвечаем на вопросы:

    1. Overview (обзор ключевых метрик)
        - Total Sales
        - Total Profit
        - Profit Ratio
        - Profit per Order
        - Sales per Customer
        - Avg. Discount
        - Monthly Sales by Segment ( табличка и график)
        - Monthly Sales by Product Category (табличка и график)

    2. Product Dashboard (Продуктовые метрики)
        - Sales by Product Category over time (Продажи по категориям)

    3. Customer Analysis
        - Sales and Profit by Customer
        - Customer Ranking
        - Sales per region

    Делаем дашборды в Metabase
    Почему Metabese - он бесплатный и очень легкий
    (можете выбрать любой на свой вкус, но в контейнере подниматься будет он)


## Подключение к контейнерам

  - Postgre
    - Host: localhost
    - Port: 5432
    - Database: orders
    - Username: admin
    - Password: admin

  - MySQL
    - Host: localhost
    - Port: 3306
    - Database: returns
    - Username: admin
    - Password: admin 

  - Clickhouse
    - Host: localhost
    - Port: 8123
    - Database: пустое поле
    - Username: default
    - Password: пустое поле

  - Metabase
    Переходим в браузер и вводим localhost:3000
    Выбираем в подключение Clickhouse

    смотрим адрес для Clickhouse
    docker network ls 
    
    находим de_workshop_etl_host

    docker network inspect de_workshop_etl_host

    находим контейнер de_workshop_clickhouse_1 и копируем IPv4Address

  - Google sheet
    таблица с данными по менеджерам
    https://docs.google.com/spreadsheets/d/1NKb_sdrg1aRvPw2DnWLVMXF7lFIR7vc5p-xWiCr8Mww/edit?usp=sharing


## Завершение работы
   docker-compose stop - остановить все контейнеры и сохранить данные
   docker-compose down - удалить все контейнеры

**[Видеоинструкция часть 1](https://youtu.be/GQI7TnlgdRY)**

**[Видеоинструкция часть 2](https://youtu.be/zdc3tvLVOvs)**

**[Видеоинструкция часть 3](https://youtu.be/hGaKychQXMc)**


