FROM docker.io/bitnami/kubectl:latest

LABEL maintainer="Guilherme Albuquerque "heisenbuggerr""

WORKDIR /ansible-deploy

ADD ./ansible-k8s /ansible-deploy

RUN mkdir /etc/ansible \
    && mv /ansible-deploy/ansible.cfg /etc/ansible/

