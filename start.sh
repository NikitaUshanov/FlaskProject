#!/bin/bash

echo "Ожидание инициализации базы данных"
sleep 10
echo "Готово"

python cool.py
flask run -h 0.0.0.0 -p 8000