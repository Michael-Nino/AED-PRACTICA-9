# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from typing import Optional, List
import time
import random
import statistics
from actividad1_nodos import Estudiante, EstadoAcademico
from actividad5_visualizacion_ascii import ArbolAcademicoVisual


def generar_datos(n: int) -> list:
    codigos = random.sample(range(20_000_000, 29_999_999), n)
    return [Estudiante(cod, f'Estudiante_{i}', 'Ingenieria',
                       round(random.uniform(8.0, 20.0), 1), 100,
                       EstadoAcademico.ACTIVO, '2024-I')
            for i, cod in enumerate(codigos)]


def benchmark(n: int):
    datos = generar_datos(n)
    buscar_cod = datos[n // 2].codigo

    arbol_b = ArbolAcademicoVisual()
    t0 = time.perf_counter()
    for e in datos:
        arbol_b.insertar(e)
    t_ins_bst = (time.perf_counter() - t0) * 1000
    t0 = time.perf_counter()
    arbol_b.buscar(buscar_cod)
    t_bus_bst = (time.perf_counter() - t0) * 1000

    diccionario = {}
    t0 = time.perf_counter()
    for e in datos:
        diccionario[e.codigo] = e
    t_ins_dic = (time.perf_counter() - t0) * 1000
    t0 = time.perf_counter()
    _ = diccionario.get(buscar_cod)
    t_bus_dic = (time.perf_counter() - t0) * 1000

    print(f'N={n:>8} | BST ins:{t_ins_bst:7.2f}ms bus:{t_bus_bst:.4f}ms | '
          f'Dict ins:{t_ins_dic:7.2f}ms bus:{t_bus_dic:.4f}ms | '
          f'Altura BST: {arbol_b.altura()}')


if __name__ == '__main__':
    print('N         | BST insercion  busqueda   | Dict insercion  busqueda   | Altura')
    print('-' * 85)
    for n in [100, 1_000, 10_000, 100_000]:
        benchmark(n)
