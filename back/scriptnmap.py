import nmap

def scan_host(hostname):
    scanner = nmap.PortScanner()
    scanner.scan(hostname, arguments='-Pn -sV -O')

    # Affichage des résultats de l'analyse de ports et services
    for host in scanner.all_hosts():
        print('Host : %s (%s)' % (host, scanner[host].hostname()))
        print('State : %s' % scanner[host].state())
        for proto in scanner[host].all_protocols():
            print('Protocol : %s' % proto)

            # Parcours des ports pour le protocole actuel
            ports = scanner[host][proto].keys()
            for port in ports:
                print('Port : %s\tState : %s\tService : %s' % (port, scanner[host][proto][port]['state'], scanner[host][proto][port]['name']))

    # Exécution de l'analyse des vulnérabilités
    scanner.scan(hostname, arguments='-sV --script vulners')
    for host in scanner.all_hosts():
        print('Host : %s' % host)
        if 'vulners' in scanner[host]:
            for result in scanner[host]['vulners']:
                print('Vulnerability : %s' % result['id'])
                print('Summary : %s' % result['summary'])
                print('CVSS : %s' % result['cvss'])
        else:
            print('No vulnerabilities found for this host.')
# Appel de la fonction avec l'adresse IP ou le nom d'hôte
scan_host('127.0.0.1')