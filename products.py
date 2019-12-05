import os

products = []
if os.path.isfile('products.csv'):
	print('找到檔案了')
	# 讀取檔案
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案...')

# 使用者輸入
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

# 存檔
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')