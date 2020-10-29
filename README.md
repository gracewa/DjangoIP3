# DjangoIP3

## Author  
  
[Grace Wanene](https://github.com/gracewa)  

# Description  
This is a Django application that allows a user to post a project he/she has created and get it reviewed by his/her peers.

##  Live Link  


## Setup and Installation  
1. Clone the repository

```bash
git clone https://github.com/gracewa/DjangoIP3.git
```
2. Navigate into the project folder

3. Python3 -m venv myvenv
4. Activate virtual environment

```bash
source virtual/bin/activate 
```
4. Install requirements 
```bash 
 pip install -r requirements.txt 
```
5. python manage.py createsuperuser 
6. python manage.py makemigrations postings
7. python manage.py migrate postings
8. python manage.py run server and then go to http://localhost:8000/
