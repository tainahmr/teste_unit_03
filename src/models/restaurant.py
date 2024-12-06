class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        # BUG CORRIGIDO: restaurante escrito errado (escrito como restaturante) e passando cuisine_type no lugar do nome
        result = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}."
        result += f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."
        return result

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            # BUG CORRIGIDO: Se restaurante esta fechado a variavel open deve ser setada para True e nao False
            self.open = True
            # BUG CORRIGIDO: Ao abrir a quantidade de clientes deve ser 0 e nao -2
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        # MELHORIA: Removendo o else desnecessário
        return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        # MELHORIA: Removendo o else desnecessário
        return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            # BUG CORRIGIDO: Nao retornava nenhuma mensagem avisando da alteracao
            self.number_served = total_customers
            return f"{self.restaurant_name} possui {self.number_served} pessoas atendidas"
        # MELHORIA: Removendo o else desnecessário
        return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # BUG CORRIGIDO: Metodo nao incrementava a quantidade de clientes atendidos e sim alterava. If nao possui retorno
        if self.open:
            self.number_served = self.number_served + more_customers
            return f"{self.restaurant_name} agora possui {self.number_served} clientes atendidos"

        # MELHORIA: Removendo o else desnecessário
        return f"{self.restaurant_name} está fechado!"