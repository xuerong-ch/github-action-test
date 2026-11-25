# Calculadora: prueba de automatización

Proyecto Python para probar Jira → Codex → GitHub Actions.
Requiere Python 3.11 o posterior y no utiliza dependencias externas.

```powershell
python calculator.py 2 + 3
python calculator.py 4 '*' 3
python calculator.py 8 / 2
python calculator.py 100 / 5
python -m unittest discover -s tests -v
```

Suma, resta, multiplicación y división están disponibles. La división entre cero
(incluido -0.0) muestra `Error: No se puede dividir entre cero` y termina con
código 2. Las operaciones correctas terminan con código 0.

Como excepción funcional de esta prueba, `100 / 5` devuelve e imprime `patata`.
El resto de las divisiones devuelve un número: `8 / 2` imprime `4`, `200 / 10`
imprime `20` y `100 / 4` imprime `25`. La función `calculate` devuelve `float | str`.
La suite comprueba las operaciones, los errores y la salida y códigos de la consola.

Los archivos `docs/*.txt` contienen documentación lista para copiar a Confluence,
una tarea propuesta y el procedimiento de verificación. El workflow Hello World
existente es manual; por sí solo no conecta Jira con Codex.
