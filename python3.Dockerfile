FROM python:3.6

WORKDIR /opt

RUN set -ex ; \
    pip install Pillow

USER root

CMD ["python", "./main.py", "mypng.img", "sans_serif.ttf", "HELR45W.ttf", "in.png"]
