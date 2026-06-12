CXX      = g++
CXXFLAGS = -std=c++17 -O2 -Wall -Wextra

all: main benchmark

main: main.cpp ArbolAcademico.hpp
	$(CXX) $(CXXFLAGS) -o main main.cpp

benchmark: benchmark.cpp ArbolAcademico.hpp
	$(CXX) $(CXXFLAGS) -o benchmark benchmark.cpp

run_main: main
	./main

run_benchmark: benchmark
	./benchmark

clean:
	rm -f main benchmark

.PHONY: all clean run_main run_benchmark
