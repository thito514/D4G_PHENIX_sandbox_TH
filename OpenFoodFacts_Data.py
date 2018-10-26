#############
## Liste de fonctions pour extraire des données de OpenFoodFacts (à compléter)
## par Thierry Ha
#############

def get_OpenFoodFactsData(EAN_number):
	import pandas as pd
	import requests

	url = ' https://fr.openfoodfacts.org/api/v0/produit/'
	product_json = requests.get(url+str(EAN_number)+'.json').content
	df_product = pd.read_json(product_json)

	return df_product

def get_productname(df_product):
    return (df_product[df_product.index == 'generic_name_fr']['product'][0])

def get_quantity(df_product):
    return (df_product[df_product.index == 'quantity']['product'][0])

def get_novagroup(df_product):
    try:
        result = (df_product[df_product.index == 'nova_groups']['product'][0])
    except:
        result = False
    return result

def get_nutriscore(df_product):
    return (df_product[df_product.index == 'nutrition_grade_fr']['product'][0])

def get_categories(df_product):
    return (df_product[df_product.index == 'categories']['product'][0].split(','))
            
def get_categories_hierarchy(df_product):
    return (df_product[df_product.index == 'categories_hierarchy']['product'][0])

def extract_quantity(str_qty):
    import re
    lst_qty = str_qty.split(',')
    lst_dict = []
    for s in lst_qty:
        string = s.strip()
        print(string)
        value = re.search('\\d+[,.]?\\d*',string).group(0)
        print(value)
        unit = re.search('([a-zA-Z]+)',string).group(0) if re.search('([a-zA-Z]+)',string)!=None else ''
        t = ''
        if re.search('l|L',unit)!=None:
            t = 'volume'
        if re.search('g|G',unit)!=None:
            t = 'weight'
            d = {'string': string, 'value': value, 'unit':unit, 'type':t}
        lst_dict.append(d)
    return lst_dict