import os

# 讀取檔案
def read_file(file_name):
    products = []
    with open(file_name, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products

# 使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q' or name == '':
            break
        price = input('請輸入商品金額：')   
        products.append([name, price])
    print(products)
    return products

#印出所有商品
def print_products(products):
    for p in products:
        print(p)

# 存檔
def save(file_name, products):
    with open(file_name, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    file_name = 'products.csv'
    if os.path.isfile(file_name):# 檢查檔案
        print('找到檔案了')
        products = read_file(file_name)
    else:
        print('找不到檔案')
    products = user_input(products)
    print_products(products)
    save('products.csv', products)

main()