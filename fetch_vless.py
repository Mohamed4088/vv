from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY_RAW.txt"

data = urlopen(URL, timeout=30).read().decode("utf-8")

vless = [l for l in data.splitlines() if l.startswith("vless://")]

with open("vless.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(vless))
