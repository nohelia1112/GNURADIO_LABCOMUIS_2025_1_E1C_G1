# Laboratorio de Comunicaciones
## Universidad Industrial de Santander

---
# Práctica 1: CREAR UN REPOSITORIO GITHUB

### Integrantes
- **NOHELIA AGUDELO CUERVO** - 2210413
- **FABIÁN CAMILO CHACÓN** - 2214192

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
13 de febrero de 2025

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento. 

---
## Contenido

### Resumen
En el presente informe, se presentan las evidencias de la creación de un repositorio de GitHub y usuario Git para uso del componente de laboratorio de la asignatura Comunicaciones I. 

**Palabras clave:** GitHub, Git.

### Introducción

Git es un software de control de versiones de código abierto que permite rastrear de manera eficiente los cambios en los archivos de un proyecto, a través de lo que se conoce como un repositorio. Es una herramienta bastante útil para el desarrollo del laboratorio en el transcurso del semestre gracias a su disponibilidad de trabajo simultáneo, facilitando el apoyo de trabajo en grupo.

Existen diversas plataformas de alojamiento basadas en Git, entre ellas GitHub, un servicio en la nube diseñado precisamente para el desarrollo colaborativo. Esta plataforma permite gestionar proyectos mediante el sistema de control de versiones Git y se utiliza principalmente para almacenar y desarrollar código fuente de software. Adicionalmente, se ha convertido en una herramienta clave para profesionales de la industria TI, funcionando como una carta de presentación o portafolio que muestra sus habilidades y contribuciones en proyectos de software.

### Procedimiento

En primer lugar, se realizó con antelación la conformación del grupo 1 (G1) de laboratorio en el aula virtual Moodle. Durante las horas estipuladas de laboratorio, de realizó la creación de cuentas de usuario, haciendo mención al docente Óscar Reyes del banco 4 como puesto de trabajo. Posteriormente, se hizo el cambio de contraseña con ayuda del comando "passwd" al ejecutarlo desde el terminal de Linux.

Por otro lado, se hizo la creación del repositorio "GNURADIO_LABCOMUIS_2025_1_E1C_G1" en una cuenta de GitHub existente. Se creó la clave SSH (id_ed25519) para la cuenta de la propietaria del repositorio desde el banco trabajo, usando el comando "ssh-keygen -t ed25519 -C 'nohelia1112@hotmail.com'", comprobándose la conexión SSH con "ssh -T git@github.com". Después, se estableció un usuario con el protocolo "git config --global user.name" y "git config --global user.email", y se clonó el repositorio usando la clave SSH.

Como última medida, se subió README.md al branch main. Se creó una nueva rama y fue subida al repositorio remoto con "git push -u origin <nombre_rama>".

### Conclusión

Con éxito se pudo crear el repositorio de Github a utilizar a lo largo del semestre y se vinculó el repositorio local con el remoto en el respectivo puesto de trabajo.

### Referencias

- [Git](https://es.wikipedia.org/wiki/Git)
- [Qué es GitHub y cómo empezar a usarlo](https://www.hostinger.es/tutoriales/que-es-github)

---

  

