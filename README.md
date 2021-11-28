# Electronic Shop
Electronic shop is a e-commerce website where users can buy products, create an account, write reviews and asking for questions.

## How to configure the app
1. Its a python based application, so you have to install python on your pc: [download python](https://www.python.org/downloads/)
2. Download the app or just clone it from reposiotory
3. Enable virtual enviroment using command: `env\Scripts\activate.bat`
4. Install requirements.txt: `pip install -r requirements.txt`
5. Install database on your pc and choose it as a backend in settings.py. This procject use Postgresql, so here is an example taken from Django documentation:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': os.getenv('DB_NAME'),
                    'USER': os.getenv('DB_USER'),
                    'PASSWORD': os.getenv('DB_PASSWORD'),
                    'HOST': os.getenv('DB_HOST')
                }
            }
6. Create .env file to store the database data and secret key as fallows:

        SEC_KEY=***
        DB_NAME=**
        DB_USER=**
        DB_PASSWORD=**
        DB_HOST=**
7. Generate secret key in django shell and pase it to .env file. Run the commands:

        cd electronic_shop
        manage.py shell
        from django.core.management.utils import get_random_secret_key
        get_random_secret_key()
        exit()

8. Create database tables:

        manage.py makemigrations
        manage.py migrate

### Optional
You can pass options on the bottom, but the shop will be empty (no products avaiable)

9. There is a file `ProductApp/products.py` where the products are stored. Before putting them to database, you got two options:

    a) Adding images: Create folders as fallows: `electronic_shop/static/images/products`. Inside main folder create subfolders called like in "for loop" blocks (for example "tv", "headphones"). Full pathes are in file `products.py`. Inside each folder add images which will be used with products. Call them as you want, but remeber to changes names inside each product dictionary in `products.py`. //Will be changed soon to simpler one.

    b) If there won't be images, add Try/except block before calling "photo save" methods.

10. After preparing folders and products, add them to database. To do that, you have to run comands in commented blocks in Django shell (`manage.py shell`). Here is an example:

        from django.core.files import File
        from ProductApp.models import *
        from ProductApp.products import *
        TV_PATH = r'electronic_shop/static/images/products/tv/'
        for tv in tvs:
            tvv = Tv.objects.create(**tv)
            tvv.main_photo.save(tv['main_photo'], File(open(TV_PATH + tv['main_photo'], 'rb')))
            try:
                tvv.second_photo.save(tv['second_photo'], File(open(TV_PATH + tv['second_photo'], 'rb')))
            except:
                pass
            try:
                tvv.third_photo.save(tv['third_photo'], File(open(TV_PATH + tv['third_photo'], 'rb')))
            except:
                pass

## How to run the app

1. To run the app call command: `manage.py runserver`. App will be served on [localhost](http://127.0.0.1:8000/)

## Features


## Future features:

- Simplify creating products
- Dockerise app