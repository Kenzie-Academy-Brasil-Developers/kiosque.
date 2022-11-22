from menu import products


def get_product_by_id(_id: int):
    if type(_id) != int:
            raise TypeError("product id must be an int")
    for dish in products:
        if dish["_id"] == _id:
            return dish
    return {}
    
    

def get_products_by_type(_type: str):
    if type(_type) != str:
        raise TypeError("product type must be a str")
    lis = []
    for dish in products:
        if dish["type"] == _type:
            lis.append(dish)
    return lis
    

def menu_report():
    average = 0
    most_common_type = ""
    max_type_value = 0
    types={}
    for product in products:
        average += product["price"]
        types[product["type"]]= len(get_products_by_type(product["type"]))
    for _type in types.items():
        if _type[1] > max_type_value:
            max_type_value = _type[1]
            most_common_type = _type[0]

    return f"Products Count: {len(products)} - Average Price: ${round(average/len(products),2)} - Most Common Type: {most_common_type}"



def add_product(menu: list, **kwargs):
    max_product_id = 0
    for product in menu:
        if product["_id"] > max_product_id:
            max_product_id = product["_id"]
    max_product_id += 1
    kwargs["_id"] = max_product_id
    menu.append(kwargs)
    return kwargs
