import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def setup_driver():
    """Configura y devuelve el driver de Selenium para Firefox."""
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    service = Service(r'C:\Users\yanze\Documents\AppPythonDeteccionFace\geckodriver.exe')  # Cambia si el nombre del archivo es diferente
    driver = webdriver.Firefox(service=service, options=options)
    return driver


def scrape_amazon(query, max_results=50):
    """
    Busca productos en Amazon, extrae precios y descuentos.
    
    Args:
    - query (str): Término de búsqueda en Amazon.
    - max_results (int): Número máximo de productos a extraer.

    Returns:
    - List[Dict]: Lista de productos con su información.
    """
    driver = setup_driver()
    url = f"https://www.amazon.com/s?k={query.replace(' ', '+')}"
    driver.get(url)
    time.sleep(3)  # Esperar que cargue la página
    
    products = []
    try:
        while len(products) < max_results:
            items = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
            for item in items:
                try:
                    title = item.find_element(By.CSS_SELECTOR, "h2 a span").text
                    price_whole = item.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                    price_fraction = item.find_element(By.CSS_SELECTOR, ".a-price-fraction").text
                    price = float(price_whole.replace(",", "") + "." + price_fraction)
                    discount_element = item.find_elements(By.CSS_SELECTOR, ".savingsPercentage")
                    discount = int(discount_element[0].text.replace("%", "").replace("-", "")) if discount_element else 0
                    link = item.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                    
                    products.append({
                        "Title": title,
                        "Price": price,
                        "Discount (%)": discount,
                        "Link": link
                    })

                    if len(products) >= max_results:
                        break
                except Exception as e:
                    # Ignorar errores en elementos específicos
                    continue
            
            # Intentar ir a la siguiente página si no se alcanzó el límite
            next_page = driver.find_elements(By.CSS_SELECTOR, ".s-pagination-next")
            if next_page and len(products) < max_results:
                next_page[0].click()
                time.sleep(3)
            else:
                break
    except Exception as e:
        print(f"Error durante el scraping: {e}")
    finally:
        driver.quit()

    return products


def save_to_csv(products, filename="amazon_products.csv"):
    """
    Guarda los productos en un archivo CSV.

    Args:
    - products (List[Dict]): Lista de productos con su información.
    - filename (str): Nombre del archivo CSV.
    """
    df = pd.DataFrame(products)
    df = df.sort_values(by=["Price", "Discount (%)"], ascending=[True, False])  # Ordenar por precio y descuento
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"Datos guardados en {filename}")


if __name__ == "__main__":
    search_query = input("¿Qué productos deseas buscar? ")
    max_items = int(input("¿Cuántos productos deseas extraer? "))
    products = scrape_amazon(search_query, max_results=max_items)
    if products:
        save_to_csv(products)
    else:
        print("No se encontraron productos.")