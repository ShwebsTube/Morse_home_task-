import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',32768))
s.listen()


def str2morse(x):
    
    if x == '0':
        return '-----'
    elif x == '1':
        return '.----'
    elif x == '2':
        return '..---'
    elif x == '3':
        return '...--'
    elif x == '4':
        return '....-'
    elif x == '5':
        return '.....'
    elif x == '6':
        return '-....'
    elif x == '7':
        return '--...'
    elif x == '8':
        return '---..'
    elif x == '9':
        return '----.'
    elif x == '.':
        return '-.-.-'
        
        
while True:
    
    conn, addr = s.accept()
    ip = str(addr[0])
    print(ip)
    m = " "
    ip = ip.strip()
    for x in ip:
        m += str2morse(x)
    conn.send(str(m))
    conn.close()        


while True:
    
    conn, addr = s.accept()
    
    ip = str(addr[0])
    print(ip)
    m = " "
    ip = ip.strip()
    for x in ip:
        m += str2morse(x)
    conn.send(str(m))
    conn.close()        



