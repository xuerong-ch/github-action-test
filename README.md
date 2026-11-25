# Calculadora: prueba de automatización

Proyecto Python parcialmente implementado para probar Jira → Codex → GitHub Actions.
Requiere Python 3.11 o posterior y no utiliza dependencias externas.

```powershell
python calculator.py 2 + 3
python calculator.py 4 '*' 3
python -m unittest discover -s tests -v
```

Suma, resta y multiplicación están implementadas. La división muestra un error
controlado y queda pendiente para la tarea de prueba. La suite inicial valida
las operaciones existentes; no certifica que la calculadora esté completa.

Los archivos `docs/*.txt` contienen documentación lista para copiar a Confluence,
una tarea propuesta y el procedimiento de verificación. El workflow Hello World
existente es manual; por sí solo no conecta Jira con Codex.
