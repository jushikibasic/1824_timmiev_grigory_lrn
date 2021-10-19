result = []
with open('Chache/nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        string = line.strip()
        remote_addr, _, _, _, _, request_type, requested_resource, *_ = string.split()
        result.append(tuple((remote_addr, request_type[1:], requested_resource)))
    spam_ch = []
    for item in result:
        spam_ch.append(item[0])
    from collections import Counter
    hi_scores = Counter(spam_ch)
    max_val = max(hi_scores.values())
    spam_addr = list(hi_scores.keys())[list(hi_scores.values()).index(max_val)]
    spam = f'адресс:{spam_addr} запросов: {max_val}'
print(spam)
