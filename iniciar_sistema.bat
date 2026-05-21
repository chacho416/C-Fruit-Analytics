@echo off
title Chachos Software - Panel de Control
echo =========================================
echo   INICIANDO ESTACION DE ESCANEO AIoT
echo =========================================
echo.
echo 1. Despertando el Cerebro (YOLOv8)...
start "Servidor IA" cmd /k "py -m uvicorn servidor:app --reload"

timeout /t 3 >nul

echo 2. Conectando con el Hardware (Arduino)...
start "Puente Serial" cmd /k "py cliente_serial.py"

echo.
echo Sistemas en linea
echo Ya puedes cerrar esta ventana principal.