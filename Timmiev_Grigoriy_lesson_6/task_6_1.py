from utils import send_request

print(*send_request())

#with open('Chache/nginx_logs.txt', 'w', encoding='utf-8') as fw:
#    fw.write(str([*send_request()]))
#    # fw.write(*send_request())
#
#file_2 = open('Chache/nginx_logs.txt', 'r', encoding='utf-8')
#print(file_2.readline().strip())
#
