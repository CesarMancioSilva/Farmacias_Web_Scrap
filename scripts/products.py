def extract_product_data(product,farmacia_name):
    return {
        'id': product.get('id'),
        'description': product.get('description'),
        'details': product.get('details'),
        'unit_price': product.get('unitPrice'),
        'min_price': product.get('unitMinPrice'),
        'original_price': product.get('unitOriginalPrice'),
        'min_order': product.get('sellingOption', {}).get('minimum'),
        'incremental': product.get('sellingOption', {}).get('incremental'),
        'available_units': ', '.join(product.get('sellingOption', {}).get('availableUnits', [])),
        'tags': ', '.join([tag['tags'][0] for tag in product.get('productTags', []) if tag['tags']]),
        'packaging': product.get('productInfo', {}).get('packaging'),
        'quantity': product.get('productInfo', {}).get('quantity'),
        'unit': product.get('productInfo', {}).get('unit'),
        'categories': ', '.join(product.get('productAisles', [])),
        'empresa':farmacia_name,
    }

