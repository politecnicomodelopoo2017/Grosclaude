from .Pasajeros import Pasajero
from datetime import datetime
class Vuelo(object):

    def __init__(self,a,f,h,o,d,t,p):
        self.Avion = a
        self.Fecha = f
        self.Hora = h
        self.Origen = o
        self.Destino = d
        self.Tripulantes = t
        self.Pasajeros = p

    def CantPersonas(self):
        return len(self.Tripulantes) + len(self.Pasajeros)

    def PasajeroJoven(self):
        for item in self.Pasajeros:
            for item2 in self.Pasajeros:
                if item.FechaNacimiento.year > item2.FechaNacimiento.year:
                    a = item
                elif item.FechaNacimiento.year == item2.FechaNacimiento.year:
                    if item.FechaNacimiento.month >item2.FechaNacimiento.month:
                        a = item
                    elif item.FechaNacimiento.month == item2.FechaNacimiento.month:
                        if item.FechaNacimiento.day > item2.FechaNacimiento.day:
                            a = item
        return a

    def TripulacionMin(self):
        if len(self.Tripulantes) >= self.Avion.CantTrip:
            return True

    def Colados(self):
        Lis = []
        for item in self.Tripulantes:
            if item.ModAvion.Codigo != self.Avion.Codigo:
                Lis.append(item.Nombre)
        return Lis