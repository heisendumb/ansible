# Ansible

## deploy_vars arquivo exemplo

```
namespace: "teste"
app_name: "elasticsearch"
number_replicas: 2

apps:
  - name: "{{app_name}}"
    deploy_name: "{{app_name}}"
    group: "{{namespace}}"
    image: "{{app_name}}"
    replicas: "{{number_replicas}}" # opcional
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
