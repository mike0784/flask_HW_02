import time

import requests
from multiprocessing import Process, Pool

import threading

import os

import sys

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

files = []

def parsingNameFile(url: str) -> str:
    tokens = url.split('/')
    return tokens[-1]

def download(url):
    global files
    file = parsingNameFile(url)
    files.append(file)
    download_start = time.time()
    r = requests.get(url)
    with open(file, 'wb') as f:
        f.write(r.content)
    print(f"Загрузка {file} завершена. Время загрузки {time.time() - download_start:.2f} c")

def deleteFile() -> None:
    global files
    for file in files:
        os.remove(file)
    files.clear()

threads = []
processes = []

if __name__ == '__main__':
    l = len(sys.argv)
    if l != 1:
        urls = sys.argv[1:]
        print('urls=',urls)
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Общее время: {time.time() - start_time} с")
    deleteFile()

    start_time = time.time()
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print(f"Общее время: {time.time() - start_time} с")
    deleteFile()

