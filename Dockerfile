FROM python:3.10-alpine as development


EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /electronic_shop
WORKDIR /electronic_shop


COPY . /electronic_shop

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" user && chown -R user /electronic_shop
RUN chown -R user:user /vol/
RUN chmod -R 755 /electronic_shop
# RUN chmod -R 777 /electronic_shop/_logs/
RUN chmod -R 755 /vol/web
USER user

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'Electronic_shop'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "electronic_shop.wsgi"]

FROM development as production
RUN mkdir /electronic_shop/_logs/

CMD ["sh"]