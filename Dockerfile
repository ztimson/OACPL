FROM python:3

# Add files
RUN mkdir /site
WORKDIR /site
ADD . /site/

# Set up configs
RUN mv OACPL/settings.base.py OACPL/settings.py

# Install packages
RUN pip install -r requirements.txt

# Initialize Django
RUN python3 manage.py makemigrations --no-input
RUN python3 manage.py migrate --no-input
RUN python3 manage.py collectstatic --no-input

EXPOSE 8000
ENTRYPOINT python3
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
