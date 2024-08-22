from app import models, columns

class Funcionarios(models.Model):
    _table = 'funcionarios'
    _description = 'Funcionario'

    _columns = {
        'cedula': columns.VarChar('Cédula'),
        'nombre': columns.VarChar('Nombre'),
        'cargo': columns.VarChar('Cargo'),
        'sueldo': columns.Decimal('Sueldo'),
        'fechaIngreso': columns.VarChar('Fecha de Ingreso')
    }
