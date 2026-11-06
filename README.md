README.md
#COMO Se USA

1) Se imprime el título "———cormado———" para dar la bienvenida al colmado.

3) Se crea un diccionario llamado articulos donde se guardan los productos con su precio. Por ejemplo pollo: 250, agua: 25, huevos: 10, tomate: 15.

5) Se añade while True para que el programa se repita y no se cierre cuando termine una compra.

7) Se crea una variable llamada pd donde con input se le pregunta al usuario que tu quieres, y se le dice que escriba salir o metel.

8-10) Se crea un if donde si la variable pd es igual a salir se imprime "ruede mio" y se cierra el programa con break.

12-17) Se crea un if donde si la variable pd es igual a metel algo se le pregunta al usuario que quiere metel y a cuanto lo va a poner. Con int se convierte el precio a numero y con articulos[new] = pr se guarda el producto nuevo en el diccionario. Después se imprime "ya mio, ta listo" y se usa continue para volver al inicio.

19-20) Se crea un if donde si la variable pd está dentro del diccionario articulos se muestra el precio con f"el {pd} cuesta {articulos[pd]}".

21-22) Se crea un else donde si el producto no está en el diccionario la consola dice "no tenemos eso mio".
