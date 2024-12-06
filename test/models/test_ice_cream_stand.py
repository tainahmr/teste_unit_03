from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:
    flavor_list = ["Chocolate", "Baunilha", "Morango", "Flocos", "Napolitano", "Cookies and Cream",
                   "Menta com Chocolate", "Coco", "Ninho", "Pistache", "Doce de Leite", "Farinha Lactea"]
    ice_cream_stand = IceCreamStand("Noonan's", 'Sorveteria', flavor_list)

    def test_flavors_available(self):
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis: " + ", ".join(self.flavor_list)
        self.ice_cream_stand.open_restaurant()
        result = self.ice_cream_stand.flavors_available()
        assert result == expected_result

    def test_flavor_unavailable(self):
        exepected_result = "Estamos sem estoque atualmente!"
        new_stand = IceCreamStand("John's", "Sorveteria", [])
        new_stand.open_restaurant()
        result = new_stand.flavors_available()
        assert result == exepected_result

    def test_find_flavor(self):
        expected_result = "Temos no momento Ninho!"
        self.ice_cream_stand.open_restaurant()
        result = self.ice_cream_stand.find_flavor("Ninho")
        assert result == expected_result

    def test_cant_find_flavor(self):
        expected_result = "Não temos no momento Nutella!"
        self.ice_cream_stand.open_restaurant()
        result = self.ice_cream_stand.find_flavor("Nutella")
        assert result == expected_result

    def test_find_flavor_without_stock(self):
        exepected_result = "Estamos sem estoque atualmente!"
        new_stand = IceCreamStand("John's", "Sorveteria", [])
        new_stand.open_restaurant()
        result = new_stand.find_flavor("Ninho")
        assert result == exepected_result

    def test_add_flavor(self):
        expected_result = "Nutella adicionado ao estoque!"
        self.ice_cream_stand.open_restaurant()
        result = self.ice_cream_stand.add_flavor("Nutella")
        assert result == expected_result

    def test_add_existing_flavor(self):
        expected_result = "Sabor já disponivel!"
        self.ice_cream_stand.open_restaurant()
        result = self.ice_cream_stand.add_flavor("Ninho")
        assert result == expected_result

    def test_add_first_flavor(self):
        exepected_result = "Nutella adicionado ao estoque!"
        new_stand = IceCreamStand("John's", "Sorveteria", [])
        new_stand.open_restaurant()
        result = new_stand.add_flavor("Nutella")
        assert result == exepected_result