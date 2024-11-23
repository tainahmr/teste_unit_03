class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #BUG: o result está escrito ""restaturante"
        #BUG: o primeiro result não chama o restaurant_name
        result = f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}."
        result += f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."
        return result

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        #BUG: no if not o self.open não é false
        #CORREÇÃO: self.open = True
        if not self.open:
            self.open = False
            #BUG: O number_served não pode ser negativo, não é utilizado nessa função
            #CORREÇÃO: o number_served deve ser 0
            self.number_served = -2
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        #BUG: falta return do if
        if self.open:
            self.number_served = total_customers
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        #BUG: não está incrementando o número
        # BUG: falta return do if
        if self.open:
            self.number_served = more_customers
        else:
            return f"{self.restaurant_name} está fechado!"
