# About
**Project folder is `mysite/`**  
**It was done by me to get four certificates from University of Michigan about Django Framework.**
This project is about various functional apps implementing different criteries like post redirection,django frameworks generics, get and post request, implementing authentication and authorization,data modeling like one to many , many to many,Ajax implementation for loading data from server without page refresh,Json serializer and deserializer implementation, jquery and more.
It wasn't easy to complete took me some time though I could have ended it sooner.

Run in the dir where you see manage.py   
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install pipenv
pipenv install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
Close the Console Create a super user if you wish to,
```bash
python3 manage.py createsuperuser
```
The view of the project is
![project home page](/doc-images/home.png)
