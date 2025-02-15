# pyscore
## 程式架構
```
/score_system
├── app.py
├── score.txt
└── templates
    ├── index.html
    ├── login.html
    └── admin.html
```
## 如何使用
1. 安裝pip
`pip install flask flask_login gunicorn`
2. start flask
`gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app`
3. 訪問 host:8000