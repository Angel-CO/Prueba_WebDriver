from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

def capture_screenshot(context, title='captured_screenshot'):
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name=f'{title}',
        attachment_type=allure.attachment_type.PNG
    )

@given('Que estoy en la página de login')
def estoy_en_la_pagina_de_login(context):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.saucedemo.com/")
    capture_screenshot(context,'estoy_en_la_pagina_de_login')

@when('Ingreso mis credenciales válidas')
def ingreso_mis_credenciales_validas(context) :
    input_username = context.driver.find_element(by=By.ID, value='user-name')
    input_password = context.driver.find_element(by=By.ID, value='password')
    input_username.send_keys('standard_user')
    input_password.send_keys('secret_sauce')
    capture_screenshot(context,'ingreso_mis_credenciales_validas')    

@when('Hago click en el botón de inicio de sesión')
def hago_click_en_el_botón_de_inicio_de_sesion(context) :
    btn_login = context.driver.find_element(by=By.ID, value='login-button')
    btn_login.click()

@then('Se muestra la página principal')
def se_muestra_la_pagina_principal(context) :
    status = context.driver.find_element(by=By.ID, value="page_wrapper").is_displayed()
    url = context.driver.current_url
    assert status
    assert url == "https://www.saucedemo.com/inventory.html"
    capture_screenshot(context,'se_muestra_la_pagina_principal')    

@when('Ingreso mis credenciales inválidas')
def ingreso_mis_credenciales_invalidas(context) :
    input_username = context.driver.find_element(by=By.ID, value='user-name')
    input_password = context.driver.find_element(by=By.ID, value='password')
    input_username.send_keys('locked_out_user')
    input_password.send_keys('secret_sauce')
    capture_screenshot(context,'ingreso_mis_credenciales_invalidas')

@then('Aparece un mensaje de error')
def aparece_un_mensaje_de_error(context):
    error_message = context.driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
    assert error_message == "Epic sadface: Sorry, this user has been locked out."
    capture_screenshot(context,'aparece_un_mensaje_de_error')


@when('Ingreso mis credenciales válidas "{user}" y "{password}"')
def step_cuando(context, user, password) :
    input_username = context.driver.find_element(by=By.ID, value='user-name')
    input_password = context.driver.find_element(by=By.ID, value='password')
    input_username.send_keys(user)
    input_password.send_keys(password)
    capture_screenshot(context,'ingreso_credenciales_validas')


