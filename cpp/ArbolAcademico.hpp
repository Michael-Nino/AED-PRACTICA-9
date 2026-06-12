// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

#pragma once

#include <string>
#include <vector>
#include <queue>
#include <memory>
#include <optional>
#include <stdexcept>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <numeric>

namespace una_puno {

enum class EstadoAcademico {
    ACTIVO, EGRESADO, RETIRADO, SUSPENDIDO
};

inline std::string estadoStr(EstadoAcademico e) {
    switch(e) {
        case EstadoAcademico::ACTIVO: return "ACTIVO";
        case EstadoAcademico::EGRESADO: return "EGRESADO";
        case EstadoAcademico::RETIRADO: return "RETIRADO";
        case EstadoAcademico::SUSPENDIDO: return "SUSPENDIDO";
        default: return "DESCONOCIDO";
    }
}

struct Estudiante {
    int codigo;
    std::string nombre;
    std::string escuela;
    float ppa;
    int creditos;
    EstadoAcademico estado;
    std::string semestre_ingreso;

    Estudiante(int cod, std::string nom, std::string esc,
               float pp, int cred, EstadoAcademico est, std::string sem)
        : codigo(cod), nombre(std::move(nom)), escuela(std::move(esc)),
          ppa(pp), creditos(cred), estado(est),
          semestre_ingreso(std::move(sem))
    {
        if (cod < 10000000 || cod > 29999999)
            throw std::invalid_argument("Codigo invalido: " + std::to_string(cod));
        if (pp < 0.0f || pp > 20.0f)
            throw std::invalid_argument("PPA fuera de rango [0,20]");
    }

    void print() const {
        std::cout << std::left
                  << std::setw(10) << codigo
                  << std::setw(35) << nombre
                  << std::setw(20) << escuela
                  << "PPA:" << std::fixed << std::setprecision(1) << ppa
                  << " " << estadoStr(estado) << '\n';
    }
};

struct NodoBST {
    Estudiante dato;
    std::unique_ptr<NodoBST> izquierdo;
    std::unique_ptr<NodoBST> derecho;

    explicit NodoBST(Estudiante e)
        : dato(std::move(e)), izquierdo(nullptr), derecho(nullptr) {}
};

class ArbolAcademico {
public:
    ArbolAcademico() = default;

    void insertar(Estudiante e) {
        insertar_(raiz, std::move(e));
    }

    std::optional<Estudiante> buscar(int codigo) const {
        const NodoBST* nodo = buscar_(raiz.get(), codigo);
        if (nodo) return nodo->dato;
        return std::nullopt;
    }

    void eliminar(int codigo) {
        if (!buscar(codigo))
            throw std::runtime_error("Codigo no encontrado: " + std::to_string(codigo));
        raiz = eliminar_(std::move(raiz), codigo);
    }

    std::vector<Estudiante> inOrder() const {
        std::vector<Estudiante> resultado;
        inOrder_(raiz.get(), resultado);
        return resultado;
    }

    std::vector<Estudiante> preOrder() const {
        std::vector<Estudiante> resultado;
        preOrder_(raiz.get(), resultado);
        return resultado;
    }

    std::vector<Estudiante> postOrder() const {
        std::vector<Estudiante> resultado;
        postOrder_(raiz.get(), resultado);
        return resultado;
    }

    std::vector<Estudiante> bfs() const {
        std::vector<Estudiante> resultado;
        if (!raiz) return resultado;
        std::queue<const NodoBST*> cola;
        cola.push(raiz.get());
        while (!cola.empty()) {
            const NodoBST* curr = cola.front(); cola.pop();
            resultado.push_back(curr->dato);
            if (curr->izquierdo) cola.push(curr->izquierdo.get());
            if (curr->derecho) cola.push(curr->derecho.get());
        }
        return resultado;
    }

    int altura() const { return altura_(raiz.get()); }

    bool estaVacio() const { return raiz == nullptr; }

    std::vector<Estudiante> porRangoPPA(float ppa_min, float ppa_max = 20.0f) const {
        auto todos = inOrder();
        std::vector<Estudiante> resultado;
        std::copy_if(todos.begin(), todos.end(),
                     std::back_inserter(resultado),
                     [ppa_min, ppa_max](const Estudiante& e){
                         return e.ppa >= ppa_min && e.ppa <= ppa_max;
                     });
        return resultado;
    }

    void estadisticas() const {
        auto todos = inOrder();
        if (todos.empty()) { std::cout << "Arbol vacio\n"; return; }
        float suma = 0.0f, mn = 20.0f, mx = 0.0f;
        int activos = 0;
        for (const auto& e : todos) {
            suma += e.ppa;
            if (e.ppa < mn) mn = e.ppa;
            if (e.ppa > mx) mx = e.ppa;
            if (e.estado == EstadoAcademico::ACTIVO) activos++;
        }
        std::cout << std::fixed << std::setprecision(2)
                  << "  Total nodos    : " << todos.size() << '\n'
                  << "  Altura         : " << altura() << '\n'
                  << "  PPA promedio   : " << suma/todos.size() << '\n'
                  << "  PPA minimo     : " << mn << '\n'
                  << "  PPA maximo     : " << mx << '\n'
                  << "  Activos        : " << activos << '\n';
    }

    void imprimirArbol() const {
        std::cout << "\n-- Estructura del BST --\n";
        imprimir_(raiz.get(), "", false);
    }

    std::optional<Estudiante> maximo() const {
        if (!raiz) return std::nullopt;
        const NodoBST* nodo = raiz.get();
        while (nodo->derecho) nodo = nodo->derecho.get();
        return nodo->dato;
    }

    std::vector<Estudiante> buscarRangoCodigo(int cod_min, int cod_max) const {
        std::vector<Estudiante> resultado;
        buscarRango_(raiz.get(), cod_min, cod_max, resultado);
        return resultado;
    }

private:
    std::unique_ptr<NodoBST> raiz;

    void insertar_(std::unique_ptr<NodoBST>& nodo, Estudiante e) {
        if (!nodo) {
            nodo = std::make_unique<NodoBST>(std::move(e));
            return;
        }
        if (e.codigo < nodo->dato.codigo)
            insertar_(nodo->izquierdo, std::move(e));
        else if (e.codigo > nodo->dato.codigo)
            insertar_(nodo->derecho, std::move(e));
        else
            throw std::runtime_error("Codigo duplicado: " + std::to_string(e.codigo));
    }

    const NodoBST* buscar_(const NodoBST* n, int cod) const {
        if (!n || n->dato.codigo == cod) return n;
        if (cod < n->dato.codigo)
            return buscar_(n->izquierdo.get(), cod);
        return buscar_(n->derecho.get(), cod);
    }

    std::unique_ptr<NodoBST> eliminar_(std::unique_ptr<NodoBST> nodo, int cod) {
        if (!nodo) return nullptr;
        if (cod < nodo->dato.codigo)
            nodo->izquierdo = eliminar_(std::move(nodo->izquierdo), cod);
        else if (cod > nodo->dato.codigo)
            nodo->derecho = eliminar_(std::move(nodo->derecho), cod);
        else {
            if (!nodo->izquierdo)
                return std::move(nodo->derecho);
            if (!nodo->derecho)
                return std::move(nodo->izquierdo);
            NodoBST* suc = minimo_(nodo->derecho.get());
            nodo->dato = suc->dato;
            nodo->derecho = eliminar_(std::move(nodo->derecho), suc->dato.codigo);
        }
        return nodo;
    }

    NodoBST* minimo_(NodoBST* n) const {
        while (n->izquierdo) n = n->izquierdo.get();
        return n;
    }

    void inOrder_(const NodoBST* n, std::vector<Estudiante>& r) const {
        if (!n) return;
        inOrder_(n->izquierdo.get(), r);
        r.push_back(n->dato);
        inOrder_(n->derecho.get(), r);
    }

    void preOrder_(const NodoBST* n, std::vector<Estudiante>& r) const {
        if (!n) return;
        r.push_back(n->dato);
        preOrder_(n->izquierdo.get(), r);
        preOrder_(n->derecho.get(), r);
    }

    void postOrder_(const NodoBST* n, std::vector<Estudiante>& r) const {
        if (!n) return;
        postOrder_(n->izquierdo.get(), r);
        postOrder_(n->derecho.get(), r);
        r.push_back(n->dato);
    }

    int altura_(const NodoBST* n) const {
        if (!n) return -1;
        return 1 + std::max(altura_(n->izquierdo.get()), altura_(n->derecho.get()));
    }

    void imprimir_(const NodoBST* n, std::string prefix, bool isLeft) const {
        if (!n) return;
        std::string conector = isLeft ? "+-- " : "`-- ";
        std::cout << prefix << conector
                  << n->dato.codigo << " [PPA:"
                  << std::fixed << std::setprecision(1)
                  << n->dato.ppa << "]\n";
        std::string ext = isLeft ? "|   " : "    ";
        imprimir_(n->izquierdo.get(), prefix + ext, true);
        imprimir_(n->derecho.get(), prefix + ext, false);
    }

    void buscarRango_(const NodoBST* n, int min_val, int max_val,
                      std::vector<Estudiante>& res) const {
        if (!n) return;
        if (min_val < n->dato.codigo)
            buscarRango_(n->izquierdo.get(), min_val, max_val, res);
        if (min_val <= n->dato.codigo && n->dato.codigo <= max_val)
            res.push_back(n->dato);
        if (max_val > n->dato.codigo)
            buscarRango_(n->derecho.get(), min_val, max_val, res);
    }
};

} // namespace una_puno
