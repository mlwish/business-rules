import json
from business_rules.engine import run_all
from transaction import Transaction
from variables import TransactionVariables
from actions import TransactionActions

rules = None
with open('rules.json') as rules_config:
        rules = json.load(rules_config)

# id, amount, ip, ip_country, shipping_country, card_type, bin_num)
txn1 = Transaction('t1', 100, '123.123.1.123', 'US', 'US', 'visa', 1200)
txn2 = Transaction('t2', 200, '13.123.2.123', 'US', 'RU', 'visa', 1800)
txn3 = Transaction('t3', 300, '13.123.3.123', 'US', 'UA', 'mastercard', 1200)
txn4 = Transaction('t4', 400, '123.123.12.123', 'US', 'FR', 'visa', 1200)
txn5 = Transaction('t5', 500, '13.12.1.123', 'US', 'DE', 'visa', 2222)
txn6 = Transaction('t6', 600, '123.12.12.123', 'US', 'SE', 'mastercard', 1200)
txn7 = Transaction('t7', 700, '12.123.123.13', 'US', 'BR', 'visa', 2888)

txns = [txn1, txn2, txn3, txn4, txn5, txn6, txn7] 

for txn in txns:

    run_all(rule_list=rules,
            defined_variables=TransactionVariables(txn),
            defined_actions=TransactionActions(txn),
            stop_on_first_trigger=True
    )