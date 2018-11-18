import hashlib

class Estado:
	def __init__(self, actual, pendientes): #id para el md5??
		self.nActual=actual
		self.nPendientes=pendientes
		self.id=self.codificarMD5()
	def codificarMD5(self):
		h=hashlib.md5()
		h.update(self.nActual.encode('utf-8'))
		for n in self.nPendientes:
			h.update(n.encode('utf-8'))
		return h.hexdigest().encode('utf-8')