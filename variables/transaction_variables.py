from business_rules.variables import BaseVariables, numeric_rule_variable, string_rule_variable

class TransactionVariables(BaseVariables):

    def __init__(self, transaction):
        self.transaction = transaction
    
    # @numeric_rule_variable
    # def amount(self):
    #     return self.transaction.amount
    
    # @string_rule_variable
    # def ip_country(self):
    #     return self.transaction.ip_country
    
    # @string_rule_variable
    # def shipping_country(self):
    #     return self.transaction.shipping

    @string_rule_variable
    def card_type(self):
        return self.transaction.card_type
    
    @numeric_rule_variable
    def bin_num(self):
        return self.transaction.bin_num
    
