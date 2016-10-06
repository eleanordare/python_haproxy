FROM registry.access.redhat.com/rhscl/python-35-rhel7

ADD routes.py /
ADD servers.py /
ADD update.py /
ADD test.py /
ADD test/ /
ADD configs/ /

RUN yum install -y python-pip
RUN pip install bottle
RUN yum install haproxy
RUN systemctl start haproxy
RUN systemctl enable haproxy

CMD [ "python", "./routes.py" ]
