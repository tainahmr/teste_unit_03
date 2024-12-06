import difflib

from src.models.restaurant import Restaurant


class TestRestaurant:
    restaurant = Restaurant('Big Belly Burger', 'fast food')

    def test_describe_restaurant(self):
        expected_result = "Esse restaurante chama Big Belly Burger e serve fast food."
        expected_result += "Esse restaurante está servindo 0 consumidores desde que está aberto."
        result = self.restaurant.describe_restaurant()
        assert result == expected_result

    def test_open_restaurant(self):
        expected_result = 'Big Belly Burger agora está aberto!'
        result = self.restaurant.open_restaurant()
        assert result == expected_result

    def test_open_restaurant_twice(self):
        expected_result = 'Big Belly Burger já está aberto!'
        self.restaurant.open_restaurant()
        result = self.restaurant.open_restaurant()
        assert result == expected_result

    def test_close_restaurant(self):
        expected_result = 'Big Belly Burger agora está fechado!'
        self.restaurant.open_restaurant()
        result = self.restaurant.close_restaurant()
        assert result == expected_result

    def test_close_restaurant_closed(self):
        expected_result = 'Big Belly Burger já está fechado!'
        result = self.restaurant.close_restaurant()
        assert result == expected_result

    def test_set_number_served(self):
        expected_result = 'Big Belly Burger possui 8 pessoas atendidas'
        self.restaurant.open_restaurant()
        result = self.restaurant.set_number_served(8)
        assert result == expected_result

    def test_set_number_served_closed_restaurant(self):
        expected_result = 'Big Belly Burger está fechado!'
        self.restaurant.close_restaurant()
        result = self.restaurant.set_number_served(8)
        assert result == expected_result

    def test_increment_number_served(self):
        expected_result = 'Big Belly Burger agora possui 12 clientes atendidos'
        self.restaurant.open_restaurant()
        self.restaurant.set_number_served(8)
        result = self.restaurant.increment_number_served(4)
        assert result == expected_result

    def test_increment_number_served_closed_restaurante(self):
        expected_result = 'Big Belly Burger está fechado!'
        self.restaurant.close_restaurant()
        result = self.restaurant.increment_number_served(4)
        assert result == expected_result