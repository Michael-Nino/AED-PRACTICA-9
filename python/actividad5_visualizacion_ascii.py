# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from typing import Optional, List
import statistics
from actividad1_nodos import Estudiante, EstadoAcademico
from actividad4_consultas_estadisticas import ArbolAcademicoCompleto


class ArbolAcademicoVisual(ArbolAcademicoCompleto):
    def imprimir_arbol(self) -> None:
        print('\n---- Estructura del BST ----')
        self._imprimir(self._raiz, '', False)

    def _imprimir(self, nodo, prefix: str, is_left: bool) -> None:
        if nodo is None:
            return
        conector = '\u251c\u2500\u2500 ' if is_left else '\u2514\u2500\u2500 '
        print(f'{prefix}{conector}{nodo.dato.codigo} [PPA:{nodo.dato.ppa:.1f}]')
        ext = '\u2502   ' if is_left else '    '
        self._imprimir(nodo.izquierdo, prefix + ext, True)
        self._imprimir(nodo.derecho, prefix + ext, False)


if __name__ == '__main__':
    arbol = ArbolAcademicoVisual()
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

    arbol.imprimir_arbol()

    print('\nEliminando codigo 20210300...')
    arbol.eliminar(20210300)
    arbol.imprimir_arbol()
