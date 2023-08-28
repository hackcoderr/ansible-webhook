from flask import Flask, request
from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
import json

app = Flask(__name__)

# Update the API endpoint
@app.route('/send', methods=['POST'])
def send():
    print("start trigger playbook")
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(
        tags={},
        listtags=False,
        listtasks=False,
        listhosts=False,
        syntax=False,
        connection='ssh',
        module_path=None,
        forks=100,
        remote_user='ubuntu',
        private_key_file='/etc/ansible/mykey.pem',
        ssh_common_args=None,
        ssh_extra_args=None,
        sftp_extra_args=None,
        scp_extra_args=None,
        become=True,
        become_method='sudo',
        become_user='root',
        verbosity=True,
        check=False,
        start_at_task=None
    )

    # Update the inventory path
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))

    # Update the playbook path
    pbex = PlaybookExecutor(playbooks=['/etc/ansible/create-file.yml'], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()

    # Handle and return results
    return json.dumps(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#if __name__ == "__main__":
#    app.run(debug=True)    

