import requests

URL = "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY_RAW.txt"

r = requests.get(URL, timeout=30)
r.raise_for_status()

vless = [l for l in r.text.splitlines() if l.startswith("vless://")]

with open("vless.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(vless))
