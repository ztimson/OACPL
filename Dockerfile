FROM python:3
EXPOSE 8000

ADD . /
RUN rm OACPL/settings.py
RUN mv OACPL/settings.base.py OACPL/settings.py

RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations --no-input
RUN python3 manage.py migrate --no-input
RUN python3 manage.py collectstatic --no-input
