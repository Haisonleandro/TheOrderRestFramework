El proyecto cuenta con dos aplicaciones:

La primera, apps.finance, incluye 2 modelos (Product, Order), junto con sus serializadores y set de vistas,
de el modelo Product, únicamente los usuarios autenticados (Employees) pueden registrar, actualizar o eliminarles, puesto que, evidentemente,
no se espera que el cliente de a pie sea capaz de modificar esta información, sin embargo, este sí que es capaz de registrar nuevas órdenes,
el modelo Order contiene entre sus parámetros el status y orderType, los cuales indican el estado en que se encuentra la orden (On hold; En espera, On Preparation; En preparación,
Served; servido), y el tipo de orden (To go; para llevar, For here; para la mesa), se indica como clave foránea el producto a pedir, y se registra automáticamente
la fecha en que se registró la orden para llevar una mejor trazabilidad.

Se cuenta con un usuario personalizado, Employee, que hace referencia a los empleados, puesto que se espera que todos y cada uno de ellos se encuentren registrados,
además de los parámetros predeterminados de Django, se incluyen age (edad), legalId (Identificacion) y hireDate (Fecha de contratación).

Además de esto, la página de administración fue alterada para de este modo hacer display de estos parámetros adicionales.