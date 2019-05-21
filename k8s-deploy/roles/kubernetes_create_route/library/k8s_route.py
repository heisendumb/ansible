from ansible.module_utils.basic import *
import json

module = AnsibleModule(
    argument_spec={
        'services': {'required': True, 'type': 'json'},
        'srvname': {'required': True, 'type': 'str'}
    }
)

result = {}

for item in module.params['services']:got 
    # if item['metadata']['labels']['app'] == module.params['appname']:
    #    result = item

    #module.exit_json(changed=False, result=result)
