Create a virtual environment in a directory in VS Code with the code {for windows): 
python -m venv myenv  

Activate it using the command: 
myenv\Scripts\activate

Then create a django project using the command: 
django-admin startproject proj

Then insert the folders proj and app inside it.
If it doesn't work, try by creating a django app using the command: 
python manage.py startapp app

After putting all the files run migrations using: 
python manage.py makemigrations
python manage.py migrate

Create a superuser and run the server:
python manage.py createsuperuser
python manage.py runserver

Add data using the credentials in the django admin portal and run the web server again to see the results.
