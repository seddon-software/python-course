import cothread

# simulate a slow WebServer
class WebServer:
    def request(cmd, url):
        cothread.Sleep(10)
        if url == "site1.com": return "package1"
        if url == "site2.com": return "package2"
        if url == "site3.com": return "package3"

cache = {}
rlock = cothread.RLock()

def get_stuff(url):
    with rlock:  # critical section (only one cothread at a time)
        if url in cache:
            print(f"data for {url} already in cache")
            return cache[url]
        stuff = WebServer.request('GET', url)
        print(f"data for {url} has been added to cache")
        cache[url] = stuff
    return stuff

def get_package(url):
    print(get_stuff(url))

def do_something_else(n):
    print("cothread running concurrently")
    for i in range(25):
        print(f"{n}", end="")
        cothread.Sleep(0.25)
    print()

# cothreads t4 and t5 can run concurrently with t1, t2 and t3
# t1, t2 and t3 only call the WebServer once because of the lock
t1 = cothread.Spawn(get_package, "site2.com")
t2 = cothread.Spawn(get_package, "site2.com")
t3 = cothread.Spawn(get_package, "site2.com")
t4 = cothread.Spawn(do_something_else, 4)
t5 = cothread.Spawn(do_something_else, 5)

t1.Wait()    
t2.Wait()    
t3.Wait()    
t4.Wait()    
t5.Wait()    
