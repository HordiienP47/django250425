import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from test_app.models import Task
from datetime import datetime, timedelta
