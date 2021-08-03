from urllib.parse import urlparse
o = urlparse(
    'http://www.cwi.nl:80/ContextRoot/Mapping;p1=9,p2=3?name1=value1&name2=value2#section1'
)
print(o)
print(f"scheme:   {o.scheme}")
print(f"hostname: {o.hostname}")
print(f"port:     {o.port}")
print(f"netloc:   {o.netloc}")
print(f"path:     {o.path}")
print(f"params:   {o.params}")
print(f"query:    {o.query}")
print(f"fragment: {o.fragment}")


