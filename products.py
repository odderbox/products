products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q' or name == '':
		break
	price = input('請輸入商品金額：')	

	#product = []
	#product.append(name)
	#product.append(price)
	
	#product = [name, price]

	products.append([name, price])
print(products)

for p in products:
	print(p)
	"""
for i in range(len(products)):
	for j in range(len(product)):
		print(products[i][j])
		"""
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')