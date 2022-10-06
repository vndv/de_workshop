#### Выполнение команд
 
  1. Сборка образа (повторно выполняется только в случае изменения Dockerfile):
     ```shell
     docker-compose build
     ```

 2. Инициализация БД и шедулера
    ```shell
    docker-compose up airflow-init
    ```

 3. Поднимаем все сервисы:
    ```shell
    docker-compose up
    ```

 4. Веб интерфейс `localhost:8080` логин/пароль: `airflow/airflow`
 

Остановка контейнеров:
    
    ```
    docker-compose down
    ```