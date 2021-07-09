import asyncio
import requests
import aiohttp
import time

start_time = time.time()
urls = [
    'http://www.baidu.com','http://www.sougou.com'
]
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

tasks = []

async def get_request(url):
    print('正在下载', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=header) as response:
            #text(),read(),json()
            page_text =await response.text()
    print('下载完成', url)

for url in urls:
   c = get_request(url)
   task = asyncio.ensure_future(c)
   tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()

print('总用时：', start_time-end_time)