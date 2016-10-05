FROM python

ADD routes.py /

ADD servers.py /

ADD update.py /

ADD test.py /

ADD test/ /

ADD configs/ /

RUN pip install bottle

CMD [ "python", "./routes.py" ]
