# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List
from collections import deque
from actividad1_nodos import Estudiante, NodoBST, EstadoAcademico
from actividad2_arbol_recorridos import ArbolAcademico


class ArbolAcademicoConBusqueda(ArbolAcademico):
    def buscar(self, codigo: int) -> Optional[Estudiante]:
        nodo = self._buscar(self._raiz, codigo)
        return nodo.dato if nodo else None

    def _buscar(self, nodo, codigo):
        if nodo is None or nodo.dato.codigo == codigo:
            return nodo
        if codigo < nodo.dato.codigo:
            return self._buscar(nodo.izquierdo, codigo)
        return self._buscar(nodo.derecho, codigo)

    def eliminar(self, codigo: int) -> None:
        if self.buscar(codigo) is None:
            raise KeyError(f"Codigo no encontrado: {codigo}")
        self._raiz = self._eliminar(self._raiz, codigo)

    def _eliminar(self, nodo, codigo):
        if nodo is None:
            return None
        if codigo < nodo.dato.codigo:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, codigo)
        elif codigo > nodo.dato.codigo:
            nodo.derecho = self._eliminar(nodo.derecho, codigo)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            sucesor = self._minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.dato.codigo)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo


if __name__ == '__main__':
    arbol = ArbolAcademicoConBusqueda()
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

    encontrado = arbol.buscar(20210700)
    if encontrado:
        print(f'Encontrado: {encontrado.codigo} {encontrado.nombre} PPA: {encontrado.ppa}')
    no_existe = arbol.buscar(99999999)
    print(f'Buscar 99999999: {no_existe}')

    print(f'Nodos antes de eliminar: {len(arbol.in_order())}')
    arbol.eliminar(20210300)
    print(f'Nodos despues de eliminar 20210300: {len(arbol.in_order())}')
    print('In-Order despues:', [e.codigo for e in arbol.in_order()])
