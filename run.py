# coding: utf-8
import os
from app import create_app

app = create_app('default' or os.getenv('CONFIG'))

if __name__ == '__main__':
    app.run()
