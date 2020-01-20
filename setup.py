"""
Install project requirements.
"""

from setuptools import setup, find_packages

setup(
    name="geoprotest_server",
    version="1.0.0",
    description='Sponsorship API',
    packages=find_packages(),
    include_package_data=True,
    scripts=["manage.py"],
    install_requires=[
        "Django==2.2.9",
        "djangorestframework==3.10.2",
        "python-decouple==3.1",
        "dj-database-url==0.5.0",
        "whitenoise==4.1.3",
        "psycopg2-binary==2.8.3",
        "django-rest-swagger==2.1.2",
        "gunicorn==19.9.0",
        "django-cors-middleware==1.4.0",
        "whitenoise==4.1.3",
        "requests==2.22.0",
        "django-cors-headers==3.1.0",
        "djangorestframework-jwt==1.11.0",
        "django-grappelli==2.13.1",
    ]
)
