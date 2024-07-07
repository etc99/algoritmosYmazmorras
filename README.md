# ***Algoritmos y Mazmorras***
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


+ ## ***Autora:***
    + Elsa Tolín Carrasco
+ ## ***Tutores:***
    + Jesús Alonso Abad
    + José Manuel Galán Ordax

## Descripción
La generación procedimental, es la técnica que a través de algoritmos, permite crear contenido para videojuegos de forma autónoma o de la mano de un diseñador. 

En este trabajo de fin de grado, se van a explorar distintos algoritmos para poder probar esta técnica, de forma que se obtengan mapas navegables como lo serían en un videojuego. Estos mapas van a tener la forma de un laberinto y van a ser generados en un servidor, replicando la arquitectura cliente-servidor que se tendría en un estudio de videojuegos real.
Se han adaptado los siguientes algoritmos de generación procedimental:
- Prim
- Depth First Search-DFS
- Autómata celular
- Eller
- Kruskal
- Teselación
- Aldous Broder
- Árbol Binario

## Keywords

![C#](https://img.shields.io/badge/C_sharp-87F5F5?style=for-the-badge&logo=c&logoColor=black&labelColor=D8D8D8)
![Unity](https://img.shields.io/badge/Unity-87F5F5?style=for-the-badge&logo=unity&logoColor=black&labelColor=D8D8D8)
![Videojuegos](https://img.shields.io/badge/Videojuegos-87F5F5?style=for-the-badge&logo=unity&logoColor=black&labelColor=D8D8D8)
![Python](https://img.shields.io/badge/python-87F5F5?style=for-the-badge&logo=p&logoColor=black&labelColor=D8D8D8)
![Docker](https://img.shields.io/badge/docker-87F5F5?style=for-the-badge&logo=p&logoColor=black&labelColor=D8D8D8)
![ProceduralGeneration](https://img.shields.io/badge/procedural_generation-87F5F5?style=for-the-badge&logo=p&logoColor=black&labelColor=D8D8D8)


## Tecnologías Utilizadas

- **Unity**: Versión 2021.3.25f1
- **Lenguajes de Programación**: C# y Python
- **Entornos de Desarrollo**: Visual Studio 2019, Visual Studio Code

## Manual

La aplicación funcional se encuentra en la carpeta de Segunda Fase, es esta carpeta la que almacena todo lo necesario para continuar desarrollando este proyecto.

El código del proyecto se divide entre dos partes principales una para la aplicación de Unity, incluida en /AlgoritmosYMazmorras y la parte del servidor de laberintos contenida en /Mazmorras.

# Requisitos de la aplicación

Las dependencias necesarias para lanzar la aplicación se encuentran dentro del fichero `requirements.txt`. Para instalarlas se introduce el siguiente comando:
```bash
pip install -r requirements.txt
```

# Arrancar el servidor

Para poder arrancar el servidor es necesario tener instalado docker previamente, para más información consultar la carpeta /Documentación.
Desde la terminal de la máquina, hay que ubicarla en la carpeta de desarrollo /Mazmorras y escribir el siguiente comando:
```bash
docker compose up
```
Tras esto se necesita arrancar el ejecutable 'AlgoritmosYMazmorras'

# Parar el servidor

Para parar el servidor se puede hacer desde la terminal con Ctrl+C, pero para eliminar el contenedor por completo se necesita ejecutar el siguiente comando:
```bash
docker compose down
```
