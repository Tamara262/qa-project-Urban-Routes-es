from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from UrbanRoutesLocators import UrbanRoutesLocators


import data
import helpers



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from UrbanRoutesMethods import UrbanRoutesPage
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

        # Prueba 1
    def test_set_route(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        assert self.routes_page.get_from_value() == data.ADDRESS_FROM
        assert self.routes_page.get_to_value() == data.ADDRESS_TO


     # Prueba 2
    def test_select_comfort_tariff(self):
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_comfort_tariff_button()
        comfort_tariff = self.routes_page.get_comfort_tariff_element()
        assert comfort_tariff.is_displayed(), "El botón de tarifa Comfort no se mostró correctamente"


   # Prueba 3
    def test_fill_phone_number(self):
        self.routes_page.click_phone_method()
        self.routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.routes_page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.enter_confirmation_code(code)
        self.routes_page.confirm_code()
        phone_input_value = self.driver.find_element(*self.routes_page.locators.phone_input).get_attribute("value")
        assert phone_input_value == data.PHONE_NUMBER, f"Se esperaba {data.PHONE_NUMBER}, pero se obtuvo {phone_input_value}"

        # Prueba 4

    def test_add_credit_card(self):
        self.routes_page.click_payment_method_field()
        self.routes_page.click_add_card_button()
        self.routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        self.routes_page.click_add_card_module()
        self.routes_page.click_link_card()
        self.routes_page.close_payment_modal()

        # Prueba 5

    def test_write_message(self):
        written_message = self.routes_page.write_new_message(data.MESSAGE_FOR_DRIVER)
        assert written_message == data.MESSAGE_FOR_DRIVER

        # Prueba 6

    def test_request_blanket_and_scarves(self, urban_routes_page=None):
        self.routes_page.click_blanket_and_scarves_switch()
        self.routes_page.select_option_slider_blanket_and_scarves()

        # Prueba 7

    def test_request_icecream(self, urban_routes_page=None):
        self.routes_page.click_ice_cream_counter()
        self.routes_page.click_add_icecream()
        self.routes_page.click_add_icecream()

        # prueba 8

        def test_search_taxi(self):
            WebDriverWait(self.driver, 40).until(
                expected_conditions.visibility_of_element_located(
                    self.routes_page.get_order_taxi_locator()
                )
            ).click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

