@ec@echo off
setlocal

cd /d %~dp0
cd inventario

:: Activar entorno virtual
call env\Scripts\activate

:: Iniciar servidor en segundo plano con start /B
start /B cmd /c "python manage.py runserver"

:: Esperar unos segundos para asegurar que el servidor arranque
timeout /t 2 >nul

:: Abrir navegador
start http://127.0.0.1:8000/

exit

