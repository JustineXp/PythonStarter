class Tab:

    menu = {
        'chicken': 25,
        'beef': 10,
        'burger': 15,
        'pork': 22,
        'soft_drink': 20,
        'vegetables': 18
    }

    def __init__(self):
        self.total = 0
        self.items = []
    
    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total

        total = self.total + tax + service

        print(f"ORDER BILL")
        
        for item in self.items:
            print(f"{item:20} : ${self.menu[item]}")

        print(f'{"Total":20} $ {total:.2f}')