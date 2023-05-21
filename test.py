from main import saludos, despedida

saludo = saludos("Ever")
print(saludo)
assert saludo == "saludos Ever"
desp = despedida("John")
print(desp)
assert desp == "Hasta luego John"
