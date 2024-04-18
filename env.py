import os

os.environ.setdefault("SECRET_KEY", "cook_it")
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DB_URL", "postgresql:///community")