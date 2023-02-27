# Java App Project
## Evaluation app for restaurants "eeFood"
#### Requirement
**django**
pythonのフレームワーク

download    "pip install django"

cd application

python manage.py runserver

**Build up the database**

・Restaurants{name(varchar), addr(varchar), phone(varchar16), time, number of table(int)}

・Menu{RestaurantName, price, ingredient, quantity} referenced from Restaurants(name)

・Genre{RestaurantName, price(low, mid, high), genre(ex.Japanese, Chinese, Mexican, etc} referenced from Restaurants(name)

・TimeTable{RestaurantName, openTime, closeTime} referenced from Restaurants(name)

・Review{RestaurantName, Rate(1 ~ 5), Comment(Text)} referenced from Restaurants(name)

・Reservation{ResutaurantName, Table, UserName, ReservedTime} referenced from Restaurants(name, number of table)

**phonenumber fileldのエラー**
1. pip install django-phonenumber-field
2. pip install django-phonenumbers

**テーブルの作るコマンド**
1. python manage.py migrate
2. python manage.py makemigrations applicatio

