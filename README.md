# [ORGA]Proyecto_G3
<h1 align="center">Proyecto de Organización Computacional</h1>

## Printer 

<p align="center">
    <img src="Documentacion\IMG\Printer.png">
</p>

## RAM

<p align="center">
    <img src="Documentacion\IMG\Memoria RAM.jpeg">
</p>

<p align="center">
    <img src="Documentacion\IMG\Memoria-RAM-4x5-1.jpg">
</p>
<p align="center">
    <img src="Documentacion\IMG\Memoria-RAM-4x5-2.jpg">
</p>

<h2 align="center">Grupo #3</h2>

<div align="center"> 🏛 Universidad San Carlos de Guatemala</div>
<div align="center">
💻 Laboratorio de Organizacion Computacional 
</div>
<div align="center"> 📆 Primer Semestre 2024</div>
<div align="center">🏫​ Sección B</div>
<div align="center">
🙍‍♀️ Rocío Samaí López Vasquez - 201709035 
</div>

<div align="center">
🙍‍♂️ Oswaldo Antonio Choc Cuteres - 201901844
</div>

<div align="center">
🙍‍♂️ Jencer Hamilton Hernández Alonzo - 202002141
</div>

<div align="center">
🙍‍♂️ Cristian Raúl Vega Rodríguez - 202010942
</div>

<div align="center">
🙍‍♂️ Javier Andrés Monjes Solórzano -  202100081
</div>

<div align="center">
🙍‍♂️ Angel Isaias Mendoza Martinez - 202180003
</div>

<div align="center">
🙍‍♀️ Estephanie Alejandra Ruiz Perez - 202201318
</div>

<div align="center">
🙍‍♂️ Edin Rafael Santizo Barrera - 202202072
</div>

<div align="center">
🙍‍♂️ Juan Pascual Itzep Coguox - 202202161
</div>

<div align="center">
🙍‍♂️ Diego Andrés Dubón Samayoa  - 202202429
</div>

<div align="center">
🙍‍♂️ Juan José Almengor Tizol - 202212209
</div>


<!-- Resumen -->
## Resumen

El proyecto consistía en desarrollar un plotter (impresora gráfica) controlado por una computadora a través de una conexión serial (puerto paralelo o serial). El plotter debía ser capaz de replicar dibujos realizados en una aplicación de escritorio en una hoja de papel bond, utilizando un lápiz o similar como medio de impresión.

### Requerimientos principales:

- Aplicación de escritorio:

    *  Interfaz gráfica con lienzo para dibujar en una matriz de 3x3 (estilo PixelArt)
    * Opciones: Abrir, Editar, Guardar, Guardar Como, Imprimir
Figuras predefinidas
Formato de archivo ".orga"
Código fuente alojado en un repositorio Git (GitLab)
- Interfaz PC:

    * Conexión serial a través del puerto paralelo LPT1 o puerto serial
Envío y recepción de datos seriales hacia un Arduino
- Transmisión de datos:

    * Envío de datos desde la PC al controlador de motores del plotter
- Impresión:

    * Almacenar 3 coordenadas a imprimir en una matriz de Flip-Flops (simulando RAM)
Imprimir las 3 coordenadas al presionar "Enter"
Regresar al punto de origen después de imprimir
Proceso automático para imprimir un lienzo completo
- Coordenadas X y Y:

    * Indicadores de las coordenadas X y Y del cabezal de impresión
    * Mostrar en la aplicación y externamente mediante displays
- Área de impresión:

    * Hoja de papel bond tamaño carta
    * Indicadores en las esquinas (sensores de color)
    * LED azul si todos los sensores están alineados correctamente
    * LED amarillo si algún sensor está desalineado
- Alineación:

    * 4 sensores de color para detectar la alineación del área de impresión
Indicadores visuales (LED verde y rojo) para cada sensor
Integrados permitidos:

Se proporciona una lista de circuitos integrados y compuertas lógicas que nos fueron permitidas para la realización del proyecto.



## 📖 Documentación
Para comprender de mejor manera el funcionamiento del proyecto puede dirigirse a lo siguiente información:
    <ul>
       <li><a href="">:point_right:Planteamiento de proyecto</a></li>
        <li><a href="Documentacion\PROYECTO_1_ORGA.pdf" target="_blank">:point_right:Documentacion Ensayo</a></li>
    </ul>
