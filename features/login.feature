# language: es
@login
Característica: Iniciar sesión

  Antecedentes: 
    Dado Que estoy en la página de login

  @loginValido
  Escenario: Iniciar sesión con credenciales válidas
    Cuando Ingreso mis credenciales válidas "standard_user" y "secret_sauce"
    Y Hago click en el botón de inicio de sesión
    Entonces Se muestra la página principal

  @loginInvalido
  Escenario: Iniciar sesión con credenciales inválidas
    Cuando Ingreso mis credenciales inválidas
    Y Hago click en el botón de inicio de sesión
    Entonces Aparece un mensaje de error

  @loginVariosUsuarios
  Esquema del escenario: Iniciar sesión con varios usuarios
    Cuando Ingreso mis credenciales válidas "<user>" y "<password>"
    Y Hago click en el botón de inicio de sesión

    Ejemplos: 
      | user                    | password     |
      | standard_user           | secret_sauce |
      | locked_out_user         | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |
      | error_user              | secret_sauce |
      | visual_user             | secret_sauce |
