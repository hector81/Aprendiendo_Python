import urllib.request

Word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(Word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
print(words)


# https://www.it-swarm.dev/es/python/generador-de-palabras-al-azar-python/1042032096/
