# Análisis del Código Fuente de Bitcoin v0.1 (2008)

## Estructura General del Proyecto

La versión 0.1 estaba compuesta por varios archivos fuente escritos en C++, junto con librerías auxiliares. Los componentes clave eran:

- `main.cpp`: lógica principal para la creación de bloques, verificación de transacciones y ejecución del nodo.
- `net.cpp`: gestión de la red peer-to-peer y conexión entre nodos.
- `db.cpp`: implementación de la base de datos para almacenar la cadena de bloques.
- `script.cpp`: ejecución de scripts de transacciones, base del sistema de pagos condicionales de Bitcoin.
- `irc.cpp`: conexión inicial entre nodos mediante canales IRC.
- `sha.cpp`: funciones criptográficas para hashing (SHA-1 y SHA-256).
- `util.cpp`: utilidades auxiliares para la depuración y manejo de errores.

Aunque sencillo comparado con las versiones modernas, este primer diseño ya contenía las funciones básicas del protocolo.

## Características Notables

### Conexión a través de IRC

En lugar de emplear mecanismos de descubrimiento de nodos como los actuales (DNS seeds o listas estáticas), la versión inicial utilizaba canales de IRC para que los nodos encontraran a otros. Esto se implementó como una solución temporal hasta que se desarrollaran métodos más sólidos de conexión entre pares.

### Funcionalidades experimentales

El repositorio contenía referencias a módulos que nunca llegaron a finalizarse:

- **Mercado P2P**: Un archivo llamado `market.cpp` sugiere que existía la intención de integrar un mercado descentralizado, aunque no hay evidencia de que haya sido implementado.
- **Juego de póker distribuido**: También se hallaron rastros de un módulo para un juego de póker, lo que indica que Nakamoto estaba explorando otros casos de uso para la red peer-to-peer, posiblemente para experimentar con contratos condicionales o micropagos.

### Control preciso del versionado

Satoshi asignó manualmente fechas y horas específicas a los archivos del código fuente (por ejemplo, el 15 de noviembre de 2008 a las 00:00:01), probablemente como método interno para llevar el control de las versiones y facilitar la comparación entre distintas copias del proyecto.

## Contexto del Lanzamiento

- **Publicación del whitepaper**: El 31 de octubre de 2008, Nakamoto dio a conocer el documento “Bitcoin: A Peer-to-Peer Electronic Cash System”, sentando las bases teóricas del proyecto.
- **Primer bloque (Génesis)**: El 3 de enero de 2009 se minó el primer bloque de la cadena (bloque génesis), con un mensaje codificado que aludía a la crisis financiera de ese año.
- **Lanzamiento del cliente**: El 9 de enero de 2009, Nakamoto publicó el software en SourceForge, permitiendo que cualquiera pudiera unirse a la red y comenzar a minar.

## Conclusión

El código original de Bitcoin demuestra un enfoque pragmático y funcional, priorizando una red operativa y autónoma antes que características avanzadas o interfaces complejas. Aunque algunas ideas quedaron como intentos no desarrollados (como el mercado P2P o el póker), el núcleo del sistema —cadena de bloques, minería con prueba de trabajo y red entre pares— ya estaba completamente funcional.

Este primer software marcó el inicio de una transformación profunda en cómo concebimos el valor digital, los sistemas distribuidos y la soberanía financiera.

## Referencias

1. Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://bitcoin.org/bitcoin.pdf  
2. BitcoinTalk Archive (2009). [Primer mensaje de Nakamoto con el lanzamiento](https://bitcointalk.org/index.php?topic=6.0)  
3. Chain Bulletin. (2020). *Satoshi Used Timestamps for Early Bitcoin Code Versioning*. https://chainbulletin.com/satoshi-used-timestamps-for-early-bitcoin-source-code-versioning  
4. Bitcoin Insider. (2019). *Satoshi’s Pre-Release Bitcoin Code Contains Fascinating Findings*. https://www.bitcoininsider.org/article/63857  
5. GitHub Archive: [Bitcoin v0.1](https://github.com/Maguines/Bitcoin-v0.1)  

---
