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


    
asyncio.run(main_race())
print("haha")
print("wow")
print("babo bumsu")