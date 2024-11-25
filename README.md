## RPAProductosAmz


 # Amazon Scraper

Este proyecto es una herramienta de scraping para extraer información de productos de Amazon. Permite buscar productos, recolectar detalles como el título, precio, descuento y enlace, y guardar los resultados en un archivo CSV.

## Características

- Busca productos en Amazon usando un término de búsqueda.
- Extrae información detallada de cada producto:
  - Título
  - Precio
  - Descuento (%)
  - Enlace al producto
- Guarda los datos ordenados en un archivo CSV.

## Requisitos

- Python 3.7 o superior
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) para controlar Firefox
- Navegador Mozilla Firefox
- Bibliotecas de Python:
  - `selenium`
  - `pandas`

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
    ```

## Instala las dependencias:
  ```bash
    Copiar código
    pip install selenium pandas.
   ```

## Configura Geckodriver:

  Descarga Geckodriver desde aquí.
  Asegúrate de colocar el archivo ejecutable en una ubicación accesible.
  Actualiza la ruta del controlador en el código:
  python
  Copiar código
  service = Service(r'C:\ruta\a\geckodriver.exe')
  Uso

## Ejecuta el script:

```bash
Copiar código
python amazon_scraper.py
 ```


## Introduce los datos requeridos:

  Término de búsqueda: Escribe el nombre del producto o categoría que deseas buscar (por ejemplo, "laptops", "smartphones").
  Número máximo de productos: Ingresa la cantidad máxima de productos que deseas extraer.
  Revisa los resultados:

  Los datos extraídos se guardarán en un archivo CSV llamado amazon_products.csv en el directorio actual.
  Organización del Código
  setup_driver: Configura el controlador de Selenium para Firefox.
  scrape_amazon: Realiza la búsqueda y extrae información de los productos.
  save_to_csv: Guarda los datos recolectados en un archivo CSV.
  Notas
  El scraping está sujeto a los términos de uso de Amazon. Utiliza este script de manera responsable y asegúrate de no exceder las solicitudes permitidas por el sitio.
  Este script puede requerir ajustes en los selectores CSS si Amazon realiza cambios en su estructura HTML.
  Contribuciones
  ¡Contribuciones son bienvenidas! Si tienes sugerencias o mejoras, crea un pull request o abre un issue.

Licencia
Este proyecto se distribuye bajo la MIT License.


