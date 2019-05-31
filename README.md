# Ansible

This documentation presents how-to with Ansible to automate process deploy for applications (such as: python, rubygolang and java) or services (such as: mediawiki, sharelatex, grafana and etc....).

* Bellow are the release versions of each software used in this project:
  * Python v3.6.7
  * Ansible v2.7.10
  * Kubernetes v1.11.8
  * kubectl v1.9.1
  * Docker v1.13.1

### Tabel of contents
<!--ts-->
 * [Deploy service - using Helm](#deploy-service-helm)
 * [Deploy aplication](#deploy-application)
 * [Common issues]($common-issues)
<!--te-->

---
### Deploy service - usign Helm

### Deploy application

## deploy_vars example for non Helm services
```
namespace: "teste"
app_name: "test"
number_replicas: 1

apps:
  - name: "{{app_name}}"
    deploy_name: "{{app_name}}"
    group: "{{namespace}}"
    image: "{{app_name}}"
    helm: "False/True"
    replicas: "{{number_replicas}}" # opcional
    version: "" # when helm is True
    chart: "" # when helm is True
    repo: "" # when helm is True
    routes:
      - name: "{{app_name}}"
        hostname: "{{app_name}}-{{namespace}}"
        port: "9200"
        path: ""

      - name: "{{app_name}}2"
        hostname: "{{app_name}}-{{namespace}}"
        port: "9200"
        path: "/teste"

    env_vars:
      - "teste1=123"
      - "teste2=123"
```

## Call

```
ansible-playbook site.yml -e deploy_vars=arquivo.yml -e target=ENVIRONMENT

```

---
# Common issues