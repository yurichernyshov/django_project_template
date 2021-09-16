FROM python

RUN pip install django

WORKDIR /apps/django_project

COPY ./django_project /apps/django_project

EXPOSE 8080

CMD ["python", "/apps/django_project/manage.py", "runserver", "0.0.0.0:8080"]

