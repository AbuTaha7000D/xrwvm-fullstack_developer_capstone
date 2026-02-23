import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='root').exists():
    User.objects.create_superuser('root', 'root@example.com', 'root123')
    print("Superuser created.")
else:
    print("Superuser already exists.")
