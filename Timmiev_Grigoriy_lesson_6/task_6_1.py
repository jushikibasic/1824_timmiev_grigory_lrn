# получить список кортежей вида:
# (<remote_addr>,<request_type>,<requested_resource>)
# Например:[('141.138.90.60', 'GET', '/downloads/product_2')]

with open('Chache/nginx_logs.txt', 'r', encoding='utf-8') as fr:
    result = []
    for line in fr:
        string = line.strip()
        remote_addr, _, _, _, _, request_type, requested_resource, *_ = string.split()
        result.append(tuple((remote_addr, request_type[1:], requested_resource)))
    print(len(result))

