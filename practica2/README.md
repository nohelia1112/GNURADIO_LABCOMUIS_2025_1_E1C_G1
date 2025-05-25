# Laboratorio de Comunicaciones

## Universidad Industrial de Santander
# Práctica 2. MODELO DE CANAL
### Integrantes

- **NOHELIA AGUDELO CUERVO** - 2210413
- **FABIÁN CAMILO CHACÓN VARGAS** - 2214192
  
Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha

 de abril de 2025

---

## Declaración de Originalidad y Responsabilidad

Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento.

Uso de IA: Se utilizó ChatGPT para reformular secciones del texto y verificar gramática, pero el contenido técnico fue desarrollado íntegramente por los autores.

---
## Contenido
### Resumen
Este laboratorio simula fenómenos de canal con GNU Radio para analizar cómo afectan la transmisión de señales. Se exploran el uso de filtros para trabajar con problemas de canal comunes como distorsiones ,atenuación, el desvanecimiento, el retardo y la dispersión. Usando el osciloscopio y el analizador de espectro, se observa el impacto de estos fenómenos en el tiempo y la frecuencia. Además, se evalúa cómo las imperfecciones del canal influyen en la conversión de frecuencia y la integridad de la señal. El objetivo es entender la importancia de los efectos del canal al diseñar sistemas de comunicación.

**Palabras clave:**
### Introducción
> [!NOTE]
> Revisar al culminar las actividades  y borrar objetivos.

## Objetivos
- Observar cómo el canal puede afectar la calidad de la señal transmitida y cómo  mitigar sus efectos.
- Evaluar aspectos clave como la relación señal-ruido y la eficiencia en la transmisión de datos.

Este enfoque permitirá no solo verificar la teoría, sino también desarrollar habilidades prácticas en el manejo de equipos de laboratorio, como equipos de medición (USRP 2920, osciloscopio R&S RTB2004 y analizador de espectros R&S FPC1000).

---

## Materiales y Equipos

- **USRP 2920:** Radio definido por software.
- **Osciloscopio R&S RTB2004:** Para visualización de señales en el dominio del tiempo y la frecuencia.
- **Analizador de Espectros R&S FPC1000:** Para mediciones en el dominio de la frecuencia.
- **Computador con GNU Radio:** Para simulación y generación de señales usando el USRP 2920.
- **Cables y conectores:** Para interconexión de equipos.
- **Audífonos y micrófono** (opcional, debe traerlo cada grupo)

### Ajustes preliminares

- En el [flujograma](filters_flowgraph.grc) propuesto para esta práctica, se incluye un bloque "Wav File Source". **Antes** de ejecutar el flujograma, seleccione un archivo WAV para ser usado por este bloque. Algunos archivos WAV de ejemplo los puede encontrar en: [LabComUIS/samples/](../../samples/) 
- Tenga en cuenta que existen instrumentos de visualización en dominio tiempo y frecuencia tanto para la señal ANTES como DESPUÉS del filtro.
---
### PROCEDIMIENTO:


## Actividad 1: Actividades de simulación de canal en GNU Radio

### Objetivo

Familiarizarse con algunos fenómenos de canal en un ambiente simulado.

### Procedimiento

**Simulación**
   - Verificar equipos y elementos a utilizar (revisar manuales de ser necesario)
   - Cargar el flujograma: [filters_flowgraph.grc](filters_flowgraph.grc).
   - Configurar siempre la frecuencia de muestreo (`samp_rate`) en $25e6/2^n$ Hz`, donde $n$ es un número entero mayor a 2.
   - Genere diferentes señales y observe el efecto de variar las frecuencias de corte del filtro.
   - Analice el efecto del ruido en el dominio del tiempo y la frecuencia para al menos dos formas de onda distintas.
   - Muestre con un ejemplo gráfico el umbral de máximo de ruido ante el cual considera que es posible recuperar cada forma de onda utilizando únicamente filtrado.

### Preguntas Orientadoras

- ¿Cuál es el efecto de filtrar las frecuencias altas de una señal?

La consecuencia dependera directamente de las caracteristicas de la señal, su frecuencia , su espectro y de los efectos de canal.

Desglosando de lo mencionado previamente en software con señales ciclicas podemos observar siguiente

 **Caso 1. Triangular con filtro cerca de los coeficientes espectrales**

| ![Analizador_Constante1](./2.Actividad%201%20GNURADIO/Triangular_filtrada.png/) | ![Analizador_Constante2](./2.Actividad%201%20GNURADIO/Triangular_E_filtrada.png)|
|:---:|:---:|
| **Señal Filtrada** | **Espectro filtrado** |

 **Caso 2. Triangular con filtro que borra los coeficientes espectales**
| ![Analizador_Constante3](./2.Actividad%201%20GNURADIO/Triangular_Highfrec_filtrada.png/) | ![Analizador_Constante2](./2.Actividad%201%20GNURADIO/Triangular_E_Highfrec_filtrada.png)|
|:---:|:---:|
| **Señal Filtrada** | **Espectro filtrado** |


Al filtrar las frecuencias altas de una señal es muy importante considerar su espectro ya que hay coeficientes de la serie de fourier de la señal que tienen mas potencia que otros, como resultado esos coeficientes son los que mas llevan informacion de la forma de la señal y al eliminarlos por consecuencia se logra observar un impacto radical en su forma de onda. Como se observa en el caso 2.

- ¿Qué sucede al filtrar muy cerca de la frecuencia fundamental de la señal?

Al filtrar cerca de frecuencias fundamentales se puede observar atenuaciones en la potencia de la señal ya que el filtro no es ideal por lo que tendra una pendiente asociada y de esa forma conseguira una atenuacion en la señal en dicha pendiente. Esto se observar en el caso 1 donde se ve una disminucion en potencia en el tiempo del 28 % de la señal original Amplitud : 0.25 ; Señal filtrada : 0.18 

- ¿Cuál es el efecto de filtrar las frecuencias bajas de una señal?

Es analogo a lo mencionado con el caso de las frecuencias altas. Aunque puede ser util ya que la mayoria de ruido producido en los dispositivos como el ruido termico, ruido flicker se producen a bajas frecuencias.

- ¿Qué ocurre al eliminar armónicos de una señal?

Al eliminar los coeficientes o armonicos principales de la señal se pierde la forma de onda y gran parte de la potencia de la señal.

- ¿Qué efecto tiene la desviación de frecuencia en la señal recibida? ¿Qué efecto(s) produce el filtro cuando la señal recibida se ve afectada por desviación de frecuencia?


<div style="text-align: center;">
    <img src="./2.Actividad 1 GNURADIO/Desviacion.png" alt="GNUConstante" width="300" />
    <p><b>Desviacion de frecuencia</b></p>
</div>

**Efecto de desviacion estandar**
| ![Analizador_Constante3](./2.Actividad%201%20GNURADIO/Efectodesviacion%20de%20frecuencia_normal.png/) | ![Analizador_Constante2](./2.Actividad%201%20GNURADIO/Efectodesviacion%20de%20frecuencia.png)|
|:---:|:---:|
| **Espectro** | **Espectro con desviacion de frecuencia** |

La desviacion de frecuencia desplaza los componentes espectrales en la frecuencia ensanchando el espectro, se  desplaza kf en direccion contraria a la frecuencia 0.

- ¿Cómo cuantificar la degradación de la señal al aumentar los niveles de ruido?
Mediante la relacion señal a ruido SNR ya que esta medida es la relacion directa en cuanto se ve afectada la amplitud de señal respecto el ruido de la misma
- ¿Cómo se puede mejorar la relación señal a ruido en una señal?

Utilizando filtros muy cerca de los armonicos de la señal para obtener el menor ruido posible y mejorar la relacion SNR de la señal

<table>
<tr>
<td align="center">
  <img src="./2.Actividad 1 GNURADIO/Triangularconruido.png" width="400"><br><strong>Ruido en el tiempo</strong>
</td>
<td align="center">
  <img src="./2.Actividad 1 GNURADIO/Triangularconruido_E.png" width="400"><br><strong>Ruido en el espectro</strong>
</td>
</tr>
</table>
Se puede observar que con una potencia del ruido del 50% de la amplitud de la señal transmitida aun puede recuperarse la señal original.

- ¿Cómo podría cuantificar la calidad de la señal recibida? Considere el caso de señales analógicas y digitales.

La calidad de una señal recibida se cuantifica de forma distinta según sea analógica o digital. En señales analógicas, se considera viable si la relación señal a ruido (SNR) es suficientemente alta, generalmente superior a 20 dB, lo que indica que la información útil predomina sobre el ruido; también pueden evaluarse métricas como SINAD o SINR si hay distorsión o interferencia. En señales digitales, la viabilidad depende principalmente de la tasa de error de bit (BER): una señal es confiable si la BER es lo bastante baja, típicamente menor a 10⁻³ o incluso 10⁻⁶ según el sistema, lo cual garantiza una recepción correcta de los datos.


 **Contraste entre SNR y BER**

<table>
<tr>
<td align="center">
  <img src="./2.Actividad 1 GNURADIO/SNR.png" width="400"><br><strong>Relacion señal a ruido</strong>
</td>
<td align="center">
  <img src="./2.Actividad 1 GNURADIO/BER2.png" width="300"><br><strong>BER VS SNR </strong>
</td>
</tr>
</table>




---

## Actividad 2: Fenómenos de canal en el osciloscopio

### Objetivo

Familiarizarse con los fenómenos de un canal alámbrico real en el dominio del tiempo.

### Procedimiento

1. **Configurar el USRP 2920:**
   - Configurar el flujograma [filters_flowgraph.grc](filters_flowgraph.grc) en GNU Radio para transmitir una señal a través del USRP.
   - Habilitar o deshabilitar los bloques correspondientes (`Channel Model`, `Throttle`, `UHD: USRP Sink`, `UHD: USRP Source`, `Virtual Sink`). Para esto, seleccione el bloque deseado y presione **E** (enable) o **D** (disable), según corresponda.
   - Configurar siempre la frecuencia de muestreo (`samp_rate`) en $25e6/2^n$ Hz`, donde $n$ es un número entero mayor a 2. Verifique que la frecuencia de muestreo durante la ejecución, sea la misma que ha configurado en el flujograma.

2. **Configurar el osciloscopio:**
   - Encender, configurar y conectar el osciloscopio a la salida del USRP 2920 usando diferentes cables coaxiales, y ajustando los parámetros necesarios para evidenciar los fenómenos de canal analizados en la Actividad 1.
   - Variar la frecuencia de portadora del USRP entre 50 MHz hasta 500 MHz y anaalizar los resultados.

### Preguntas Orientadoras

- ¿Cuál es el efecto del ruido sobre la amplitud de las señales medidas en el osciloscopio? ¿Conservan las mismas relaciones que se evidencian en la simulación?

No son iguales debido a efectos de canal producida por la impedacia de los cables , de las entradas de los equipos  y ruido producido por la manipulacion de los equipos los cuales producen fuertes atenuaciones en la potencia de la señal.

<div style="text-align: center;">
    <img src="./3.Actividad 2 Osciloscopio/Señalnoise.PNG" alt="GNUConstante" width="300" />
    <p><b>Senosoidal con ruido</b></p>
</div>

- ¿La relación señal a ruido creada intencionalmente en el computador se amplifica o se reduce en la señal observada en el osciloscopio?

La relacion señal a ruido disminuye en el osciloscopio debido a que la potencia de la señal transmitida se atenua por efectos de canal mas la potencia del ruido no.


- ¿Cómo se evidencia el fenómeno de desviación de frecuencia en el osciloscopio? 

**Efecto de desviacion estandar**
| ![Analizador_Constante3](./3.Actividad%202%20Osciloscopio/SCR05.PNG) |  ![Analizador_Constante3](./3.Actividad%202%20Osciloscopio/SCR07.PNG) 
|:---:|:---:|
| **Desviación de frecuencia** | **Señal original** |


- Determine la afectación de un medio de transmisión coaxial (usar cables largos) sobre una señal periódica operando a las capacidades máximas de muestreo del USRP.
- 
  - **NOTA:** La frecuencia de transmisión no debe superar los 500 MHz para ser observada en el osciloscopio. Para el experimento, considere las relaciones de muestreo correspondientes.

**Efecto de desviacion estandar**
| ![Analizador_Constante3](./3.Actividad%202%20Osciloscopio/SCR01.PNG) |  ![Analizador_Constante3](./3.Actividad%202%20Osciloscopio/SCR02.PNG) 
|:---:|:---:|
| **Cable corto** | **Cable largo** |

- Usando antenas, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida? ¿Es posible compensar el fenómeno?

La potencia de la señal recibida es inversamente proporcional a la distancia entre las antenas de los medios como se puede evidenciar en la ecuacion de Friss

<div style="text-align: center;">
    <img src="./3.Actividad 2 Osciloscopio/Ecuaciondefriss.jpg" alt="GNUConstante" width="300" />
    <p><b>Ecuacion de friss</b></p>
</div>

Ademas otros efectos de canal como la transmision en la misma banda de frecuencias , manipulacion de los equipos, antenas sin linea de vista pueden afectar directamente a esta misma, donde ademas se pueden producir entre otras degradaciones en la trasnmision del canal.

- ¿Qué modelo de canal básico describe mejor las mediciones obtenidas en la práctica?

Un modelo que considere las degradaciones de canal dependiendo del medio de transmision, en caso de usar transmision por linea considerar las atenuaciones dadas por la longitud del cable, impedacia en las entradas de los equipos y ruido gausiano. En caso de usar transmision inalambria considerar los efectos como la ecuacion de friss, la importancia de tener una linea de vista y de considerar efectos climatológicos

---

## Actividad 3: Fenómenos de canal en el analizador de espectro

### Objetivo

Familiarizarse con los fenómenos de un canal alámbrico real en el dominio de la frecuencia.

### Procedimiento

1. **Configurar el USRP 2920:**
   - Configurar el flujograma [filters_flowgraph.grc](filters_flowgraph.grc) en GNU Radio para transmitir una señal a través del USRP.
   - Habilitar o deshabilitar los bloques correspondientes (`Channel Model`, `Throttle`, `UHD: USRP Sink`, `UHD: USRP Source`, `Virtual Sink`). Para esto, seleccione el bloque deseado y presione **E** (enable) o **D** (disable), respectivamente.
   - Configurar siempre la frecuencia de muestreo (`samp_rate`) en $25e6/2^n$ Hz`, donde $n$ es un número entero mayor a 2.  Verifique que la frecuencia de muestreo durante la ejecución, sea la misma que ha configurado en el flujograma.

2. **Configurar el Analizador de Espectros:**
   - Encender, configurar y conectar el analizador de espectros a la salida del USRP 2920 usando diferentes cables coaxiales, y ajustando los parámetros necesarios para evidenciar los fenómenos de canal analizados en la Actividad 1.

### Preguntas Orientadoras

- ¿Cuál es el efecto del ruido sobre la respuesta en frecuencia de las señales medidas en el analizador de espectro? ¿Conservan las mismas relaciones que se evidencian en la simulación?

Se observa una diferencia en la medida de potencia en los equipos dada por la diferencia entre la impedancia de entrada de entrada para su funcionalidad.  El osciloscopio R&S®RTB2000 tiene una impedancia de entrada alta (1 MΩ) para no cargar el circuito y medir voltajes sin alterar la señal, ideal para observar formas de onda. En cambio, el analizador de espectro R&S®FPC1000 usa 50 Ω para adaptarse a sistemas de RF y medir potencia de forma precisa. Cada uno es mejor en su función: el osciloscopio para medir tensión en el tiempo y el analizador para medir potencia y espectro en frecuencia.





- Usando cables coaxiales de diferentes longitudes, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida?

Con cables largos, la señal experimenta una mayor atenuación, lo que reduce su amplitud significativamente y provoca una variación mínima en su frecuencia central, además de introducir un ligero retardo en la transmisión. Por el contrario, al usar cables cortos, la atenuación es menor, permitiendo que la señal mantenga una mejor amplitud y su fidelidad, sin que su frecuencia se vea afectada de forma considerable ni se introduzcan retardos perceptibles.
- Usando antenas, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida? ¿Es posible compensar el fenómeno?

Cuando el transmisor y el receptor están cerca, la señal se amplifica porque hay menos dispersión y atenuación. A medida que la distancia aumenta, la amplitud de la señal disminuye debido a las pérdidas inherentes a la propagación en el espacio libre. Además, cualquier perturbación en el medio, como la presencia de una mano cerca de la antena, puede absorber parte de la energía y afectar la señal. Para mitigar estos efectos, se puede ajustar la potencia de transmisión, usar antenas direccionales o añadir amplificadores de señal.


## Actividad 4: Efectos de los fenómenos de canal en la conversión de frecuencia

### Objetivo

Familiarizarse con los efectos de los fenómenos de un canal alámbrico e inalámbrico real en la conversión de frecuencia.

### Procedimiento

**Configurar el USRP 2920:**
   - Configurar el flujograma [filters_flowgraph.grc](filters_flowgraph.grc) en GNU Radio para **transmitir y recibir ** una señal a través del USRP.
   - Habilitar o deshabilitar los bloques correspondientes (`Channel Model`, `Throttle`, `UHD: USRP Sink`, `UHD: USRP Source`, `Virtual Sink`). Para esto, seleccione el bloque deseado y presione **E** (enable) o **D** (disable), respectivamente.
   - Configurar siempre la frecuencia de muestreo (`samp_rate`) en $25e6/2^n$ Hz`, donde $n$ es un número entero mayor a 2. Verifique que la frecuencia de muestreo durante la ejecución, sea la misma que ha configurado en el flujograma.
   - Compare los resultados al recibir la señal usando diferentes medios (aire o cable coaxial).

### Preguntas Orientadoras

- ¿Cómo se evidencian los diferentes fenómenos de canal en la señal recibida?

Los fenómenos de canal se manifiestan en la señal recibida principalmente como atenuación, la cual reduce su amplitud debido a las pérdidas inherentes al medio de transmisión. También se observa el desvanecimiento, que causa fluctuaciones en la potencia de la señal, y la presencia de ruido, que introduce componentes no deseados y afecta la claridad de la comunicación.

- ¿Cómo se pueden mitigar los efectos del canal en la señal recibida?
Estos problemas se pueden mitigar utilizando filtros (pasa banda o pasa bajos) para reducir el ruido, y amplificadores para contrarrestar la atenuación. Además, tecnologías modernas como Wi-Fi o 5G tienen la capacidad de ajustar dinámicamente la transmisión, lo que les permite optimizar el rendimiento de la señal en diferentes entornos.
