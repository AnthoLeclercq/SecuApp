import nmap

class LocalNetworkScanService:
    def scan_local_network(self):
        scanner = nmap.PortScanner()
        scanner.scan(hosts='192.168.1.0/24', arguments='-sP')

        results = []
        for host in scanner.all_hosts():
            host_info = {
                'Host': host,
                'Status': scanner[host].state(),
                'OpenPorts': []
            }
            if scanner[host].all_protocols():
                for proto in scanner[host].all_protocols():
                    for port in scanner[host][proto].keys():
                        host_info['OpenPorts'].append({
                            'Port': port,
                            'Service': scanner[host][proto][port]['name'],
                            'Protocol': proto
                        })
            results.append(host_info)

        return results
