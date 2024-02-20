from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@when('Agrego productos al carrito de compra')
def agrego_productos_al_carrito_de_compra(context) :
    for i in range(1,7):
        btn_add_to_card = context.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div/div/div/div[' + str(i) + ']/div[2]/div[2]/button')
        btn_add_to_card.click()
    time.sleep(5)

@when('Decido quitar los productos del carrito de compra')
def decido_quitar_los_productos_del_carrito_de_compra(context) :
    for i in range(1,7):
        btn_add_to_card = context.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div/div/div/div[' + str(i) + ']/div[2]/div[2]/button')
        btn_add_to_card.click()
    time.sleep(5)

@then('Se muestra el carrito de compra vacío')
def se_muestra_el_carrito_de_compra_vacio(context) :
    #shopping_cart = context.driver.find_element(by=By.CLASS_NAME, value='shopping_cart_link').is_displayed()
    elements = context.driver.find_elements(by=By.CLASS_NAME, value='shopping_cart_badge')
    if len(elements) == 0:
        assert True
    else:
        assert False

@then('Se muestra la cantidad de productos agregados al carrito de compra')
def se_muestra_la_cantidad_de_productos_agregados_al_carrito_de_compra(context):
    quantity_products = context.driver.find_element(by=By.CLASS_NAME, value='shopping_cart_badge').text
    assert quantity_products == "6"
