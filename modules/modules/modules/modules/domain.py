import socket

def domain_scan(domain):
    try:
        ip = socket.gethostbyname(domain)

        return f"""
domain report

domain: {domain}
ip: {ip}

status: resolved
"""
    except:
        return "domain not found"
