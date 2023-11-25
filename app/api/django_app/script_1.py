import pymongo

# Підключення до MongoDB
client = pymongo.MongoClient("mongodb://localhost/")

# Вибір бази даних
db = client["mydatabase"]  
# Вибір колекції (таблиці)
collection = db["mycollection"]  
# Отримання всіх документів (рядків) з колекції
documents = collection.find()

# Виведення отриманих даних
for document in documents:
    print(document)

# Закриття з'єднання
client.close()