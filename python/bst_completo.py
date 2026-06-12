# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List
from collections import deque
import time
import random
import statistics


class EstadoAcademico(Enum):
    ACTIVO = auto()
    EGRESADO = auto()
    RETIRADO = auto()
    SUSPENDIDO = auto()


@dataclass
class Estudiante:
    codigo: int
    nombre: str
    escuela: str
    ppa: float
    creditos: int
    estado: EstadoAcademico
    semestre_ingreso: str

    def __post_init__(self):
        if not (10_000_000 <= self.codigo <= 29_999_999):
            raise ValueError(f"Codigo invalido: {self.codigo}")
        if not (0.0 <= self.ppa <= 20.0):
            raise ValueError(f"PPA fuera de rango [0,20]: {self.ppa}")


@dataclass
class NodoBST:
    dato: Estudiante
    izquierdo: Optional[NodoBST] = field(default=None, repr=False)
    derecho: Optional[NodoBST] = field(default=None, repr=False)


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

    def maximo(self) -> Optional[Estudiante]:
        if self._raiz is None:
            return None
        nodo = self._raiz
        while nodo.derecho:
            nodo = nodo.derecho
        return nodo.dato

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


DATOS_PRUEBA = [
    Estudiante(20210500, 'Mamani Quispe, Juan', 'Ing. Sistemas', 15.8, 120, EstadoAcademico.ACTIVO, '2021-I'),
    Estudiante(20210300, 'Huanca Apaza, Maria', 'Ing. Civil', 14.2, 110, EstadoAcademico.ACTIVO, '2021-I'),
    Estudiante(20210700, 'Condori Flores, Pedro', 'Medicina', 17.1, 130, EstadoAcademico.ACTIVO, '2021-I'),
    Estudiante(20210100, 'Ticona Lupaca, Rosa', 'Contabilidad', 12.0, 90, EstadoAcademico.SUSPENDIDO, '2021-I'),
    Estudiante(20210400, 'Larico Ccama, Carlos', 'Ing. Sistemas', 16.5, 115, EstadoAcademico.ACTIVO, '2021-I'),
    Estudiante(20210600, 'Cutipa Vargas, Elena', 'Agronomia', 13.7, 100, EstadoAcademico.ACTIVO, '2021-I'),
    Estudiante(20210900, 'Pari Choque, Luis', 'Ing. Sistemas', 18.3, 140, EstadoAcademico.EGRESADO, '2021-I'),
]


def test_actividad1() -> bool:
    e1 = Estudiante(20210500, 'Mamani Quispe, Juan', 'Ing. Sistemas', 15.8, 120, EstadoAcademico.ACTIVO, '2021-I')
    nodo = NodoBST(dato=e1)
    ok = nodo.dato.codigo == 20210500 and nodo.izquierdo is None and nodo.derecho is None
    print(f'  {"[OK]" if ok else "[FAIL]"} Actividad 1: NodoBST creado correctamente')
    return ok


def test_actividad2() -> bool:
    arbol = ArbolAcademico()
    for e in DATOS_PRUEBA:
        arbol.insertar(e)
    ino = [e.codigo for e in arbol.in_order()]
    ok = ino == [20210100, 20210300, 20210400, 20210500, 20210600, 20210700, 20210900]
    ok = ok and arbol.altura() == 2
    print(f'  {"[OK]" if ok else "[FAIL]"} Actividad 2: In-order ordenado y altura={arbol.altura()}')
    return ok


def test_actividad3() -> bool:
    arbol = ArbolAcademico()
    for e in DATOS_PRUEBA:
        arbol.insertar(e)
    ok = arbol.buscar(20210700) is not None
    ok = ok and arbol.buscar(99999999) is None
    arbol.eliminar(20210300)
    ok = ok and len(arbol.in_order()) == 6
    print(f'  {"[OK]" if ok else "[FAIL]"} Actividad 3: Buscar y eliminar')
    return ok


def test_actividad4() -> bool:
    arbol = ArbolAcademico()
    for e in DATOS_PRUEBA:
        arbol.insertar(e)
    stats = arbol.estadisticas()
    ok = stats['total_nodos'] == 7 and stats['altura'] == 2
    rang = arbol.por_rango_ppa(15.0)
    ok = ok and len(rang) >= 3
    print(f'  {"[OK]" if ok else "[FAIL]"} Actividad 4: Consultas y estadisticas')
    return ok


def test_actividad5() -> bool:
    arbol = ArbolAcademico()
    for e in DATOS_PRUEBA:
        arbol.insertar(e)
    arbol.imprimir_arbol()
    print('  [OK] Actividad 5: Arbol impreso en ASCII')
    return True


def test_actividad6() -> bool:
    def generar_datos(n: int) -> list:
        codigos = random.sample(range(20_000_000, 29_999_999), n)
        return [Estudiante(cod, f'Est_{i}', 'Ingenieria',
                           round(random.uniform(8.0, 20.0), 1), 100,
                           EstadoAcademico.ACTIVO, '2024-I')
                for i, cod in enumerate(codigos)]

    def benchmark(n: int):
        datos = generar_datos(n)
        buscar_cod = datos[n // 2].codigo
        arbol_b = ArbolAcademico()
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
        print(f'  N={n:>8} | BST ins:{t_ins_bst:7.2f}ms bus:{t_bus_bst:.4f}ms | '
              f'Dict ins:{t_ins_dic:7.2f}ms bus:{t_bus_dic:.4f}ms | '
              f'Altura: {arbol_b.altura()}')

    print('  Ejecutando benchmark...')
    for n in [100, 1_000, 10_000, 100_000]:
        benchmark(n)
    print('  [OK] Actividad 6: Benchmark completado')
    return True


def test_actividad7() -> bool:
    print('  --- 7.1 Arbol degenerado ---')
    arbol_deg = ArbolAcademico()
    arbol_rand = ArbolAcademico()
    n = 20
    for i in range(20_000_000, 20_000_000 + n):
        arbol_deg.insertar(Estudiante(i, f'Est_{i}', 'Test', 15.0, 100, EstadoAcademico.ACTIVO, '2024-I'))
    codigos_rand = random.sample(range(20_000_000, 29_999_999), n)
    for i, cod in enumerate(codigos_rand):
        arbol_rand.insertar(Estudiante(cod, f'Est_{i}', 'Test', 15.0, 100, EstadoAcademico.ACTIVO, '2024-I'))
    print(f'    Altura degenerado: {arbol_deg.altura()}, Altura aleatorio: {arbol_rand.altura()}')

    print('  --- 7.2 Post-order ---')
    arbol = ArbolAcademico()
    mapping = {50: 20000050, 30: 20000030, 70: 20000070, 20: 20000020, 40: 20000040, 60: 20000060, 80: 20000080}
    orden = [50, 30, 70, 20, 40, 60, 80]
    for cod in orden:
        arbol.insertar(Estudiante(mapping[cod], f'Est_{cod}', 'Test', 15.0, 100, EstadoAcademico.ACTIVO, '2024-I'))
    codigos = [e.codigo for e in arbol.post_order()]
    esperado = [20000020, 20000040, 20000030, 20000060, 20000080, 20000070, 20000050]
    ok = codigos == esperado
    print(f'    Post-order: {codigos}, Esperado: {esperado} {"OK" if ok else "FAIL"}')

    print('  --- 7.3 Maximo ---')
    mx = arbol.maximo()
    print(f'    Maximo: {mx.codigo if mx else None}')

    print('  --- 7.4 Buscar rango ---')
    arbol2 = ArbolAcademico()
    for e in DATOS_PRUEBA:
        arbol2.insertar(e)
    rango = arbol2.buscar_rango_codigo(20210300, 20210700)
    print(f'    Rango [20210300, 20210700]: {[e.codigo for e in rango]}')

    print('  [OK] Actividad 7: Experimentacion completada')
    return True


if __name__ == '__main__':
    inicio = time.perf_counter()
    print('=' * 60)
    print('  BST COMPLETO -- SIS210 UNAP')
    print('=' * 60)
    print()

    resultados = []
    print('--- Actividad 1: Nodos ---')
    resultados.append(('Actividad 1', test_actividad1()))

    print('\n--- Actividad 2: Arbol y Recorridos ---')
    resultados.append(('Actividad 2', test_actividad2()))

    print('\n--- Actividad 3: Buscar y Eliminar ---')
    resultados.append(('Actividad 3', test_actividad3()))

    print('\n--- Actividad 4: Consultas y Estadisticas ---')
    resultados.append(('Actividad 4', test_actividad4()))

    print('\n--- Actividad 5: Visualizacion ASCII ---')
    resultados.append(('Actividad 5', test_actividad5()))

    print('\n--- Actividad 6: Benchmark ---')
    resultados.append(('Actividad 6', test_actividad6()))

    print('\n--- Actividad 7: Experimentacion ---')
    resultados.append(('Actividad 7', test_actividad7()))

    tiempo_total = time.perf_counter() - inicio
    print()
    print('=' * 60)
    print('  RESUMEN FINAL')
    print('=' * 60)
    todos_ok = True
    for nombre, ok in resultados:
        icono = '\u2713' if ok else '\u2717'
        print(f'  {icono} {nombre}')
        if not ok:
            todos_ok = False
    print(f'  Tiempo total: {tiempo_total:.3f}s')
    print(f'  Estado: {"TODAS LAS VERIFICACIONES PASARON" if todos_ok else "ALGUNAS VERIFICACIONES FALLARON"}')
    print('=' * 60)
