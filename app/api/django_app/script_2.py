import pymongo
from my_django_app.models import models   

# Підключення до MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost/")
mongo_db = mongo_client["database"]  
mongo_collection = mongo_db["mycollection"]

# Запит до MongoDB для отримання даних
mongodb_data = mongo_collection.find({})

# Перенесення даних в PostgreSQL з використанням транзакцій
with transaction.atomic():
    for item in mongodb_data:
        django_instance = models(
            field1=item["mongodb_field1"],
            field2=item["mongodb_field2"]
        )
        django_instance.save()

print("Дані було успішно перенесено в PostgreSQL.")