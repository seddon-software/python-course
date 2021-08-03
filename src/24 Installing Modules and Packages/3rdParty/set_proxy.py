def setProxy(url):
    """example call:
          setProxy("http://wwwcache.rl.ac.uk:8080")
    """
    os.environ["HTTP_PROXY"] = url

setProxy("http://wwwcache.rl.ac.uk:8080")