### Description

This is an unfinished webscraping project deployed with Django. You can list the name, price, link of products and make quick compaarison from a website

#### Set up

first you need download the files, and then install django, and dependencies (beautifulsopu etc.) Your main functions are in utils.py, wiev.py is just doing the request

#### Running

you just come to correct directory (in the first mscraper folder)

on terminal python manage.py runserver

(if you made changes on models.py, first you need to make migrations like: python manage.py makemigrations and then apply them as python manage.py migrate)

Note that this is working only for specified url in base_url (you can find it in utils.py and change it.. eventually you got to change the function according to the html structure of new website)
