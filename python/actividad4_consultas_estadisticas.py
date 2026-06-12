# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from typing import Optional, List
import statistics
from actividad1_nodos import Estudiante, EstadoAcademico
from actividad3_buscar_eliminar import ArbolAcademicoConBusqueda


class ArbolAcademicoCompleto(ArbolAcademicoConBusqueda):
    def por_rango_ppa(self, ppa_min: float, ppa_max: float = 20.0) -> List[Estudiante]:
        return [e for e in self.in_order() if ppa_min <= e.ppa <= ppa_max]

    def por_escuela(self, escuela: str) -> List[Estudiante]:
        return [e for e in self.in_order() if e.escuela == escuela]

    def por_estado(self, estado: EstadoAcademico) -> List[Estudiante]:
        return [e for e in self.in_order() if e.estado == estado]

    def estadisticas(self) -> dict:
        todos = self.in_order()
        if not todos:
            return {}
        ppas = [e.ppa for e in todos]
        return {
            'total_nodos': len(todos),
            'altura': self.altura(),
            'ppa_promedio': round(statistics.mean(ppas), 2),
            'ppa_minimo': min(ppas),
            'ppa_maximo': max(ppas),
            'total_activos': sum(1 for e in todos if e.estado == EstadoAcademico.ACTIVO),
        }


if __name__ == '__main__':
    arbol = ArbolAcademicoCompleto()
    datos = [
        Estudiante(20210500, 'Mamani Quispe, Juan', 'Ing. Sistemas', 15.8, 120, EstadoAcademico.ACTIVO, '2021-I'),
        Estudiante(20210300, 'Huanca Apaza, Maria', 'Ing. Civil', 14.2, 110, EstadoAcademico.ACTIVO, '2021-I'),
        Estudiante(20210700, 'Condori Flores, Pedro', 'Medicina', 17.1, 130, EstadoAcademico.ACTIVO, '2021-I'),
        Estudiante(20210100, 'Ticona Lupaca, Rosa', 'Contabilidad', 12.0, 90, EstadoAcademico.SUSPENDIDO, '2021-I'),
        Estudiante(20210400, 'Larico Ccama, Carlos', 'Ing. Sistemas', 16.5, 115, EstadoAcademico.ACTIVO, '2021-I'),
        Estudiante(20210600, 'Cutipa Vargas, Elena', 'Agronomia', 13.7, 100, EstadoAcademico.ACTIVO, '2021-I'),
        Estudiante(20210900, 'Pari Choque, Luis', 'Ing. Sistemas', 18.3, 140, EstadoAcademico.EGRESADO, '2021-I'),
    ]
    for e in datos:
        arbol.insertar(e)

    print('Estudiantes con PPA >= 15.0:')
    for e in arbol.por_rango_ppa(15.0):
        print(f'  {e.codigo} {e.nombre:<35} PPA: {e.ppa}')

    print()
    print('Estudiantes de Ing. Sistemas:')
    for e in arbol.por_escuela('Ing. Sistemas'):
        print(f'  {e.codigo} {e.nombre:<35} PPA: {e.ppa}')

    print()
    print('Estudiantes ACTIVOS:')
    for e in arbol.por_estado(EstadoAcademico.ACTIVO):
        print(f'  {e.codigo} {e.nombre:<35} PPA: {e.ppa}')

    print()
    print('Estadisticas del arbol:')
    for k, v in arbol.estadisticas().items():
        print(f'  {k:<20}: {v}')
