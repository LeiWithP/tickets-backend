# tickets-backend
Backend on djangorest for gaytan crud projects

# Iniciar Virtual Enviroment
pip install virtualenv
python -m virtualenv venv

Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate

# instalar Requerimientos
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate
