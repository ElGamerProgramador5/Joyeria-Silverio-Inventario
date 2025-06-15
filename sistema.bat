@echo off
setlocal

echo ========================================
echo INSTALADOR - JOYERÍA SILBERIO
echo ========================================
echo.

:: Verificar si Python está instalado
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python no encontrado. Instalando...
    start /wait python-3.12.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    echo Reinicia este instalador después de completar la instalación de Python.
    pause
    exit /b
)

:: Instalar Django y Pillow globalmente
echo Instalando Django y Pillow...
pip install --upgrade pip
pip install django pillow

:: Ir a la carpeta del proyecto
cd inventario

:: Ejecutar migraciones
echo Ejecutando migraciones...
python manage.py migrate

echo.
echo ✅ Instalación completada.
echo Usa iniciar.bat para lanzar el sistema.
pause
