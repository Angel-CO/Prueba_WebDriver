from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@when('Reviso mi carrito de compra')
def reviso_mi_carrito_de_compra(context):
    btn_shopping_cart = context.driver.find_element(by=By.CLASS_NAME, value='shopping_cart_link')
    btn_shopping_cart.click()

@when('Confirmo mis productos agregados')
def Confirmo_mis_productos_agregados(context) :
    time.sleep(5)
    btn_checkout = context.driver.find_element(by=By.ID, value='checkout')
    btn_checkout.click()
    
@when('Agrego mis datos de envío')
def agrego_mis_datos_de_envio(context) :
    time.sleep(5)
    input_first_name = context.driver.find_element(by=By.ID, value='first-name')    
    input_last_name = context.driver.find_element(by=By.ID, value='last-name')    
    input_postal_code = context.driver.find_element(by=By.ID, value='postal-code')
    input_first_name.send_keys("Ángel")
    input_last_name.send_keys("Calderón")
    input_postal_code.send_keys("91330")

    btn_continue = context.driver.find_element(by=By.ID, value='continue')
    btn_continue.click()

@when('Confirmo mi orden de compra')
def confirmo_mi_orden_de_compra(context) :
    time.sleep(5)
    total = context.driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
    assert total == "Total: $140.34"
    btn_finish = context.driver.find_element(by=By.ID, value='finish')
    btn_finish.click()

@then('Se muestra un mensaje de confirmación de compra')
def se_muestra_un_mensaje_de_confirmación_de_compra(context) :
    time.sleep(5)
    complete_header = context.driver.find_element(by=By.CLASS_NAME, value='complete-header').text
    complete_text = context.driver.find_element(by=By.CLASS_NAME, value='complete-text').text
    assert complete_header == "Thank you for your order!" and complete_text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
