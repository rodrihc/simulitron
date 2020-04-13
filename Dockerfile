FROM python:3.6.7

WORKDIR /app

ENV FLASK_APP manage.py
ENV FLASK_RUN_HOST 0.0.0.0

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /app

EXPOSE  5000

CMD ["flask", "run"]