import requests
from bs4 import BeautifulSoup

def dede(material_name):
    base_url = "https://www.dedeman.ro/ro/materiale-de-constructii/c/21"
    products = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    # Loop through all pages
    for page in range(1, 18):  # Adjust the range to match the total number of pages
        url = f"{base_url}?page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
            break
 
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Find product containers
        product_containers = soup.find_all('div', class_='product-item-info')

        # Break the loop if no products are found
        if not product_containers:
            print(f"No products found on page {page}. Stopping.")
            break

        for container in product_containers:
            # Extract product name
            name_tag = container.find('strong', class_='product-item-name')
            product_name = name_tag.text.strip() if name_tag else "No name"

            # Extract product link
            link_tag = name_tag.find('a') if name_tag else None
            product_link = link_tag['href'] if link_tag else "No link"

            # Extract price and unit
            price_container = container.find('div', class_='price-box')
            if price_container:
                price_tag = price_container.find('span', class_='price')
                unit_tag = price_container.find('span', class_='price-sale-unit')
                price = price_tag.text.strip() if price_tag else "No price"
                unit = unit_tag.text.strip() if unit_tag else "No unit"
                price_info = f"{price} {unit}"
            else:
                price_info = "No price info"

            # Match material name (partial match)
            if material_name.lower() in product_name.lower():
                products.append({
                    'full_name': product_name,
                    'link': product_link,
                    'price_info': price_info
                })

        print(f"Page {page} scraped successfully.")

    return products
