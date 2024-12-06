from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            # MELHORIA: Alterando o for para um join para que o código fique mais limpo e a lista seja separada por
            # virgulas
            result = "No momento temos os seguintes sabores de sorvete disponíveis: "
            result += ", ".join(self.flavors)
            return result
        # MELHORIA: Removendo o else desnecessário
        return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            #BUG CORRIGIDO: Ambos if e else retornavam a lista com todos os sabores e não apenas o sabor procurado!
            if flavor in self.flavors:
                return f"Temos no momento {flavor}!"
            else:
                return f"Não temos no momento {flavor}!"
        # MELHORIA: Removendo o else desnecessário
        return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            # MELHORIA 1: Mudando pra um if que verifica se o sabor NÃO está na lista pra deixar o codigo mais compacto
            if flavor not in self.flavors:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            # MELHORIA 2: Não faz sentido adicionar sabores apenas se a lista já existir, pode ser o caso de ser a
            # primeira adição de sabor, então esse else funciona como resolução para a inexistencia de sabores na lista
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"

        return "Sabor já disponivel!"