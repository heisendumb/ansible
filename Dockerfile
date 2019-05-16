FROM docker.io/bitnami/kubectl:latest

LABEL maintainer="Guilherme Albuquerque "heisendumb""

WORKDIR /ansible-deploy

COPY ./ansible-k8s /ansible-deploy

RUN mkdir /etc/ansible \
    && mv /ansible-deploy/ansible.cfg /etc/ansible/

