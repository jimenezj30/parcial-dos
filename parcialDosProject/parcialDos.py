




salario_base_Mensual1 = 3000000
cargo_empleado1 = "directivo"
Nivel_desempeño1 = "alto"

salario_base_Mensual2 = 2500000
cargo_empleado2 = 'directivo'
Nivel_desempeño2 = 'Medio'

salario_base_Mensual3 = 1300000
cargo_empleado3 = 'Auxiliar'
Nivel_desempeño3 = 'Bajo'

salario_base_Mensual4 = 1750000
cargo_empleado4 = 'operativo'
Nivel_desempeño4 = 'medio'


def calcular_bonificacion(salario_base_Mensual, cargo_empleado,Nivel_desempeño):

    tasa_bonificacion = {
        'directivo': {'alto': 0.20, 'medio': 0.10, 'bajo': 0.0},
        'Operativo': {'alto': 0.15, 'medio': 0.05, 'bajo': 0.0}
    }

    # Bonificación basada en el cargo y nivel de desempeño
    bonificacion = salario_base_Mensual * tasa_bonificacion[cargo_empleado][Nivel_desempeño]

    # Total a recibir
    total = salario_base_Mensual + bonificacion

    return bonificacion,


empleados = [
    {'salario_base': salario_base_Mensual1, 'cargo': cargo_empleado1, 'desempeño': Nivel_desempeño1},
    {'salario_base': salario_base_Mensual2, 'cargo': cargo_empleado2, 'desempeño': Nivel_desempeño2},
    {'salario_base': salario_base_Mensual3, 'cargo': cargo_empleado3, 'desempeño': Nivel_desempeño3},
    {'salario_base': salario_base_Mensual4, 'cargo': cargo_empleado4, 'desempeño': Nivel_desempeño4},
]


for empleado in empleados:
    salario_base = empleado['salario_base']
    cargo_empleado = empleado["Cargo_empleado"]
    Nivel_desempeño = empleado['Nivel_desempeño']

    if cargo_empleado ['directivo', 'operativo']:
        bonificacion, total = calcular_bonificacion(salario_base, cargo_empleado,Nivel_desempeño)
        print(f"-----Resumen del Pago-----")
        print(f"Cargo: {cargo_empleado.capitalize()}")
        print(f"Nivel de Desempeño: {Nivel_desempeño.capitalize()}")
        print(f"Salario Base: ${salario_base}")
        print(f"Bonificación: ${bonificacion}")
        print(f"Total a Recibir: ${total}")
        print("-----------------------------------------")
    else:
        print(f"-----Resumen del Pago-----")
        print(f"Cargo: {cargo_empleado.capitalize()}")
        print(f"Nivel de Desempeño: {Nivel_desempeño.capitalize()}")
        print(f"Salario Base: ${salario_base}")
        print(f"Bonificación: $0")
        print(f"Total a Recibir: ${salario_base}")
        print("-----------------------------------------")



