import nmap

class ServiceByPortService:
    def get_services_by_port(self, port):
        scanner = nmap.PortScanner()
        scanner.scan(arguments='-p %d' % port)

        results = []
        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                if port in scanner[host][proto]:
                    result = {
                        'Host': host,
                        'Protocol': proto,
                        'Port': port,
                        'Service': scanner[host][proto][port]['name'],
                        'Version': scanner[host][proto][port]['version'],
                        'State': scanner[host][proto][port]['state']
                    }
                    results.append(result)

        return results
