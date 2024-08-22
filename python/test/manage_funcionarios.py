import csv
import os
from app import env
import pandas as pd

Funcionarios = env['funcionarios']
RecibosDeSueldo = env['recibos_de_sueldo']
DetalleRecibos = env['detalle_recibos']

csv_file_path = 'datos_iniciales.csv'

def cargar_datos_iniciales_desde_csv():
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Crear el funcionario
            funcionario = Funcionarios.create(
                {
                    'cedula': row['cedula'],
                    'nombre': row['nombre'],
                    'cargo': row['cargo'],
                    'sueldo': float(row['sueldo']),
                    'fechaIngreso': row['fechaIngreso']
                }
            )
            print(f"Funcionario {funcionario.nombre} cargado")

            # Convertir detalle_recibo_id a entero si no es None
            detalle_recibo_id = row['detalle_recibo_id']
            if detalle_recibo_id and detalle_recibo_id.strip() != '':
                detalle_recibo_id = int(detalle_recibo_id)
            else:
                detalle_recibo_id = None

            # Crear el recibo de sueldo
            recibo = RecibosDeSueldo.create({
                'ano_mes': row['ano_mes'],
                'tipo_recibo': row['tipo_recibo'],
                'cedula_funcionario': funcionario.id,  # Asegurarse de que este sea un entero
                'nombre_empleador': row['nombre_empleador'],
                'detalle_recibo_id': detalle_recibo_id
            })
            print(f"Recibo del funcionario {funcionario.nombre} cargado")

def eliminar_recibos_por_cedula(cedula):
    recibos = RecibosDeSueldo.records()
    recibosEliminar = [r for r in recibos if r.cedula_funcionario == cedula]

    for recibo in recibosEliminar:
        recibo.delete()
        print(f"El recibo con Id: {recibo.id} para el funcionario con cedula {cedula} fue eliminado")

def modificar_funcionario_por_cedula(cedula, nombreNuevo, cargoNuevo):
    funcionarios = Funcionarios.records()
    funcionario = next((f for f in funcionarios if f.cedula == cedula), None)
    if funcionario:
        funcionario.update({
            'nombre': nombreNuevo,
            'cargo': cargoNuevo
        })
        print(f"Funcionario con cedula {cedula} modificado. Su nuevo nombre es {funcionario.nombre} y su nuevo cargo {funcionario.cargo}")
    else:
        print(f"No se encontro un funcionario con la cedula ingresada")

# Ejemplos de uso
cargar_datos_iniciales_desde_csv()
eliminar_recibos_por_cedula('12345678')
modificar_funcionario_por_cedula('12345678', 'Nombre Nuevo funcionario', 'Cargo Nuevo funcionario')
