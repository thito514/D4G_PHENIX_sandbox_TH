

def get_OpenFoodFactsData(EAN_number):
	import pandas as pd
	import requests

	url = ' https://fr.openfoodfacts.org/api/v0/produit/'
	product_json = requests.get(url+EAN_search+'.json').content
	df_product = pd.read_json(product_json)

	return df_product