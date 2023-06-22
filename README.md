# File Cloud
### *__File__ __Cloud__* is a service where you can check, upload, download and delete any files what do you want.
1. Firstly, you need to download requirements
   ```python
   pip install -r requirements.txt
2. Create a ".env" file at the root of the directory with params
   ```python
   ALL SETTINGS FOR POSTGRESQL
   
   DB_USER=your postgres user
   DB_PASS=your password for user
   DB_NAME=your name of db
   DB_HOST=127.0.0.1 or localhost
   DB_PORT=5432
3. Finally, you can start the project: in main.py or by a command 
    ```
    uvicorn main:app --reload
> If you create some records to db, you can start tests
  ```python
  pytest
