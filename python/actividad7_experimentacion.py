# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from typing import Optional, List
import random
import statistics
from actividad1_nodos import Estudiante, EstadoAcademico
from actividad5_visualizacion_ascii import ArbolAcademicoVisual


class ArbolAcademicoExperimental(ArbolAcademicoVisual):
    def maximo(self) -> Optional[Estudiante]:
        if self._raiz is None:
            return None
        nodo = self._raiz
        while nodo.derecho:
            nodo = nodo.derecho
        return nodo.dato

    def buscar_rango_codigo(self, cod_min: int, cod_max: int) -> List[Estudiante]:
        resultado: List[Estudiante] = []
        self._buscar_rango(self._raiz, cod_min, cod_max, resultado)
        return resultado

    def _buscar_rango(self, nodo, min_val: int, max_val: int, res: List[Estudiante]) -> None:
        if nodo is None:
            return
        if min_val < nodo.dato.codigo:
            self._buscar_rango(nodo.izquierdo, min_val, max_val, res)
        if min_val <= nodo.dato.codigo <= max_val:
            res.append(nodo.dato)
        if max_val > nodo.dato.codigo:
            self._buscar_rango(nodo.derecho, min_val, max_val, res)


def actividad_71():
    print('=== 7.1 Arbol degenerado ===')
    arbol_deg = ArbolAcademicoExperimental()
    arbol_rand = ArbolAcademicoExperimental()
    n = 20

    for i in range(20_000_000, 20_000_000 + n):
        arbol_deg.insertar(Estudiante(i, f'Est_{i}', 'Test', 15.0, 100,
                                       EstadoAcademico.ACTIVO, '2024-I'))
    codigos_rand = random.sample(range(20_000_000, 29_999_999), n)
    for i, cod in enumerate(codigos_rand):
        arbol_rand.insertar(Estudiante(cod, f'Est_{i}', 'Test', 15.0, 100,
                                        EstadoAcademico.ACTIVO, '2024-I'))

    print(f'Altura arbol degenerado (orden creciente): {arbol_deg.altura()}')
    print(f'Altura arbol aleatorio: {arbol_rand.altura()}')
    print('El arbol degenerado tiene altura n-1 = 19, el aleatorio ~log2(n)')
    print()


def actividad_72():
    print('=== 7.2 Verificar post_order ===')
    arbol = ArbolAcademicoExperimental()
    for cod in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(Estudiante(cod, f'Est_{cod}', 'Test', 15.0, 100,
                                   EstadoAcademico.ACTIVO, '2024-I'))
    codigos = [e.codigo for e in arbol.post_order()]
    esperado = [20, 40, 30, 60, 80, 70, 50]
    print(f'Post-order obtenido: {codigos}')
    print(f'Post-order esperado: {esperado}')
    print(f'Coinciden: {codigos == esperado}')
    print()


def actividad_73():
    print('=== 7.3 Maximo ===')
    arbol = ArbolAcademicoExperimental()
    for cod in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(Estudiante(cod, f'Est_{cod}', 'Test', 15.0, 100,
                                   EstadoAcademico.ACTIVO, '2024-I'))
    max_est = arbol.maximo()
    print(f'Maximo codigo encontrado: {max_est.codigo if max_est else None}')
    print('Complejidad: O(h) donde h es la altura del arbol')
    print('Siempre se navega hacia la derecha')
    print()


def actividad_74():
    print('=== 7.4 Buscar rango de codigo ===')
    arbol = ArbolAcademicoExperimental()
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

    rango = arbol.buscar_rango_codigo(20210300, 20210700)
    print(f'Estudiantes en rango [20210300, 20210700]:')
    for e in rango:
        print(f'  {e.codigo} {e.nombre}')
    print('Usa la invariante BST para descartar subarboles completos')
    print()


if __name__ == '__main__':
    actividad_71()
    actividad_72()
    actividad_73()
    actividad_74()
