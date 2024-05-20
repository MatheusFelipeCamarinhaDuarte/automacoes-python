Este projeto contempla autoamções criadas em python para que seja possível a migração de determinadas tabelas entre um banco de dados e outros variados.

develop:
pyinstaller --onefile --icon=app/raiz/ms3.ico --add-data "app:app" main.py

producao:
pyinstaller --onefile --windowed --icon=../selltech.ico --add-data "app:app" main.py
