from business_rules import export_rule_data
from variables import TransactionVariables
from actions import TransactionActions
import json

with open('spec.json', 'w') as file:
    json.dump(export_rule_data(TransactionVariables, TransactionActions), file)
