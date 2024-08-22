from app import models, columns

class DetalleRecibos(models.Model):
    _table = 'detalle_recibos'
    _description = 'Detalle de Recibo'

    _columns = {
        'tipo_concepto': columns.VarChar('Tipo de Concepto'),
        'cantidad': columns.Decimal('Cantidad'),
        'monto': columns.Decimal('Monto')
    }
