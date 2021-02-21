import asyncio, random, time


async def fetch_url(url):
    print(f"~ executing fetch_url({url})")
    t = time.perf_counter()
    await asyncio.sleep(random.randint(1, 5))
    print(f"time of fetch_url({url}): {time.perf_counter() - t:.2f}s")
    return f"<em>fake</em> page html for {url}"

async def analyze_sentiment(html):
    print(f"~ executing analyze_sentiment('{html}')")
    t = time.perf_counter()
    await asyncio.sleep(random.randint(1, 5))
    r = {"positive": random.uniform(0, 1)}
    print(f"time of analyze_sentiment('{html}'): {time.perf_counter() - t:.2f}s")
    return r

urls = [
    "https://1",
    "https://2",
    "https://3",
    "https://4",
    "https://5",
    "https://6",
    "https://7",
    "https://8",
    "https://9",
    "https://10",
    "https://11",
    "https://12",
]
extracted_data = {}

async def handle_url(url):
    html = await fetch_url(url)
    extracted_data[url] = await analyze_sentiment(html)

async def main():
    t = time.perf_counter()
    await asyncio.gather(*(handle_url(url) for url in urls))
    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")

async def main_race():
    t = time.perf_counter()
    await asyncio.wait([handle_url(url) for url in urls],
                       return_when=asyncio.FIRST_COMPLETED)
    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")

async def main_sequential():
    t = time.perf_counter()
    for url in urls:
        await handle_url(url)
    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")

async def main_concurrent():
    t = time.perf_counter()
    tasks = [asyncio.create_task(handle_url(url))
             for url in urls]
    for task in tasks:
        await task
    print("> extracted data:", extracted_data)
    print(f"time elapsed: {time.perf_counter() - t:.2f}s")

asyncio.run(main_concurrent())
