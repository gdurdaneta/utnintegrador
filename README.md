# utnintegrador

Esta aplicacion fue desarrollada en 3 ventanas por Gerardo Urdaneta y Francisco Bryndum.

En el archivo visuallogin.py estan las ventanas de login (class loginApp) y la ventana para la creacion de usuarios (class baseApp). Luego esta el archivo visualbase.py donde esta la ventana para las operaciones dentro de la base de datos (class App) como: modificar, eliminar y consultar data. 

El programa inicia del archivo visuallogin.py donde existen 2 opciones:

- Ingresar: previa validacion de un usuario y contraseña que sean validadas por la base de datos lo que nos permite el acceso a la ventana de operaciones de base de datos.

Para modificar un dato se debe ingresar el usuario en el primer entry y el dato a modificar en el segundo entry, luego tildar la informacion que se quiere modificar (Password, Nombre, Apellido, Telefono, Dni).

Para eliminar información se debe ingresar el usuario en el primer entry y la contraseña en el segundo entry, si esta informacion es corroborada con la base de datos el usuario es borrado.

Para consultar solo hay que ingresar el dato del usuario para que nos devuelva la informacion que tiene en la base de datos.

- Crear: Es posible crear sin previamente validar un ingreso de usuario y contraseña. Solo se deben completar los datos y apretar el boton crear.

