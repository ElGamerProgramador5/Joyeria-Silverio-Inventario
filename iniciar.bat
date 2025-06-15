@echo off
cd /d %~dp0
cd inventario
start http://127.0.0.1:8000/
python manage.py runserver
