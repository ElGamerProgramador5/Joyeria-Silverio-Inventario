@echo off
setlocal

cd /d %~dp0
cd inventario

:: Activar entorno virtual
call env\Scripts\activate

:: Lanzar servidor y luego abrir navegador cuando esté listo
start "" cmd /c "python manage.py runserver && start http://127.0.0.1:8000/"
