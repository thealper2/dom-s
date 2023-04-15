# dom-s

Bir domain hakkında bilgiler öğrenmeye yarayan bir araçtır.

## Gereksinimler

ssh-brute aşağıdaki kütüphaneleri kullanır.

* Colorama
* Dnspython
* Whois
* Requests

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/dom-s.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -d        | Sorgu yapılacak domaini belirtmek için kullanılır. |
| -w        | Alt domainleri bulmak için kullanılacak wordlist dosyasını belirtmek için kullanılır. |
| -q        | WHOIS sorgusu yapmak için kullanılır. |
| -r        | DNS Resolve |
```bash
usage: dom-s.py [-h] -d D [-w W] [-q] [-r]

domain search

options:
  -h, --help  show this help message and exit
  -d D        domain
  -w W        subdomain wordlist
  -q          WHOIS query
  -r          DNS Resolve
```

## Örnekler

```python
python3 dom-s.py -d TARGET_DOMAIN -r
python3 dom-s.py -H TARGET_IP -q
python3 dom-s.py -H TARGET_IP -w subdomains.txt
```
