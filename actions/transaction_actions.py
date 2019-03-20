from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from business_rules.actions import BaseActions, rule_action

class TransactionActions(BaseActions):

    def __init__(self, transaction):
        self.transaction = transaction
    
    @rule_action(params={"new_state": FIELD_TEXT})
    def auth(self, new_state):
        self.transaction.state = new_state

    @rule_action(params={"psp_option": FIELD_TEXT})
    def psp_route(self, psp_option):
        self.transaction.psp_route = psp_option
        print('%s should go thru %s' % (self.transaction.id, psp_option))
