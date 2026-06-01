class Customer :
    def __init__(self, name, cpf, has_cnh, cnh_number, contact ):
        self.name = name
        self.cpf = cpf
        self.has_cnh = has_cnh
        self.cnh_number = cnh_number
        self.contact = contact

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"CPF: {self.cpf}")
        print(f"has_cnh: {self.has_cnh}")
        print(f"Contact: {self.contact}")
        if self.has_cnh:
            print(f"CNH number: {self.cnh_number}")

