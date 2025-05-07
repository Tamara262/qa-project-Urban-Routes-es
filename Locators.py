from selenium.webdriver.common.by import By


class UrbanRoutesLocators:
    # Direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Botones Principales
    request_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')  # Pedir un taxi
    tariff_comfort_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")  # Seleccionar Tarifa
    end_taxi_button = (By.CLASS_NAME, "smart-button-main")  #Botón buscar Taxi

    # Teléfono
    phone_method_button = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[contains(text(), "Siguiente")]')

    # Confirmación del teléfono
    code_field = (By.ID, 'code')
    confirmation_code_button = (By.XPATH, '//*[contains(text(), "Confirmar")]')

    # Información de pago
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_number_field = (By.NAME, 'number')
    card_code_field = (By.NAME, 'code')
    add_card_module = (By.CLASS_NAME, "plc")
    link_card_button = (By.XPATH, "//div[contains(@class, 'modal')]//button[. = 'Agregar']")
    close_payment_modal = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    # Mensaje al conductor
    message_to_driver = (By.ID, 'comment')

    # Pedir Manta y Pañuelos
    blanket_switch = (By.XPATH, "//input[@type='checkbox' and @class='switch-input']")
    select_round = (By.CSS_SELECTOR, ".slider.round")

    # Pedir Helado
    counter_ice_cream = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']")
    add_ice_cream_Button = (By.CLASS_NAME, "counter-plus")

    # Modal opcional
    driver_details_button = (By.XPATH, "//button[@class='order-button']//img[@alt='burger']")
