@echo off
title Lab Pengukuran Virtual
echo Menjalankan Lab Pengukuran Virtual...
cd /d %~dp0
python -m streamlit run streamlit_app.py
pause