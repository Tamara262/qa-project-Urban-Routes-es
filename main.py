from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


import data



# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

#Localizadores
class UrbanRoutesPage:


    #Direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    #Botones Principales
    order_rate_button = (By.CCS_SELECTOR, ".button.round")
    comfort_rate_icon = (By. XPATH, "//div[@class='tcard-title' and text()='Comfort`]")
    #Telefono
    phone_number_field_one= (By.XPATH, "//div[@class='np_text' and text() = 'Numero de teledono']")
    phone_number_field_two= (By.XPATH, "//*[@id='phone']")
    next_button = (By.XPATH,"//button[@class='button full' and text()= 'Siguiente']")
    #Confirmacion del pedido
    code_field = (By.XPATH,"//*[@id = 'code']")
    confirm_button = (By.XPATH,"//button[@class='button full' and text()= 'Confirmar']")
    #Informacion de pago
    card_number = (By.XPATH,"//div[@class='pp_button filled']")
    add_new_card_button = (By.XPATH, "//div[@class= 'pp-title' and texte() = 'Agregar tarjeta']")
    add_new_card_number = (By.XPATH, "//*[@id='number']")
    cvv_field = (By.NAME, "code")
    confirm_add_card_button = (By.XPATH, "//button[@class= 'button full' and text()= 'Agregar']")
    #Mensaje al conductor
    comment_field = (By.NAME, "comment")
    #Pedir Manta y Pañuelos
    slider_blanket_button = (By.XPATH, "//span[@class= 'slider round']")
    #Pedir Helado
    ice_cream_button_plus = (By.CLASS_NAME,'counter-plus')
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')
    complete_order_button = (By.CSS_SELECTOR, "span.smart-button-main")
    #Modal opcional
    timeout_modal = (By.CCS_SELECTOR, "div.order-number")
    switch_button = (By.CCS_SELECTOR, "switch-input")
    modal_serch_a_car = (By.CLASS_NAME,'order-header-title')
    order_screen_dysplayed = (By.CCS_SELECTOR, ".order.show")


#Metodos
    def __init__(self, driver):
        self.swicht_button = None
        self.add_new_card_numer = None
        self.phone_numer_field_two = None
        self.order_taxi_buton = None
        self.request_taxi_button = None
        self.driver = driver


#prueba 1
    def set_from(self, from_address):
       # self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver,  5).until(
           expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5 ).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(to_address)


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

#prueba 2
    def get_order_taxi_button(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_buton)
        )

    def click_on_order_taxi_button(self):
        self.get_order_taxi_button().click()

    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_rate_icon)
        )

    def click_on_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

#prueba 3
    def get_phone_number_field_one(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_number_field_one)
        )
    def click_on_phone_number_field_one(self):
        self.get_phone_number_field_one().click()

    def set_phone_numer_field_two(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_numer_field_two)
        ).send_keys(data.phone_number)

    def click_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        ).click()

    def get_code_field(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(self.code_field)
        )

    def set_code_number(self):
        self.get_code_field().send_keys(retrieve_phone_code(driver=self.driver))

    def click_confirm_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.confirm_button)
        ).click()

    def get_phone_number_value(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.presence_of_element_located(self.phone_number_field_two)
        ).get_property('value')

#prueba 4
    def get_card_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.card_number)
        ).click()

    def get_add_new_card_number_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_new_card_button)
        ).click()

    def set_new_card_number(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_new_card_number)
        ).send_keys(data.card_number)

    def new_card_value(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.add_new_card_numer)
        ).get_property('value')

    def get_cvv_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.cvv_field)
        )

    def set_cvv_number(self):
        self.get_cvv_field().send_keys(data.card_code + Keys.TAB)

    def get_cvv_value(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.cvv_field)
        ).get_property('value')

    def get_confirm_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.confirm_add_card_button)
        ).click()

#prueba 5
    def get_comment_field(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(self.comment_field)
        )

    def set_message_for_driver(self):
        self.get_comment_field().send_keys(data.message_for_driver)

    def message_for_driver(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.presence_of_element_located(self.comment_field)
        ).get_property('value')

#prueba 6
    def click_blanket_button(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(self.slider_blanket_button)
        ).click()

    def switch_button_active(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.presence_of_element_located(self.swicht_button)
        )

#prueba 7
    def get_ice_cream_button_plus(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(self.ice_cream_button_plus)
        )

    def click_ice_cream_button_plus(self):
        self.get_ice_cream_button_plus().click()


    def ice_cream_counter_value(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(self.complete_order_button)
        ).click()

#prueba 8
    def click_find_a_car(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(self.complete_order_button)
        ).click()

    def serch_a_car_screen(self):
        return WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located(self.modal_serch_a_car)
        ).text

#prueba 9
    def get_timeout_modal(self):
        return WebDriverWait(self.driver,50).until(
            expected_conditions.visibility_of_element_located(self.timeout_modal)
        )

    def order_shown(self):
        return WebDriverWait(self.driver,50).until(
            expected_conditions.visibility_of_element_located(self.order_screen_dysplayed)
        )


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
      # no lo modifiques ya que necesitamos un registro adicional habilitado para recuperar el codigo de confirmacion del telefono
      options = Options()
      options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

      cls.driver = webdriver.Chrome(service=Service(), options=options)
      cls.methods = UrbanRoutesPage(cls.driver)

#prueba 1
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)


        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#prueba 2
    def test_select_comfort_rate_icon(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_order_taxi_button()
        routes_page.click_on_comfort_rate_icon()
        comfort_rate = routes_page.get_comfort_rate_icon().text
        comfort_text ="Comfort"

        assert comfort_rate in comfort_text


#prueba 3
    def test_set_phone_number(self):
        self.test_select_comfort_rate_icon()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_on_phone_number_field_one()
        routes_pages.set_phone_numer_field_two()
        routes_pages.click_next_button()
        routes_pages.set_code_number()
        routes_pages.click_confirm_button()

        assert routes_pages.get_phone_number_value() == '+1 123 123 12 12'


#prueba 4
    def test_set_card_number(self):
        self.test_set_phone_number()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.get_card_number_field()
        routes_pages.get_add_new_card_number_button()
        routes_pages.set_new_card_number()
        routes_pages.get_cvv_field()
        routes_pages.set_cvv_number()
        routes_pages.get_confirm_add_card_button()

        assert routes_pages.new_card_value() == '1234 5678 9100'
        assert routes_pages.get_cvv_value() == '111'

#prueba 5
    def test_send_message_for_driver(self):
        self.test_select_comfort_rate_icon()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.get_comment_field()
        routes_pages.set_message_for_driver()

        assert routes_pages.message_for_driver()== 'Traiga un aperitivo'

#prueba 6
    def test_order_blanket(self):
        self.test_send_message_for_driver()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_blanket_button()

        assert routes_pages.switch_button_active().is_selected() == True


#prueba 7
    def test_order_two_ice_cream(self):
        self.test_order_blanket()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.get_ice_cream_button_plus()
        routes_pages.click_ice_cream_button_plus()
        routes_pages.click_ice_cream_button_plus()
        routes_pages.ice_cream_counter_value()

        assert routes_pages.ice_cream_counter_value() == '2'


#prueba 8
    def test_find_a_car(self):
        self.test_order_two_ice_cream()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_find_a_car()

        assert routes_pages.serch_a_car_screen() == 'Buscar automovil'


#prueba 9
    def test_driver_information(self):
        self.test_find_a_car()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.get_timeout_modal()

        assert routes_pages.order_shown().is_displayed() == True

        
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
