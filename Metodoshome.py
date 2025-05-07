import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
from Locators import Locators


class UrbanRoutesPage:

    def __init__(self, driver):
        self.modal_opcional = None
        self.driver = driver
        self.locators = Locators


    # Configurar la dirección (Desde - Hasta)
    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from_value(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to_value(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    # Pedir un Taxi
    def click_order_taxi_button(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.request_taxi_button)
            ).click()


    # Seleccionar la tarifa "Comfort"
    def click_comfort_tariff_button(self):
        comfort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.tariff_comfort_icon)
        )
        comfort_button.click()

    def get_comfort_tariff_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.tariff_comfort_icon)
        )


    # Rellenar el número de teléfono
    def fill_phone_number(self, phone=data.PHONE_NUMBER):
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.phone_input)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
        phone_field.clear()
        phone_field.send_keys(phone)

    def click_next_button(self):
        next_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.next_button)
        )
        next_btn.click()

    def enter_confirmation_code(self, code):
        code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.code_field)
        )
        code_field.clear()
        code_field.send_keys(code)

    def confirm_code(self):
        confirm_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.confirmation_code_button)
        )
        confirm_btn.click()

    def click_phone_method(self):
        phone_method_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.phone_method_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_method_button)
        phone_method_button.click()


    # Agregar una tarjeta de crédito
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    def click_payment_method_field(self):
        locator = self.locators.payment_method_button
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message="El botón 'Método de pago' no es clickeable después de 15 segundos"
        )
        self.scroll_to_element(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def click_away(self):
        body = self.driver.find_element("tag name", 'body')
        body.click()

    def click_add_card_button(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.add_card_button)
        )
        btn.click()

    def fill_card_details(self, card_number=data.CARD_NUMBER, card_code=data.CARD_CODE):
        number_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.card_number_field)
        )
        number_field.clear()
        number_field.send_keys(card_number)

        code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.card_code_field)
        )
        code_field.clear()
        code_field.send_keys(card_code)

    def click_add_card_module(self):
        module = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.add_card_module),
            message="Módulo 'plc' no clickeable después de 10 segundos"
        )
        self.scroll_to_element(module)  # Asegurar visibilidad
        try:
            module.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", module)

    def click_link_card(self):
        add_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.link_card_button),
            message="Botón 'Agregar' no está clickeable después de 15 segundos"
        )
        self.scroll_to_element(add_btn)
        try:
            add_btn.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", add_btn)

    def close_payment_modal(self):
        add_btn = (WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.close_payment_modal)
        ).click())

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.locators.close_payment_modal)
        )
        print("Modal de pago cerrado exitosamente.")
        return True


    # Escribir un mensaje al conductor
    def write_new_message(self, message=data.MESSAGE_FOR_DRIVER):
        message_field = self.driver.find_element(*self.locators.message_to_driver)
        message_field.clear()
        message_field.send_keys(message)
        return message_field.get_property('value')


    # Pedir Manta y pañuelos
    def scroll_blanket_and_scarves(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    def click_blanket_and_scarves_switch(self):
        switch_element = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.blanket_switch)
        ))

    def select_option_slider_blanket_and_scarves(self):
        slider = (WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.select_round)
        ).click())


    # Pedir 2 Helados
    def click_ice_cream_counter(self):
        counter_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.counter_ice_cream)
        )

    def click_add_icecream(self, count=2):
        counter_plus = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.add_ice_cream_Button)
        )
        counter_plus.click()
        print("Contador de helado incrementado.")
        return True


    # Botón buscar Taxi
    def get_order_taxi_locator(self):
        return self.locators.end_taxi_button

    def click_order_a_taxi(self):
        self.driver.find_element(*self.locators.end_taxi_button).click()


    # Esperar Modal información del conductor
    def click_driver_details(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))
        )

        driver_details_button = WebDriverWait(self.driver, 80).until(
            EC.element_to_be_clickable(self.locators.driver_details_button)
        )
        driver_details_button.click()