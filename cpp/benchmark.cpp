// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

#include "ArbolAcademico.hpp"
#include <chrono>
#include <random>
#include <algorithm>
#include <set>

using namespace una_puno;
using Clock = std::chrono::high_resolution_clock;

std::vector<Estudiante> generarDatos(int n) {
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> distCod(20000000, 29999999);
    std::uniform_real_distribution<float> distPPA(8.0f, 20.0f);

    std::set<int> unicos;
    while ((int)unicos.size() < n) {
        unicos.insert(distCod(rng));
    }
    std::vector<int> codigos(unicos.begin(), unicos.end());
    std::shuffle(codigos.begin(), codigos.end(), rng);

    std::vector<Estudiante> datos;
    for (int i = 0; i < n; i++)
        datos.emplace_back(codigos[i], "Estudiante_" + std::to_string(i),
                           "Ingenieria", 10.0f + distPPA(rng) * 0.5f,
                           100, EstadoAcademico::ACTIVO, "2024-I");
    return datos;
}

void benchmark(int n) {
    auto datos = generarDatos(n);
    int buscarCod = datos[n / 2].codigo;

    ArbolAcademico arbol;
    auto t0 = Clock::now();
    for (auto& e : datos) arbol.insertar(e);
    auto t1 = Clock::now();
    double ms_ins = std::chrono::duration<double, std::milli>(t1 - t0).count();

    auto t2 = Clock::now();
    arbol.buscar(buscarCod);
    auto t3 = Clock::now();
    double ms_bus = std::chrono::duration<double, std::milli>(t3 - t2).count();

    std::cout << std::setw(8) << n
              << " | ins: " << std::fixed << std::setprecision(3)
              << std::setw(9) << ms_ins << " ms"
              << " | bus: " << std::setw(8) << ms_bus << " ms"
              << " | altura: " << arbol.altura() << '\n';
}

int main() {
    std::cout << "       N | Insercion  | Busqueda  | Altura\n";
    std::cout << std::string(60, '-') << '\n';
    for (int n : {100, 1000, 10000, 100000})
        benchmark(n);
    return 0;
}
