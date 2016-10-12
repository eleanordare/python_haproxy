FROM fedora 

ADD routes.py /
ADD servers.py /
ADD update.py /
ADD test.py /
ADD test /test
ADD configs /configs

USER root
ENV container=docker

RUN yum install python-pip
RUN pip install bottle
RUN yum install haproxy

CMD service haproxy start

EXPOSE 5000
EXPOSE 8081

CMD [ "python", "./routes.py" ]
