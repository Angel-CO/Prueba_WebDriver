# language: es

@agregarYRemoverProductos
Característica: Agregar y remover productos

Antecedentes:
    Dado Que estoy en la página de login

  @removerProductos
  Escenario: Remover productos del carrito de compra
    Cuando Ingreso mis credenciales válidas
    Y Hago click en el botón de inicio de sesión
    Entonces Se muestra la página principal
    Cuando Agrego productos al carrito de compra
    Y Decido quitar los productos del carrito de compra
    Entonces Se muestra el carrito de compra vacío

  @agregarProductos
  Escenario: Agregar productos al carrito de compra
    Cuando Ingreso mis credenciales válidas
    Y Hago click en el botón de inicio de sesión
    Entonces Se muestra la página principal
    Cuando Agrego productos al carrito de compra
    Entonces Se muestra la cantidad de productos agregados al carrito de compra