from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators

import collaboratorhome
import data


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from Metodoshome import UrbanRoutesPage
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

        # 1. Configurar la dirección (Desde - Hasta)
    def test_set_route(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        assert self.routes_page.get_from_value() == data.ADDRESS_FROM
        assert self.routes_page.get_to_value() == data.ADDRESS_TO


        # 2. Seleccionar la tarifa "Comfort"
    def test_select_comfort_tariff(self):
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_comfort_tariff_button()
        comfort_tariff = self.routes_page.get_comfort_tariff_element()
        assert comfort_tariff.is_displayed(), "El botón de tarifa Comfort no se mostró correctamente"

        # 3. Rellenar el número de teléfono
    def test_fill_phone_number(self):
        self.routes_page.click_phone_method()
        self.routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.routes_page.click_next_button()
        code = collaboratorhome.retrieve_phone_code(self.driver)
        self.routes_page.enter_confirmation_code(code)
        self.routes_page.confirm_code()
        phone_input_value = self.driver.find_element(*self.routes_page.locators.phone_input).get_attribute("value")
        assert phone_input_value == data.PHONE_NUMBER, f"Se esperaba {data.PHONE_NUMBER}, pero se obtuvo {phone_input_value}"

        # 4. Agregar una tarjeta de crédito
    def test_add_credit_card(self):
        self.routes_page.click_payment_method_field()
        self.routes_page.click_add_card_button()
        self.routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        self.routes_page.click_add_card_module()
        self.routes_page.click_link_card()
        self.routes_page.close_payment_modal()


        # 5. Escribir un mensaje para el conductor
    def test_write_message(self):
        written_message = self.routes_page.write_new_message(data.MESSAGE_FOR_DRIVER)
        assert written_message == data.MESSAGE_FOR_DRIVER


        # 6. Pedir una manta y pañuelos
    def test_request_blanket_and_scarves(self, urban_routes_page=None):
        self.routes_page.click_blanket_and_scarves_switch()
        self.routes_page.select_option_slider_blanket_and_scarves()


        # 7. Pedir 2 helados

    def test_request_icecream(self, urban_routes_page=None):
        self.routes_page.click_ice_cream_counter()
        self.routes_page.click_add_icecream()
        self.routes_page.click_add_icecream()


        # 8. Buscar un taxi

    def test_search_taxi(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(
                self.routes_page.get_order_taxi_locator()
            )
        ).click()


        # 9. Esperar Modal información del conductor
    def test_wait_modal(self):
        self.routes_page.click_driver_details()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()