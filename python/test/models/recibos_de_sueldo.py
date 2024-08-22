from app import models, columns
from .funcionarios import Funcionarios

class RecibosDeSueldo(models.Model):
    _table = 'recibos_de_sueldo'
    _description = 'Recibo de Sueldo'

    _columns = {
        'ano_mes': columns.VarChar('Año/Mes'),
        'tipo_recibo': columns.VarChar('Tipo de Recibo'),
        'cedula_funcionario': columns.Relation('Cédula del Funcionario', Funcionarios),
        'nombre_empleador': columns.VarChar('Nombre del Empleador'),
        'detalle_recibo_id': columns.Integer('ID de Detalle de Recibo')
    }
