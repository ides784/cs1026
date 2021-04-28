class Part:
    def __init__(self, pn=0, desc="", quant=0, price=0.0):
        self.partNo = pn
        self.description = desc
        self.quantity = quant
        self.price = price

    def __repr__(self):
        return str(self.partNo) + "[" + self.description + "," + str(self.quantity) + "," + str(self.price) + "]"

aPart = Part(55, "Power Drill", 5, 79.99)
print(aPart)
