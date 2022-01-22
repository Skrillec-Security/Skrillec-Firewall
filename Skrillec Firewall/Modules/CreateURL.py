
# we do not use this, this is useless i don't know why i made it.
class SplitS:
    def cript(url):
        url = url.strip().replace("http://", " ")
        url = url.strip().replace("https://", " ")
        url = url.strip().replace("/", " ")
        return url