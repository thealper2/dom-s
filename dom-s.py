import requests
import whois
import argparse
import colorama
from colorama import Fore, Back, Style
import dns.resolver

colorama.init(autoreset=True)

def subdomain_discovering(domain, subdomain_list):
	try:
		with open(subdomain_list) as file:
			content = file.read()
			subdomains = content.splitlines()

		for subdomain in subdomains:
			url = f"http://{subdomain}.{domain}"
			res = requests.get(url)
			if res.status_code == 200:
				print(f"{Fore.GREEN}[+] Discovered: {Fore.RESET}", url)

	except Exception as e:
		print(f"{Fore.RED}[!] Error: {Fore.RESET}", e)

def resolve_dns(domain):
	record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
	resolver = dns.resolver.Resolver()
	try:
		for record_type in record_types:
			try:
				answer = resolver.resolve(domain, record_type)
			except dns.resolver.NoAnswer:
				continue

		print(f"{Fore.YELLOW}[?] DNS records [{domain}]:({record_type}): {Fore.RESET}")
		for answer in answers:
			print(f"{Fore.GREEN}[+] {answer} {Fore.RESET}")

	except Exception as e:
		print(f"{Fore.RED}[!] Error: {Fore.RESET}", e)

def py_whois(domain):
	try:
		host = whois.query(domain)

		print(f"{Fore.YELLOW}WHOIS RESULTS{Fore.RESET}")
		print(f"{Fore.GREEN}[+] Name: {Fore.RESET}", host.name)
		print(f"{Fore.GREEN}[+] Registrar: {Fore.RESET}", host.registrar)
		print(f"{Fore.GREEN}[+] Creation Date: {Fore.RESET}", host.creation_date)
		print(f"{Fore.GREEN}[+] Expiration Date: {Fore.RESET}", host.expiration_date)
		print(f"{Fore.GREEN}[+] Last Updated: {Fore.RESET}", host.last_updated)
		print(f"{Fore.GREEN}[+] Name Servers: {Fore.RESET}", host.name_servers)

	except Exception as e:
		print(f"{Fore.RED}[!] Error: {Fore.RESET}", e)

argument_parser = argparse.ArgumentParser(description='domain search')
argument_parser.add_argument("-d", required=True, type=str, help='domain')
argument_parser.add_argument("-w", required=False, type=str, help='subdomain wordlist')
argument_parser.add_argument("-q", required=False, action='store_true', help='WHOIS query')
argument_parser.add_argument("-r", required=False, action='store_true', help='DNS Resolve')
args = argument_parser.parse_args()

if args.w != None and not args.q and not args.r:
	subdomain_discovering(args.d, args.w)

elif args.w == None and args.q and not args.r:
	py_whois(args.d)

elif args.w == None and not args.q and args.r:
	resolve_dns(args.d)
