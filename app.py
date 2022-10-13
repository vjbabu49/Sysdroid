from flask import Flask, render_template, request
from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'Reboot Servers':
            reboot_servers()
            return render_template('successful.html')
        elif request.form['action'] == 'Restart Service':
              return render_template('restart_service.html')
        elif request.form['action'] == 'Malware Scan':
              malware_scan()
              return render_template('successful.html')
        elif request.form['action'] == 'Disk Usage':
              disk_usage()
              return render_template('successful.html')
        elif request.form['action'] == 'Freeup disk space':
              free_disk_space()
              return render_template('successful.html')

    elif request.method == 'GET':
        return render_template('index.html')


def reboot_servers():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/test_reboot_server.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()


@app.route('/restart_service', methods=('GET', 'POST'))
def restart_service():
    if request.method == 'POST':
        if request.form['action'] == 'Restart httpd':
            restart_httpd()
            return render_template('successful.html')
        elif request.form['action'] == 'Restart SSH':
             # restart_ssh()
              results = restart_ssh()
              print(results)
              return render_template('successful.html', result = results)
        elif request.form['action'] == 'Restart cron':
              restart_cron()
              return render_template('successful.html')
        elif request.form['action'] == 'Restart apache2':
              restart_apache2()
              return render_template('successful.html')

    elif request.method == 'GET':
        return render_template('restart_service.html')


def malware_scan():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='ec2-user', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/malware_scan.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()


def disk_usage():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/disk_usage.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()


def free_disk_space():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/free_disk_space.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()



def restart_httpd():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/restart_httpd.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()



def restart_ssh():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/restart_ssh.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()
    data = results


def restart_cron():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/restart_cron.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()



def restart_apache2():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                    module_path=None, forks=100, remote_user='ec2-user', private_key_file='/home/vijay/test_key_pair.pem',
                                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(
        loader=loader, sources=('/home/vijay/hosts',))

    variable_manager = VariableManager(
        loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['/home/vijay/restart_apache2.yaml'],
                            inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()
