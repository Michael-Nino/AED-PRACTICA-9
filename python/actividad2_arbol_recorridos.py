# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List
from collections import deque
from actividad1_nodos import Estudiante, NodoBST, EstadoAcademico


class ArbolAcademico:
    def __init__(self) -> None:
        self._raiz: Optional[NodoBST] = None

    def insertar(self, e: Estudiante) -> None:
        self._raiz = self._insertar(self._raiz, e)

    def _insertar(self, nodo: Optional[NodoBST], e: Estudiante) -> NodoBST:
        if nodo is None:
            return NodoBST(dato=e)
        if e.codigo < nodo.dato.codigo:
            nodo.izquierdo = self._insertar(nodo.izquierdo, e)
        elif e.codigo > nodo.dato.codigo:
            nodo.derecho = self._insertar(nodo.derecho, e)
        else:
            raise ValueError(f"Codigo duplicado: {e.codigo}")
        return nodo

    def in_order(self) -> List[Estudiante]:
        resultado: List[Estudiante] = []
        self._in_order(self._raiz, resultado)
        return resultado

    def _in_order(self, nodo, res):
        if nodo is None:
            return
        self._in_order(nodo.izquierdo, res)
        res.append(nodo.dato)
        self._in_order(nodo.derecho, res)

    def pre_order(self) -> List[Estudiante]:
        resultado: List[Estudiante] = []
        self._pre_order(self._raiz, resultado)
        return resultado

    def _pre_order(self, nodo, res):
        if nodo is None:
            return
        res.append(nodo.dato)
        self._pre_order(nodo.izquierdo, res)
        self._pre_order(nodo.derecho, res)

    def post_order(self) -> List[Estudiante]:
        resultado: List[Estudiante] = []
        self._post_order(self._raiz, resultado)
        return resultado

    def _post_order(self, nodo, res):
        if nodo is None:
            return
        self._post_order(nodo.izquierdo, res)
        self._post_order(nodo.derecho, res)
        res.append(nodo.dato)

    def bfs(self) -> List[Estudiante]:
        if self._raiz is None:
            return []
        resultado, cola = [], deque([self._raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

    def altura(self) -> int:
        return self._altura(self._raiz)

    def _altura(self, nodo) -> int:
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))


if __name__ == '__main__':
    arbol = ArbolAcademico()
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
    print(f'Altura del arbol: {arbol.altura()}')
    print()
    print('In-Order (ordenado por codigo):')
    for e in arbol.in_order():
        print(f'  {e.codigo} {e.nombre:<35} PPA: {e.ppa}')
    print()
    print('Pre-Order:')
    print([e.codigo for e in arbol.pre_order()])
    print()
    print('Post-Order:')
    print([e.codigo for e in arbol.post_order()])
    print()
    print('BFS (nivel por nivel):')
    print([e.codigo for e in arbol.bfs()])
