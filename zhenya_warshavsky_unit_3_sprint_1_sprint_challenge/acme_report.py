from acme import Product

import random

def generate_products():
    products = []
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'] 

    for i in range(30):
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        product = Product(name = name)
        product.price = 15
        product.price = random.randint(5, 100)
        product.weight = random.randint(5, 100)
        product.flammability = random.uniform(0.0,2.5) 
        products.append(product)
    return products


def inventory_report():
    # #takes a list of products and prints summary
    products = generate_products()
    # print([i.name for i in products])
    uniques = len(list(set([i.name for i in products])))
    print(f'Unique product names: {uniques}')
    PriceMean = (sum([i.price for i in products]) / len(products))
    print(f'Average price: {PriceMean}')
    WeightMean = (sum([i.weight for i in products]) / len(products))
    print(f'Average weight: {WeightMean}')
    FlammabilityMean = (sum([i.flammability for i in products]) / len(products))
    print(f'Average flammability: {FlammabilityMean}')

    
if __name__ == '__main__':
    inventory_report()
