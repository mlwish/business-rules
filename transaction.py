class Transaction():
    
    def __init__(self, id, amount, ip, ip_country, shipping_country, card_type, bin_num):
        self.id = id
        self.amount = amount
        self.ip = ip
        self.ip_country = ip_country
        self.shipping_country = shipping_country
        self.state = 'PENDING'
        self.card_type = card_type
        self.bin_num = bin_num
        
        self.psp_route = None
