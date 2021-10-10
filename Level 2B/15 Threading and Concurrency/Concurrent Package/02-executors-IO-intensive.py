from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time
import requests


# if the work is IO intensive, threads should be at least as fast as processes

def work():
    requests.get("https://www.nytimes.com/puzzles/sudoku/easy")
    requests.get("https://www.nytimes.com/puzzles/sudoku/medium")
    requests.get("https://www.nytimes.com/puzzles/sudoku/hard")

def compute(executor, name):
    r = range(100)
    start = time.time()
    futures = [executor.submit(work) for n in r]
    results = [futures[n].result() for n in r]
    print(f"{name} took {time.time() - start:.1f} secs")

with ThreadPoolExecutor(max_workers=50) as executor: compute(executor, "threads")
with ProcessPoolExecutor(max_workers=50) as executor: compute(executor, "processes")
