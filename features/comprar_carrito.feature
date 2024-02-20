# language: es

@comprarCarrito
Característica: Comprar carrito

Antecedentes:
    Dado Que estoy en la página de login

  Escenario: Comprar los productos del carrito
    Cuando Ingreso mis credenciales válidas
    Y Hago click en el botón de inicio de sesión
    Entonces Se muestra la página principal
    Cuando Agrego productos al carrito de compra
    Entonces Se muestra la cantidad de productos agregados al carrito de compra
    Cuando Reviso mi carrito de compra
    Y Confirmo mis productos agregados
    Y Agrego mis datos de envío
    Y Confirmo mi orden de compra
    Entonces Se muestra un mensaje de confirmación de compra