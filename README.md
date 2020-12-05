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
## Ads App
![Ads](/doc-images/ah1.png)
![Ads](/doc-images/ah2.png)
Here users can post adds but one user can not edit or delete other users adds but comment in it.
![](/doc-images/g1.png)
![](/doc-images/g2.png)
The view of running script to load scattered data from [unesco world heritage site csv file](https://raw.githubusercontent.com/19mddil/Different-functional-Django-App-Source-Codes/main/unesco/load.csv)
![view of script run](/doc-images/sr.png)
And more... Run to see :).
