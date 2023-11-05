import asyncio

print("------------使用run_forever()方法：-----------------------------")


async def func(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')


def call_result(future):
    print(future.result())
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    future.add_done_callback(call_result)        # 注意这行
    try:
        loop.run_forever()
    finally:
        loop.close()
