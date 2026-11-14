class StockInvalidoError(Exception): pass
class DispositivoEcologico:
 def __init__(self,nombre,stock): self.nombre=nombre; self.stock=stock
 @property
 def stock(self): return self._stock
 @stock.setter
 def stock(self,v):
  if v<0: raise StockInvalidoError()
  self._stock=v
class PanelSolar(DispositivoEcologico): pass
