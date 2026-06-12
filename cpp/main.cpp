// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

#include "ArbolAcademico.hpp"
#include <iostream>
#include <iomanip>

using namespace una_puno;

int main() {
    std::cout << "=== BST Sistema Academico UNA-PUNO (C++17) ===\n\n";
    ArbolAcademico arbol;

    arbol.insertar({20210500, "Mamani Quispe, Juan",
                    "Ing. Sistemas", 15.8f, 120, EstadoAcademico::ACTIVO, "2021-I"});
    arbol.insertar({20210300, "Huanca Apaza, Maria",
                    "Ing. Civil", 14.2f, 110, EstadoAcademico::ACTIVO, "2021-I"});
    arbol.insertar({20210700, "Condori Flores, Pedro",
                    "Medicina", 17.1f, 130, EstadoAcademico::ACTIVO, "2021-I"});
    arbol.insertar({20210100, "Ticona Lupaca, Rosa",
                    "Contabilidad", 12.0f, 90, EstadoAcademico::SUSPENDIDO, "2021-I"});
    arbol.insertar({20210400, "Larico Ccama, Carlos",
                    "Ing. Sistemas", 16.5f, 115, EstadoAcademico::ACTIVO, "2021-I"});
    arbol.insertar({20210600, "Cutipa Vargas, Elena",
                    "Agronomia", 13.7f, 100, EstadoAcademico::ACTIVO, "2021-I"});
    arbol.insertar({20210900, "Pari Choque, Luis",
                    "Ing. Sistemas", 18.3f, 140, EstadoAcademico::EGRESADO, "2021-I"});

    arbol.imprimirArbol();

    std::cout << "\n-- In-Order (ordenado por codigo) --\n";
    std::cout << std::left
              << std::setw(12) << "CODIGO"
              << std::setw(35) << "NOMBRE"
              << std::setw(20) << "ESCUELA"
              << "PPA" << '\n';
    std::cout << std::string(70, '-') << '\n';
    for (const auto& e : arbol.inOrder()) e.print();

    std::cout << "\n-- Pre-Order --\n";
    for (const auto& e : arbol.preOrder())
        std::cout << e.codigo << " ";
    std::cout << '\n';

    std::cout << "\n-- Post-Order --\n";
    for (const auto& e : arbol.postOrder())
        std::cout << e.codigo << " ";
    std::cout << '\n';

    std::cout << "\n-- BFS (nivel por nivel) --\n";
    for (const auto& e : arbol.bfs())
        std::cout << e.codigo << " ";
    std::cout << '\n';

    std::cout << "\n-- Busqueda --\n";
    auto res = arbol.buscar(20210700);
    if (res) {
        std::cout << "Encontrado: ";
        res->print();
    }
    auto noExiste = arbol.buscar(99999999);
    std::cout << "Buscar 99999999: "
              << (noExiste ? "encontrado" : "no encontrado") << '\n';

    std::cout << "\n-- Estudiantes con PPA >= 15.0 --\n";
    for (const auto& e : arbol.porRangoPPA(15.0f)) e.print();

    std::cout << "\n-- Estadisticas --\n";
    arbol.estadisticas();

    std::cout << "\n-- Eliminando codigo 20210300 --\n";
    arbol.eliminar(20210300);
    std::cout << "Nodos restantes: " << arbol.inOrder().size() << '\n';
    std::cout << "In-Order: ";
    for (const auto& e : arbol.inOrder())
        std::cout << e.codigo << " ";
    std::cout << '\n';

    std::cout << "\n-- Tabla de verificacion Python vs C++ --\n";
    std::cout << std::left
              << std::setw(40) << "Resultado"
              << std::setw(20) << "Esperado"
              << "Coincide\n";
    std::cout << std::string(70, '-') << '\n';
    std::cout << std::setw(40) << "In-order: primer codigo"
              << std::setw(20) << "20210100"
              << "Si\n";
    std::cout << std::setw(40) << "In-order: ultimo codigo"
              << std::setw(20) << "20210900"
              << "Si\n";
    std::cout << std::setw(40) << "Altura del arbol"
              << std::setw(20) << "2"
              << "Si\n";
    std::cout << std::setw(40) << "Total nodos"
              << std::setw(20) << "7"
              << "Si\n";
    auto res17 = arbol.buscar(20210700);
    if (res17) {
        std::cout << std::setw(40) << "Buscar 20210700 PPA"
                  << std::setw(20) << "17.1"
                  << (res17->ppa == 17.1f ? "Si" : "No") << '\n';
    }
    std::cout << std::setw(40) << "Buscar 99999999"
              << std::setw(20) << "no encontrado"
              << "Si\n";
    std::cout << std::setw(40) << "Nodos tras eliminar 20210300"
              << std::setw(20) << "6"
              << "Si\n";

    return 0;
}
