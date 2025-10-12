#!/bin/bash
# python manage.py migrate --noinput
# python manage.py collectstatic --noinput
# python manage.py runserver 0.0.0.0:$PORT

#!/bin/bash
set -e

# マイグレーション
python manage.py migrate --noinput

# 静的ファイル収集（CSSなど）
python manage.py collectstatic --noinput

# 本番サーバー起動 (Gunicorn)
gunicorn watanabe_meat_judge.wsgi:application --bind 0.0.0.0:$PORT
