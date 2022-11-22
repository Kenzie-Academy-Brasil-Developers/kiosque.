from menu import products

def calculate_tab(list_dic: list):
    result = {"subtotal": 0}

    for consumption in list_dic:
         for product in products:
             if product["_id"] == consumption["_id"]:
                 result["subtotal"] += product["price"]*consumption["amount"]
    result["subtotal"] = "$"+str(round(result["subtotal"],2))
    return result
