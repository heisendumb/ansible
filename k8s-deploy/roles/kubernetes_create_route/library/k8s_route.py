from ansible.module_utils.basic import *
import json

module = AnsibleModule(
    argument_spec={
        'services': {'required': True, 'type': 'json'},
        'appname': {'required': True, 'type': 'str'}
    }
)

result = {}

for item in (json.loads(json.loads(module.params['services']).get('resources'))):
    if item['metadata']['name'] == module.params['appname']:
        result = item

module.exit_json(changed=False, result=result)
