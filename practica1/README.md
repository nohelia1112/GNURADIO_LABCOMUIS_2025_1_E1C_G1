# Laboratorio de Comunicaciones

## Universidad Industrial de Santander

# Práctica 1: MEDICIONES DE POTENCIA Y FRECUENCIA

### Integrantes

- **NOHELIA AGUDELO CUERVO** - 2210413
- **FABIÁN CAMILO CHACÓN VARGAS** - 2214192

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha

7 de marzo de 2025

---

## Declaración de Originalidad y Responsabilidad

Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento.

Uso de IA: Se utilizó ChatGPT para reformular secciones del texto y verificar gramática, pero el contenido técnico fue desarrollado íntegramente por los autores.

---

## Contenido

### Resumen
Durante la práctica, se hizo uso de tres equipos de laboratorio: el osciloscopio R&S RTB2004, analizador de espectros R&S FPC1000 y radio USRP 2920. Así mismo, se hizo uso de software para simular señales llamado GNU Radio. 

**Palabras clave:** medición, potencia, frecuencia, transmisión, señales.

### Introducción
La teoría de muestreo es fundamental en el procesamiento de señales, ya que establece las bases para digitalizar y reconstruir señales analógicas sin perder información. El teorema de Nyquist, que exige una frecuencia de muestreo al menos el doble de la frecuencia máxima de la señal, es crucial para evitar el ‘aliasing’. Además, el uso de técnicas como la interpolación y el diezmado son esenciales; la primera aumenta la resolución de la señal, mientras que la segunda reduce la cantidad de datos, optimizando el procesamiento y almacenamiento.

Para aplicar y visualizar estos conceptos en la práctica, herramientas como GNU Radio, un osciloscopio como el R&S RTB2004 y un analizador de espectros R&S FPC1000 son fundamentales en un laboratorio de comunicaciones. GNU Radio es un software que permite simular señales de manera flexible y, gracias a su capacidad para integrarse con un analizador de espectros y un osciloscopio, posibilita observar en tiempo real tanto las características espectrales como las propiedades de la señal. Además, se incorpora un radio USRP 2920, que permite la transmisión y recepción de señales en tiempo real, ampliando las posibilidades de experimentación y análisis en el laboratorio.


### Procedimiento

#### Actividad 1: Revisión de Especificaciones de los Equipos

  Tras revisar los manuales de uso de los equipos de laboratorio, se consideraron las siguientes especificaciones como las más importantes:

**1.	 Osciloscopio R&S RTB2004**
<div style="text-align: center;">
    <img src="./2.Evidencias_Actividad1/Osciloscopio.png" alt="Osciloscopio" width="300" />
</div>

- ***Configuración de la forma de onda:***
  Las opciones que tiene este osciloscopio para configurar la forma de onda de las señales de entrada y salida son muchas, permitiendo así un mejor tratamiento según el análisis necesario. En su manual, explican desde cómo conectar y configurar sondas, hasta ajustar la configuración horizontal y vertical de las señales, y controlar la adquisición.

- ***Configuración del trigger:***
  Esta opción va muy de la mano con la anterior especificación, puesto que gracias al ‘trigger’, se pueden capturar partes de interés de las formas de onda para lograr así una obtención de datos más precisa.

- ***Análisis de la forma de onda:***
  Dentro de este apartado presentado en el manual, la especificación que más resalta es el zoom, ya que como su nombre lo infiere, amplía una parte de la forma de onda para conocer más detalles. Las formas de onda se muestran con una escala de tiempo más corta mientras que la escala vertical permanece sin cambios.

- ***Medidas:***
  Este osciloscopio proporciona muchos tipos de medidas para conocer características de tiempo y amplitud, y para contar pulsos y flancos. Por ejemplo: la frecuencia, ciclos de trabajo, top level, entre otros. Dichas mediciones se muestran en una línea debajo de la cuadrícula.

- ***Diseño de la pantalla:***
  En cuanto a algo diferente a las facilidades ya platicadas anteriormente de este osciloscopio, es innegable la comodidad del uso de su pantalla táctil y buena calidad, a comparación de otros osciloscopios que poseen los laboratorios de la Escuela de E3T en la UIS. Se puede mostrar más datos de interés en las señales tratadas.

**2.	Analizador de espectros R&S FPC1000**

| ![Spectrum_Analyzer](./2.Evidencias_Actividad1/Spectrum_Analyzer.png) | ![diapositiva](./2.Evidencias_Actividad1/diapo.png) |
|:---:|:---:|
| **Spectrum Analyzer** | **Diapositiva** |
  
  - ***Aplicación del analizador de espectro:***
  Junto con las mediciones básicas de frecuencia y dominio temporal, también se incorporan diversas mediciones avanzadas, como la del ancho de banda ocupado (OBW). Asimismo, se dispone de una amplia variedad de configuraciones y herramientas para ajustar y analizar mediciones espectrales.

  - ***Aplicación del receptor de espectro:***
  La aplicación del receptor mide el nivel de potencia de una frecuencia específica o de un conjunto de frecuencias personalizado.

  - ***Demodulación analógica:***
  Se demodulan señales moduladas en amplitud (AM) y frecuencia (FM), y muestra algunos aspectos de la señal modulada y demodulada.

  - ***Demodulación digital:***
  Se demodulan señales moduladas con esquemas de modulación por desplazamiento de amplitud (ASK) y de frecuencia (FSK), y muestra algunos aspectos de la señal modulada y demodulada.

 - ***Diseño de la pantalla:***
  Similar a lo explicado con el osciloscopio, es importante resaltar también la importancia del diseño y distribución de los datos de interés en las señales tratadas en la pantalla.

**3.	Radio USRP 2920**
<div style="text-align: center;">
    <img src="./2.Evidencias_Actividad1/USRP_2920.png" alt="USRP_2920" width="400" />
</div>

- ***Rango de frecuencia (frequency range):***
Se trata del rango de frecuencias por el cual el radio puede transmitir o recibir señales. Tanto para el transmisor como el receptor, dicho rango es de 50[M*Hz*] a 2.2 [G*Hz*].

- ***Potencia máxima de salida (Pout)***
Indica el nivel máximo de potencia que puede emitir el transmisor, lo cual es importante para garantizar que la señal pueda llegar al destino previsto con suficiente fuerza. Posee dos rangos: 50 [M*Hz*] a 1.2 [G*Hz*], para 50 [m*W*] a 100 [m*W*] (17 [dBm] a 20 [dBm]) y 1.2 [G*Hz*] a 2.2 [G*Hz*], para 30 [m*W*] a 70 [m*W*] (15 [dBm] a 18 [dBm]).

- ***Rango de ganancia***
Es fundamental para ajustar la intensidad de la señal a niveles óptimos, garantizando una comunicación clara y confiable entre el transmisor y el receptor. Para el primero, dicho rango es de 0 [dB] a 31 [dB], y el segundo, de 0 [dB] a 31.5 [dB].

-	***Ancho de banda máximo instantáneo en tiempo real***
Especifica el ancho de banda máximo que el dispositivo puede manejar en tiempo real, lo que es esencial para aplicaciones que requieren altas velocidades de datos o señales de banda ancha. Para un ancho de muestra de 16 bits, el ancho de banda máximo es de 20 [MHz] y para uno de 8 bits, de 40[MHz].

-	***Precisión de la frecuencia***
Se utiliza para garantizar que las señales transmitidas y recibidas estén exactamente en la frecuencia prevista. Tanto para el transmisor como el receptor, dicho valor es de 2.5 [ppm].

Entre medir una señal en el dominio del tiempo (vista con el osciloscopio) y en el dominio de la frecuencia (vista con el analizador de espectros),evidentemente, se tienen dos diferentes formas de visualizar lo que son los parámetros de la señal, como lo son la potencia y la frecuencia de la señal. Se puede observar que en el espectro la información se encuentra más condensada, lo que permite recuperar parte de esa información con menores pérdidas.

| ![Analizador_Sin](./2.Evidencias_Actividad1/Analizador_Sin.jpg) | ![sin_osciloscopio](./2.Evidencias_Actividad1/Sin_osciloscopio.jpg) |
|:---:|:---:|
| **Analizador de espectro** | **Osciloscopio** |

Teniendo en cuenta las especificaciones anteriores, se procedió a hallar la 
potencia de ruido ($P_N$) y calcular el piso de ruido normalizado ($NF$):

<div style="text-align: center;">
    <img src="./2.Evidencias_Actividad1/Noisefloor_radio.png" alt="Noisefloor_radio" width="350" />
</div>

Donde se puede observar que:

  $RBW = 300[Hz]$

  $P_Nref ≈ -100[dBm]$

A continuación, se realiza el cálculo del piso de ruido:

  $NF[dBm/Hz]  = P_Nref[dBm] - 10 log(\frac{RBW}{1 [Hz]})$

  $NF = -100-10log(\frac{300}{1})$

  $NF = -124,771 [dBm/Hz]$


#### Actividad 2: Simulación de Señales en GNU Radio


Comprender las bases de cómo procesa las señales un software como GNU Radio es fundamental para trazar un margen claro entre la teoría y lo que podemos observar en una simulación. En este contexto, exploraremos los bloques principales de un esquema de diseño del siguiente [flujograma](1.Flujo_grama/simple_flowgraph.grc):


- **Signal Source:** Define los  parametros de la señal como el muestreo tanto en tiempo como frecuencia , la forma de onda, la frecuencia, la amplitud, el offset, la fase y el tipo de dato.
- **Throttle:**  Regula la tasa de muestreo de la señal para evitar que el simulador consuma demasiados recursos del sistema.
- **QT GUI Time Sink:** Define el numero de puntos que representan la señal en el dominio del tiempo.
- **QT GUI Frequency Sink:** Responsable de realizar el cambio de dominio del tiempo a el dominio de la frecuencia,definir el ancho de banda de la respuesta en frecuencia y permitirnos visualizar la magnitud en el espectro.

Los tipos de señales "análogas" en el sistema son reales ***(float)*** y complejas ***(complex)*** donde para generar la componente compleja hace uso ***Filtro de Hilbert*** [[1]](#bibliografía) , [[2]](#bibliografía)

<div style="text-align: center;">
    <img src="./3.Evidencias_Actividad2/Transformada_hilbert.png" alt="USTransformada_hilbert" width="300" />
</div>

Donde $\hat{x}(t)$ es la Transformada de Hilbert de $x(t)$.

  <div style="text-align: center;">
    <img src="./6.ECUACIONES/1.integral.png" alt="USTransformada_hilbert" width="200" />
</div>

 La Transformada de Hilbert introduce un **desfase de $-90^\circ$** para las frecuencias positivas y un **desfase de $+90^\circ$** para las frecuencias negativas.

**Transformada de Hilbert como filtro:**
- Respuesta al impulso:

  $x(t) = \frac{1}{\pi t}$


- Respuesta en frecuencia:
<div style="text-align: center;">
    <img src="./6.ECUACIONES/2.respuesta.png" alt="USTransformada_hilbert" width="250" />
</div>
**Resolución en frecuencia**:

La resolucion en **GNURADIO** nos permite ver con mejor calidad la señal y poder realizar un analasis mas profundo de como trabajar con ella, esta dada por la siguiente expresion:
\[  
\text{Resolución en frecuencia} = \frac{f_s}{N}
 \]
Donde $f_s$ es el ***sample_rate*** , $N$ el numero de puntos de la ***trasnformada de fourier***. 

Es importante tener claro los conceptos de muestro,como el ***teorema de Nyquist*** [[3]](#bibliografía) , ya que podriamos tener alissing si estamos muestreando mal una señal y esto nos puede llevar a un analisis incongruente. A continuacion se van a mostrar imagenes de algunas señales con alliasing  
 
| ![Analizador_Sin](./3.Evidencias_Actividad2/ALIASSING_Cuadrado1024_ESPECTRO.png) | ![sin_osciloscopio](./3.Evidencias_Actividad2/ALIASSING_Sample_rate_y_FFT_1024_SIN_Ft.png) |
|:---:|:---:|
| **Onda cuadrada** | **Senosoidal** |

A simple vista no es observable( [Ver mas a detalle ](../3.Evidencias_Actividad2/ALIASSING_Sample_rate_y_FFT_1024_SIN_Ft.png) ), la frecuencia de muestreo para estos ejemplos fue de 1024 $Hz$ y la frecuencia de dichas señales es de 1 $KHz$ entonces por el teorema de Nyquist se conoce que estas señales fueron mal muestras. Este efecto genera cohecifientes en frecuencias no deseadas del especto cambiando y distribuyendo la potencia de la señal en la frecuencia de forma inadecuada.

La distribucion de la potencia de las señales en el dominio de la frecuencia dependen directamente de dos factores.

| ![Potencia de una señal](./6.ECUACIONES/potencia.png) | ![Transformada de fourier](./6.ECUACIONES/fourier.png) |
|:---:|:---:|
| **Potencia de una señal** | **Transformada de fourier** |

La ***$TF$ (trasnformada de fourier)*** la cual es la responsable de dar la forma del espectro y la distribucion de potencia en el dominio de la frecuencia y la ***potencia*** de la señal que es una caracteristica dependiente de la forma de onda de la señal en el tiempo o en la frecuencia.

Se ilustratan estos conceptos con unos ejemplos:

| ![Analizador_Sin](./3.Evidencias_Actividad2/P_SIN.png) | ![sin_osciloscopio](./3.Evidencias_Actividad2/Triangular_Compleja_Potencia.png) |
|:---:|:---:|
| **Potencia Seno** | **Potencia Triangular compleja** |

La potencia de una senosoidal es $P = \frac{A^2}{2}$ , esta potencia se divide en la cantidad de armonicos que observamos en el espectro en este solo son dos debio a la TF, por lo que puede comprobarse que  $10 \log{_{10}} \left( \frac{A^2}{2*2} \right)$.
Para el caso de la triangular su potencia es de $P = \frac{A^2}{3}$ esta potencia tiene que dividirse en todo el espectro la triangular
 <div style="text-align: center;">
    <img src="./3.Evidencias_Actividad2/image.png" alt="GNUConstante" width="300" />
    <p><b>Triangular real espectro</b></p>
</div>
Ccomo puede observase son muchos armonicos. Para calcular la potencia total de esta señal es necesario considerar un criterio para medir el ancho de banda y calcular la potencia en ese ancho.Sin embargo tambien es posible hacer un analisis analitico ya que al convertir una señal real añadiendo la transformada de Hilbert  desaparece la parte negativa del espectro y toda la energía queda concentrada en un solo lado de la frecuencia. Dicho de otro modo, la señal real, que antes era simétrica en frecuencia, se transforma en una señal “unilateral”, gracias a la componente en cuadratura.

#### Actividad 3: Transmisión y Medición de Señales con el USRP 2920


Lo primero que se debe hacer es configurar en GNU Radio el flujograma otorgado en la guía del informe para transmitir una señal a través del radio USRP 2920, deshabilitándose los bloques Channel Model, Throttle, UHD: USRP Sink, Virtual Sink. Después, se edita el valor de la frecuencia según se requiera en el bloque de frecuencia de muestreo (samp_rate). En cuanto al entorno físico, se debe conectar un cable ethernet para establecer la comunicación entre GNU Radio y el USRP, y para visualizar la señal, se conecta otro cable desde la terminal TX1 del USRP al analizador de espectro. Dentro del flujograma se puede encontrar uno de los parámetros clave que afectan la potencia de la señal transmitida. Se trata del bloque QT GUI Range, el cual permite variar la amplitud de la señal portadora en tiempo real. Este ajuste influye directamente en la potencia de transmisión, lo que se refleja en la visualización de la señal en el analizador de espectro.

<div style="text-align: center;">
    <img src="./4.Evidencias_Actividad3/qam_modulator.png" alt="GNUConstante" width="300" />
    <p><b>Esquema de como procesa la señal el radio</b></p>
</div>

Las medidas de interés para el presente laboratorio son parámetros clave como potencia, ancho de banda, piso de ruido y relación señal a ruido (SNR). Para medir el ancho de banda de la señal transmitida, se utilizan marcadores en el analizador de espectro. El Marcador 1 se coloca en el pico de la señal, mientras que los Marcadores 2 y 3 se ubican en los puntos donde la amplitud disminuye 3[dB] a cada lado respecto al pico, y es la diferencia en frecuencia entre estos dos puntos lo define el ancho de banda de la señal. Otro parámetro importante es la relación señal a ruido (SNR), la cual se calcula a partir de las mediciones de potencia de la señal y del ruido obtenidas con los marcadores del analizador de espectro. Haciendo uso de la fórmula:

$\text{SNR}{[\text{dB}]} = 10 \log{_{10}} \left( \frac{P_S}{P_N} \right) \quad \text{ó} \quad \text{SNR}_{[\text{dB}]} = P_s \, [\text{dB}] - P_n \, [\text{dB}]$

Donde $P_S$ es la potencia de la señal y $P_N$ la potencia de ruido, se determina la calidad de la señal en términos de su nivel respecto al ruido presente. Este cálculo es fundamental para evaluar el desempeño del sistema de transmisión y garantizar que la señal sea lo suficientemente robusta para su recepción.

##### Señales Alambricas

 **Caso 1. Señal constante**

<div style="text-align: center;">
    <img src="./4.Evidencias_Actividad3/Constante_SNR.png" alt="GNUConstante" width="300" />
    <p><b>Señal constante vista en GNU Radio</b></p>
</div>


| ![Analizador_Constante1](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/ConstanteSNR.png) | ![Analizador_Constante2](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/ConstanteSNR2.png)|
|:---:|:---:|
| **Potencia de la señal** | **Potencia de ruido** |

$SNR_{[dBm]} = 19.79[dBm] - (-39.38) [dBm]$

$SNR_{[dBm]} = 59.17[dBm]$

**Caso 2. Señal ventana**

<div style="text-align: center;">
    <img src="./4.Evidencias_Actividad3/Z_NS_Cajas_SNR.png" alt="GNUVentana" width="300" />
    <p><b>Señal ventana vista en GNU Radio</b></p>
</div>

| ![Analizador_Caja1](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/SNR1_1.png) | ![Analizador_Caja2](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/SNR1_2.png)|
|:---:|:---:|
| **Potencia de la señal** | **Potencia de ruido** |

$SNR_{[dB]} \approx 13.64*5[dBm] - (-48.43) [dBm]$

$SNR_{[dB]} \approx 116.63[dBm]$

 **Caso 3. Señal cosenoidal tipo complejo**

<div style="text-align: center;">
    <img src="./4.Evidencias_Actividad3/Coseno_Complejo_SNR.png" alt="GNUCos" width="300" />
    <p><b>Señal cosenoidal tipo complejo vista en GNU Radio</b></p>
</div>

| ![Analizador_Coseno1](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/SNR2_1.png) | ![Analizador_Coseno2](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/SNR2_2.png) |
|:---:|:---:|
| **Potencia de la señal** | **Potencia de ruido** |

$SNR_{[dBm]} \approx 18.8*2[dBm] - (-47.93) [dBm]$

$SNR_{[dBm]} \approx 85.53[dBm]$

De igual manera, se realizó el intento de estimar algunas de estas características utilizando un osciloscopio, ya que este instrumento permite visualizar la amplitud de la señal en el dominio del tiempo y en el dominio de la frecuencia


| ![Analizador_Coseno1](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/Osciloscopio_tiempo.PNG) | ![Analizador_Coseno2](./4.Evidencias_Actividad3/Capturas_Analizador_Osciloscopio/FT_Osciloscopio.jpg) |
|:---:|:---:|
| **Señal en el tiempo** | **Espectro** |

##### Señales inalambricas 

<div style="text-align: center;">
    <img src="./4.Evidencias_Actividad3/antena.jpg" alt="Analizadorantena" width="300" />
    <p><b>Medida del espectro electromagnetico </b></p>
</div>

Para poder recibir señales inalambricas hace falta una antena , conocer la frecuencia y BW donde se esta transmitiendo la señal que queremos analizar para ello es importante revisar el uso del espectro.[[ANE]](#bibliografía)

<div style="text-align: center;">
    <img src="./4.Evidencias_Actividad3/Anchodebanda.jpg" alt="Analizadorantena" width="300" />
    <p><b>Medida de ancho de banda</b></p>
</div>

Se realizo un muestreo de una señal de radio en los $95KHz$ , utilizando el método de ancho de banda de $x$  $dB$ consideramos un $x$ de $20dBm$ se hallo que el ancho de banda es de apoximadamente $Bw\approx 2,125MHz$


**Caso 1. Señal constante**

<div style="text-align: center;">
    <img src="./5.ANTENA/Constante.png" alt="GNUConstante" width="300" />
    <p><b>Señal constante vista en GNU Radio</b></p>
</div>


| ![Analizador_Constante1](./5.ANTENA/Antenta/ConstanteSNR2.png) | ![Analizador_Constante2](./5.ANTENA/Antenta/ConstanteSNR.png)|
|:---:|:---:|
| **Potencia de la señal** | **Potencia ruido** |

$SNR_{[dBm]} = -44.43[dBm] - (-115.45) [dBm]$

$SNR_{[dBm]} = 71.02[dBm]$


**Caso 2. Señal triangular**
<div style="text-align: center;">
    <img src="./5.ANTENA/Triangular.png" alt="GNUConstante" width="300" />
    <p><b>Señal constante vista en GNU Radio</b></p>
</div>


| ![Analizador_Constante1](./5.ANTENA/Antenta/Triangular_mejorspan_SNR.png) | ![Analizador_Constante2](./5.ANTENA/Antenta/Triangular_mejorspan_SNR2.png)|
|:---:|:---:|
| **Potencia de la señal** | **Potencia de ruido** |

Se nota una gran diferencia entre las potencias en medios alambricos y inalambricos,de  apesar de que se manda la misma señal en los medios inalimbricos la potencia es mucho menor. ( [Ver video ](./5.ANTENA/Evidencia_antena_video.mp4) ) 

#### Actividad 4: Análisis de Resultados y Conclusiones

Para lograr una comunicación efectiva, es necesario equilibrar la potencia con aspectos como las interferencias causadas por el mal estado del medio de transmisión o la saturación de la señal debido a una potencia excesiva. El piso de ruido juega un papel crucial, ya que establece el límite mínimo (inferior) para la detección de señales. Una señal solo puede ser identificada si su potencia supera este umbral, de lo contrario, se confunde con el ruido propio del ambiente. Si la señal es muy débil y se aproxima al piso de ruido, la relación señal-ruido será baja, dificultando su detección. Para solucionar este problema, se pueden emplear receptores con mayor sensibilidad o técnicas de mejora que permitan distinguir la señal del ruido, lo que resalta la importancia de considerar tanto el entorno como las capacidades de los equipos utilizados.

Al hacer los cálculos mencionados en la actividad 3 de la relación señal-ruido, durante esta cuarta fase del laboratorio se pudo encontrar un error humano y común entre los estudiantes. Se trata del olvido de la distribución de potencia entre todos los armónicos de las señales captadas, por lo que de los tres casos mostrados, solo para la señal constante habría un valor correcto de $P_s$. A pesar de ello, la implementación de la fórmula de SNR fue correcta.
  
Por otro lado, las limitaciones de los equipos, como el ancho de banda ya mencionado anteriormente del radio USRP 2920, impone restricciones en la cantidad de información que puede transmitirse o recibirse por unidad de tiempo y la imposibilidad de que este radio sea de utilidad en aplicaciones de banda ancha. Además, en entornos con alto nivel de ruido, las mediciones de una señal pueden mejorarse mediante el uso de filtros adaptados a las necesidades específicas y, en algunos casos, implementando blindajes para proteger la señal del ruido externo. Estas estrategias son esenciales para garantizar la precisión y fiabilidad de las mediciones en condiciones adversas para diferentes aplicaciones reales. Un ejemplo cotidiano es la radio FM, que opera en un ancho de banda de 87.5[MHz] a 108 [MHz], o incluso la radioastronomía, que abarca desde 300[MHz] hasta 300[GHz], dividiéndose en bandas como UHF, SHF y EHF.

---
## Conclusiones

  - La potencia de la señal es un factor clave en la calidad de la comunicación, aunque no es el único elemento determinante. Es necesario que esté en equilibrio junto con interferencias y saturaciones.
  
  - El piso de ruido define el umbral mínimo para la detección de señales, determinando si una señal puede ser identificada o si se perderá entre el ruido ambiental. Dicho umbral fue calculado y tiene como valor $-124,771 [dBm/Hz]$. Se resalta la importancia de evaluar tanto las condiciones del entorno como las características del equipo utilizado para garantizar una detección precisa.
  
 - Las restricciones en el ancho de banda pueden dificultar la detección de señales de alta frecuencia, mientras que las limitaciones en precisión pueden afectar la exactitud de las mediciones. Para mitigar estos inconvenientes, es fundamental elegir el equipo adecuado para cada aplicación y realizar su respectiva configuración según los requerimientos.
 

---
## Referencias

### Bibliografía

- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. p. 95-100,132. Chapter 2.6 In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)

- [R&S, 2017] Rohde & Schwarz GmbH & Co. R&S®RTB2000 Digital Oscilloscope User Manual. 2017. p. 34-108.[Abrir documento en el repositorio][Abrir manual del osciloscopio](../Equipos_de_laboratorio/Oscilloscope_RTB_UserManual_en.pdf).

- [R&S, 2017] Rohde & Schwarz GmbH & Co. R&S®FPC1000 Spectrum Analyzer User Manual. 2017. p. 36-148.[Abrir manual del Analizador de espectros](../Equipos_de_laboratorio/Spectrum_Analyzer_FPC_XXX_ANL-EN.pdf)

- [NI, 2025] NATIONAL INSTRUMENTS CORP. USRP-2920 Specifications. 2025. p. 3-148.[Abrir manual del Radio](../Equipos_de_laboratorio/usrp-2920_specifications.pdf)


### Recursos Digitales
- Wikipedia. (s.f.). *Transformada de Hilbert*. Recuperado de https://es.wikipedia.org/wiki/Transformada_de_Hilbert
- Wikipedia. (s.f.). Teorema de muestreo de Nyquist-Shannon. Recuperado de https://es.wikipedia.org/wiki/Teorema_de_muestreo_de_Nyquist-Shannon   
- Academia Lab. (s.f.). *Transformada de Hilbert*. Recuperado de https://academia-lab.com/enciclopedia/transformada-de-hilbert/  
- Reyes, Ó. (s.f.). *COMMUNICATION SYSTEMS. Lesson 1-3: The dB in Communications*. Recuperado de https://lms.uis.edu.co/ava/pluginfile.php/271940/mod_folder/content/0/Lesson_1_3_The_dB_in_communications.pdf
- NATIONAL INSTRUMENTS CORP. (2015). *How to Measure the Noise Floor of Your Signal Analyzer*. Recuperado de https://www.youtube.com/watch?v=ujce9AzrqdY
- International Telecommunication Union (ITU), Spectrum Monitoring – Spectrum Occupancy Measurements, ITU-R Recommendation SM.328-11, May 2006. [Online]. Available: https://www.itu.int/rec/R-REC-SM.328-11-200605-I/en. [Accessed: (fecha de acceso)].
- Agencia Nacional del Espectro (ANE), *CNABF Técnico*, [Online]. Available: [https://portalespectro.ane.gov.co/Style%20Library/ane_master/cnabf-tecnico.aspx](https://portalespectro.ane.gov.co/Style%20Library/ane_master/cnabf-tecnico.aspx). [Accessed: Oct. 10, 2023].

### Artículos de Interés

- Carrick, J. (2011). *Design and Application of a Hilbert Transformer in a Digital Receiver*. [Abrir documento en el repositorio](7.ANEXOS/DESIGN_AND_APPLICATION_OF_A_HILBERT_TRANSFORMER_IN_A_DIGITAL_RECEIVER.pdf).  
- Hasegawa, T., & Sugiura, H. (2022). *Filtered Integration Rules for Finite Weighted Hilbert Transforms*. [Abrir documento en el repositorio](7.ANEXOS/Filtered_integration_rules_for_finite_weighted_Hilbert.pdf).  
  
---

Volver al [INICIO](#laboratorio-de-comunicaciones)
