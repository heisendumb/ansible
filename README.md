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

This will deploy service using helm. All necessary requirements such as namespace, docker image, chart, env_vars, router e volume information will also be created using information contained into template.

Below we can see template example to deployment service using helm.

#### deploy_vars example for Helm services
```
namespace: "teste"
app_name: "test"
number_replicas: 1

apps:
  - name: "{{app_name}}"
    deploy_name: "{{app_name}}"
    group: "{{namespace}}"
    image: "{{app_name}}"
    helm: "True"
    replicas: "{{number_replicas}}" # opcional
    version: "" # when helm is True
    chart: "" # when helm is True
    repo: "" # when helm is True
    env_vars:
    volumes:
      - pv_name: "volume_name"
        pv_size: "5"
        pv_path: "/"
        pv_acess_mode: "ReadWriteOnce"
    routes:
      - name: "{{app_name}}"
        hostname: "{{app_name}}-{{namespace}}"
        port: "9200"
        path: ""

      - name: "{{app_name}}"
        hostname: "{{app_name}}-{{namespace}}"
        port: "9200"
        path: "/teste"
```

#### Call

```
ansible-playbook site.yml -e deploy_vars=arquivo.yml -e target=ENVIRONMENT

```

---
### Deploy application

#### deploy_vars example for non Helm services
```
namespace: "teste"
app_name: "test"
number_replicas: 1

apps:
  - name: "{{app_name}}"
    deploy_name: "{{app_name}}"
    group: "{{namespace}}"
    image: "{{app_name}}"
    helm: "False"
    replicas: "{{number_replicas}}" # opcional
    routes:
      - name: "{{app_name}}"
        hostname: "{{app_name}}-{{namespace}}"
        port: "9200"
        path: ""

      - name: "{{app_name}}"
        hostname: "{{app_name}}-{{namespace}}"
        port: "9200"
        path: "/teste"

    env_vars:
      - "teste1=123"
      - "teste2=123"
```

#### Call

```
ansible-playbook site.yml -e deploy_vars=arquivo.yml -e target=ENVIRONMENT

```

---
### Common issues