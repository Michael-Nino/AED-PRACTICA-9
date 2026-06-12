# Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List
from collections import deque


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


if __name__ == '__main__':
    e1 = Estudiante(20210500, 'Mamani Quispe, Juan', 'Ing. Sistemas',
                    15.8, 120, EstadoAcademico.ACTIVO, '2021-I')
    nodo = NodoBST(dato=e1)
    print('Nodo creado:', nodo.dato.codigo, nodo.dato.nombre)
    print('Hijo izquierdo:', nodo.izquierdo)
    print('Hijo derecho: ', nodo.derecho)
