from flask import Flask, render_template, request
from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

app = Flask(__name__)


@app.route("/")
def index():
    if form.validate_on_submit():
        if 'Reboot Servers' in request.form:
            return render_template('successful.html')
        elif 'Malware Scan' in request.form:
            return render_template('successful.html')
    return render_template('index.html')
