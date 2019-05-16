# Ansible

## deploy_vars arquivo exemplo

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

## Chamada

```
ansible-playbook site.yml -e deploy_vars=arquivo.yml -e target=ENVIRONMENT

```
