import itertools
import os, django, decimal
import random

from django.utils import timezone
from django.db.utils import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electronic_shop.settings")
django.setup()

from django.db.models.functions.text import Ord

from ProductApp.products import (
    phones,
    monitors,
    laptops,
    pcs,
    accesories,
    ssds,
    graphs,
    rams,
    pendrives,
    switches,
    motherboards,
    cpus,
    tvs,
    headphones,
    routers,
)
from django.core.files import File
from ProductApp.models import *
from ProductApp.products import *
from Articles.models import ArticleComment
from ShoppingCardApp.models import *


products = [
    phones,
    monitors,
    laptops,
    pcs,
    accesories,
    ssds,
    graphs,
    rams,
    pendrives,
    switches,
    motherboards,
    cpus,
    tvs,
    headphones,
    routers,
]
folders = [
    "phones",
    "monitors",
    "laptops",
    "pcs",
    "accesories",
    "ssds",
    "graphs",
    "rams",
    "pendrives",
    "switches",
    "motherboards",
    "cpus",
    "tvs",
    "headphones",
    "routers",
]


model = {
    "phones": lambda **item: Phones.objects.get_or_create(**item),
    "monitors": lambda **item: Monitors.objects.get_or_create(**item),
    "laptops": lambda **item: Laptops.objects.get_or_create(**item),
    "pcs": lambda **item: Pc.objects.get_or_create(**item),
    "accesories": lambda **item: AccesoriesForLaptops.objects.get_or_create(**item),
    "ssds": lambda **item: Ssd.objects.get_or_create(**item),
    "graphs": lambda **item: Graphs.objects.get_or_create(**item),
    "rams": lambda **item: Ram.objects.get_or_create(**item),
    "pendrives": lambda **item: Pendrives.objects.get_or_create(**item),
    "switches": lambda **item: Switches.objects.get_or_create(**item),
    "motherboards": lambda **item: Motherboard.objects.get_or_create(**item),
    "cpus": lambda **item: Cpu.objects.get_or_create(**item),
    "tvs": lambda **item: Tv.objects.get_or_create(**item),
    "headphones": lambda **item: Headphones.objects.get_or_create(**item),
    "routers": lambda **item: Routers.objects.get_or_create(**item),
}


""" Add products to daabase """

for prod, folder in zip(products, folders):
    for product, fold in zip(prod, itertools.repeat(folder)):
        PATH = rf"electronic_shop/static/images/products/{fold}/"
        try:
            itt, _ = model[fold](**product)
        except IntegrityError:
            pass

        try:
            itt.main_photo.save(
                product["main_photo"], File(open(PATH + product["main_photo"], "rb"))
            )
        except:
            pass

        try:
            itt.second_photo.save(
                product["second_photo"],
                File(open(PATH + product["second_photo"], "rb")),
            )
        except:
            pass
        try:
            itt.third_photo.save(
                product["third_photo"], File(open(PATH + product["third_photo"], "rb"))
            )
        except:
            pass


""" Choose random products and change "product of the day" field. Adding promotion """
products = list(MainProductDatabase.objects.all())

# Reset field
for product in products:
    product.selected = False
    product.save()

selected = [products[random.randint(0, len(products) - 1)] for _ in range(0, 8)]

# Add selected and change price
for product in selected:
    product.selected = True
    product.promotion = product.price * round(decimal.Decimal(0.7), 2)
    product.save()


""" Choose one product as a product of the day """
product_of_the_day = products[random.randint(0, len(products) - 1)]

product_of_the_day.promotion = product_of_the_day.price * round(decimal.Decimal(0.6), 2)
product_of_the_day.product_of_the_day = True
product_of_the_day.product_of_the_day_added = timezone.now()
product_of_the_day.save()


""" Add 3 blog posts """

from Articles.models import LandingPageArticles
from django.contrib.auth import get_user_model


user, created = get_user_model().objects.get_or_create(email="employee@account.com")

if created:
    user.set_password("employee")
    user.save()

article = LandingPageArticles.objects.create(
    title="The standard Lorem Ipsum passage, used since the 1500s",
    tag_one="Phones",
    tag_two="Laptops",
    tag_three="Smartphones",
    alt_short_descript="The standard Lorem Ipsum passage, used since the 1500s",
    posted=timezone.now(),
    owner=user,
    content_wysiwyg="Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    short_description="The standard Lorem Ipsum passage, used since the 1500s",
)

article.img.save(
    "dqwd.png",
    File(open(r"electronic_shop/static/images/showcase/low res/dqwd.png", "rb")),
)

"""Comment section"""

first_comment = ArticleComment.objects.create(
    article=article,
    comment="Gdzie jest slonko kiedy spi?",
    email="test@gmail.com",
    name="Test Testowy",
    checked=True,
)

first_comment_answer = ArticleComment.objects.create(
    article=article,
    comment="Dokąd w nocy tupta jeż?",
    email="test@gmail.com",
    name="Test Testowy",
    checked=True,
    parent=first_comment,
)

first_comment_answer_child = ArticleComment.objects.create(
    article=article,
    comment="Avada Kedavra",
    email="test@gmail.com",
    name="Voldemort",
    checked=True,
    parent=first_comment_answer,
)

first_comment_answer_child = ArticleComment.objects.create(
    article=article,
    comment="Auuuu",
    email="test@gmail.com",
    name="101 Dalmatians",
    checked=True,
    parent=first_comment,
)

first_comment_answer_child = ArticleComment.objects.create(
    article=article,
    comment="Stay in wonderland",
    email="test@gmail.com",
    name="Morfeusz",
    checked=True,
    parent=first_comment_answer,
)

article = LandingPageArticles.objects.create(
    title="The standard Lorem Ipsum passage, used since the 1500s",
    tag_one="TV",
    tag_two="SSD",
    tag_three="Pendrives",
    alt_short_descript="The standard Lorem Ipsum passage, used since the 1500s",
    posted=timezone.now(),
    owner=user,
    content_wysiwyg="Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    short_description="The standard Lorem Ipsum passage, used since the 1500s",
)

article.img.save(
    "koparka.jpg",
    File(open(r"electronic_shop/static/images/showcase/low res/koparka.jpg", "rb")),
)


"""Comment section"""

first_comment = ArticleComment.objects.create(
    article=article,
    comment="Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    email="test@gmail.com",
    name="Where does it come from?",
    checked=True,
)

first_comment_answer = ArticleComment.objects.create(
    article=article,
    comment="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
    email="test@gmail.com",
    name="H. Rackham",
    checked=True,
    parent=first_comment,
)

first_comment_answer_child = ArticleComment.objects.create(
    article=article,
    comment="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras quam velit, ultrices eget consequat at, molestie ut diam. Nunc ultricies massa eget nunc dapibus congue. In molestie orci at risus rutrum, vel scelerisque sapien malesuada. Aliquam vitae ullamcorper elit, et consequat nisi. Cras sed pharetra dui, eget blandit odio. Etiam in commodo lacus. In congue nisi mauris, eu hendrerit elit auctor sit amet. Donec tincidunt tellus ac neque iaculis, sed interdum dui gravida.",
    email="test@gmail.com",
    name="Lorem Ipsum",
    checked=True,
    parent=first_comment_answer,
)

first_comment_answer_child = ArticleComment.objects.create(
    article=article,
    comment="Pellentesque vitae lobortis quam, eu lobortis enim. Donec eget nisl lacinia, dapibus libero id, bibendum tellus. Quisque gravida dolor et purus elementum tempus.",
    email="test@gmail.com",
    name="Neque porro quisquam ",
    checked=True,
    parent=first_comment,
)

first_comment_answer_child = ArticleComment.objects.create(
    article=article,
    comment="Aliquam maximus tincidunt magna, vitae luctus tortor finibus eu. Sed ac massa turpis. Aliquam tristique sit amet dolor sed facilisis. Suspendisse commodo nunc sit amet scelerisque porta",
    email="test@gmail.com",
    name="Ut est justo",
    checked=True,
    parent=first_comment_answer,
)

first_comment = ArticleComment.objects.create(
    article=article,
    comment="Vivamus quis maximus diam, at pulvinar mauris. Aliquam ante orci, ornare eget elit maximus, commodo hendrerit nulla. Maecenas faucibus nisi sapien, vel maximus turpis luctus a.",
    email="test@gmail.com",
    name="Aliquam ante orci",
    checked=True,
)


article = LandingPageArticles.objects.create(
    title="The standard Lorem Ipsum passage, used since the 1500s",
    tag_one="TV",
    tag_two="PC",
    tag_three="Pendrives",
    alt_short_descript="The standard Lorem Ipsum passage, used since the 1500s",
    posted=timezone.now(),
    owner=user,
    content_wysiwyg="Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.",
    short_description="The standard Lorem Ipsum passage, used since the 1500s",
)

article.img.save(
    "pc2.jpg",
    File(open(r"electronic_shop/static/images/showcase/low res/pc2.jpg", "rb")),
)


""" buy some products for employee account """


customer, created = Customer.objects.get_or_create(user=user)

for _ in range(1, 10):

    order = Order.objects.create(
        customer=customer,
        transaction_id="",
        transaction_status=True,
        transaction_finished=timezone.now(),
    )

    for _ in range(1, 5):
        product_item = products[random.randint(0, len(products) - 1)]

        order_item = OrderItem.objects.create(
            order=order, quantity=random.randint(1, 10), product=product_item
        )

        try:
            review, created = Reviews.objects.get_or_create(
                product=order_item.product,
                review="Vivamus quis maximus diam, at pulvinar mauris. Aliquam ante orci, ornare eget elit maximus, commodo hendrerit nulla. Maecenas faucibus nisi sapien, vel maximus turpis luctus a.",
                user=user,
                stars=random.randint(1, 6),
                checked_by_employer=True,
            )
        except IntegrityError:
            pass

        if created:
            review = created

        question = (
            Questions.objects.create(
                product=order_item.product,
                question="Gdzie jest słońce kiedy spi?",
                name="Janko Muzykant",
                checked_by_employer=True,
                employer_reply="A dokąd w nocy tupta jeż?",
            ),
        )

        question = Questions.objects.create(
            product=order_item.product,
            question="Mr. Anderson, welcome back, we miss you",
            name="Smith",
            checked_by_employer=True,
            employer_reply="Im leaving right now.",
        )

""" create likes """

for _ in range(1, 50):
    product_like = products[random.randint(0, len(products) - 1)].likes
    product_like.add(user)
