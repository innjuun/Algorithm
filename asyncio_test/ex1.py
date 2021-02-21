import asyncio


@asyncio.coroutine
def print_every_second_coroutine(type):
    "Print seconds"
    while True:
        for i in range(10):
            print(i, "s (corotine {})".format(type))
            yield from asyncio.sleep(1)
        loop = asyncio.get_event_loop()
        loop.stop()


def print_every_seconds_callback(i):
    print(i, "s (callback)")
    loop = asyncio.get_event_loop()
    loop.call_later(1.0, print_every_seconds_callback, i + 1)


def print_every_seconds_callback_to_coroutine():
    asyncio.ensure_future(print_every_second_coroutine("B"))


loop = asyncio.get_event_loop()
loop.call_soon(print_every_seconds_callback, 0)
loop.call_soon(print_every_seconds_callback_to_coroutine)
asyncio.ensure_future(print_every_second_coroutine("A"))

loop.run_forever()
loop.close()
