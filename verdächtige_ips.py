from collections import Counter

logs = [
    {"ip": "192.168.0.1", "status": 200, "url": "/index.html", "zeit": "10:01"},
    {"ip": "192.168.0.2", "status": 404, "url": "/login",      "zeit": "10:02"},
    {"ip": "192.168.0.1", "status": 500, "url": "/api/data",   "zeit": "10:03"},
    {"ip": "192.168.0.3", "status": 200, "url": "/index.html", "zeit": "10:04"},
    {"ip": "192.168.0.2", "status": 403, "url": "/admin",      "zeit": "10:05"},
    {"ip": "192.168.0.2", "status": 403, "url": "/admin",      "zeit": "10:06"},
    {"ip": "192.168.0.4", "status": 200, "url": "/shop",       "zeit": "10:07"},
    {"ip": "192.168.0.1", "status": 503, "url": "/api/data",   "zeit": "10:08"},
]
# Status 200 = gut | Alles über 400 = Fehler
# ---------ERMITTLUNG DER ANZAHL VON REQUESTS UND FEHLERN---------------
def detect():
    ip_stats = {}
    for log in logs:
        ip = log["ip"]
        status = log["status"]

        if ip not in ip_stats:
            ip_stats[ip] = {"ip": ip, "total": 0, "errors": 0}

        ip_stats[ip]["total"] += 1

        if status >=400:
            ip_stats[ip]["errors"] += 1
    return ip_stats
# -----------------------------------------------------------------------
# ------------VERDÄCHTIGE IPS ERMITTELN----------------------------------
def detect_sus():
    sus_ips = []
    for ip, stats in ip_stats.items():  
        if stats["total"] > 2:
            sus_ips.append(ip)

    last_error = {}
    for log in logs:
        ip = log["ip"]
        status = log["status"]
        url = log["url"]

        if status >= 400:
            current = (url, status)

            if ip in last_error and last_error[ip] == current:
                sus_ips.append(ip)
            last_error[ip] = current
    return sus_ips

def detect_most():
    url_list = []
    for log in logs:
        url = log["url"]
        url_list.append(url)

    url_counter = Counter(url_list)
    common, count = url_counter.most_common(1)[0]
    print(f"Häufigstes Element: {common} (kommt {count} Mal vor)")

ip_stats = detect()
for ip, total in ip_stats.items():
    first_key = next(iter(ip_stats))

    print(f"IP: {first_key} | Anfragen: {ip_stats[ip]["total"]} | Fehler: {ip_stats[ip]["errors"]}")

list_sus = detect_sus()
list_sus = list(dict.fromkeys(list_sus))
print(f"Verdächtige IPs: {list_sus}")
detect_most()


input()