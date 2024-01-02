import asyncio
import aiohttp
import time

urls = [
    'https://w.forfun.com/fetch/56/5656d35727009cabea6ce79973a9702c.jpeg',
    'https://w.forfun.com/fetch/da/daf8eb568fea522f6701fb9c66378cdc.jpeg',
    'https://www.1zoom.ru/big2/541/255095-Sepik.jpg',
    'https://pibig.info/uploads/posts/2022-09/1663771039_2-pibig-info-p-zastavka-na-rabochii-stol-priroda-priroda-2.jpg',
    'https://w.forfun.com/fetch/41/41017c94e44d4bf46a20986fbf2df06b.jpeg',
    'https://w.forfun.com/fetch/ec/ec036f0f1cddedb4d0a7b1176c747982.jpeg',
    'https://gas-kvas.com/uploads/posts/2023-02/1675446661_gas-kvas-com-p-kartinki-na-fonovii-risunok-rabochego-31.jpg',
    'https://klike.net/uploads/posts/2019-11/1574605248_9.jpg',
    'https://w.forfun.com/fetch/b2/b25665013f6f4500a51470dbc3b69f65.jpeg',
    'https://i.pinimg.com/originals/d3/0f/c8/d30fc877ade673509416fa5fe9917f71.jpg'
]

def parsingNameFile(url: str) -> str:
    tokens = url.split('/')
    return tokens[-1]

async def download(url):
    download_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            file = parsingNameFile(url)
            with open(file, 'wb') as f:
                while True:
                    r = await response.content.read()
                    if not r:
                        break
                    f.write(r)
    print(f"Загрузка {file} завершена. Время загрузки {time.time() - download_start:.2f} c")

async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)

start_time = time.time()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f"Общее время: {time.time() - start_time} с")