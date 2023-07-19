# check status of many webpages
import asyncio
import time
from urllib.parse import urlsplit

# get HTTPS status of a webpage
async def get_status(url):
    # split url into components
    url_parsed = urlsplit(url)
    print(f'{time.ctime()} fetch {url}')
    # open connection 
    if url_parsed.scheme == 'https':
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 443, ssl = True)
    else:
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 80)
    # send GET request 
    query = f'GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n'
    # write query to socket 
    writer.write(query.encode())
    # wait for the bytes to be written to the socket
    await writer.drain()
    # send the single line response 
    response = await reader.readline()
    # close the connection 
    writer.close()
    # decode and strip white space 
    status = response.decode().strip()
    print(f'{time.ctime()} done {url}')
    # return the response 
    return status

# main coroutine 
async def main():
    # list of 10 websites to check 
    sites = ['https://www.google.com/',
             'https://www.youtube.com/',
             'https://www.facebook.com/',
             'https://twitter.com/',
             'https://www.instagram.com/',
             'https://www.baidu.com/',
             'https://wikipedia.com',
             'https://yandex.ru',
             'https://yahoo.com',
             'https://www.whatsapp.com'
            ]
    # check the status of all websites
    for url in sites:
        # get the status for the url 
        status = await get_status(url)
        # report the url and its status 
        print(f'{time.ctime()} {url:30}:\t{status}')

# run the asynchonous program 
asyncio.run(main())

# Running Result 
# Wed Jul 19 14:40:30 2023 fetch https://www.google.com/
# Wed Jul 19 14:40:31 2023 done https://www.google.com/
# Wed Jul 19 14:40:31 2023 https://www.google.com/       :        HTTP/1.1 200 OK
# Wed Jul 19 14:40:31 2023 fetch https://www.youtube.com/
# Wed Jul 19 14:40:31 2023 done https://www.youtube.com/
# Wed Jul 19 14:40:31 2023 https://www.youtube.com/      :        HTTP/1.1 200 OK
# Wed Jul 19 14:40:31 2023 fetch https://www.facebook.com/
# Wed Jul 19 14:40:32 2023 done https://www.facebook.com/
# Wed Jul 19 14:40:32 2023 https://www.facebook.com/     :        HTTP/1.1 302 Found
# Wed Jul 19 14:40:32 2023 fetch https://twitter.com/
# Wed Jul 19 14:40:32 2023 done https://twitter.com/
# Wed Jul 19 14:40:32 2023 https://twitter.com/          :        HTTP/1.1 302 Found
# Wed Jul 19 14:40:32 2023 fetch https://www.instagram.com/
# Wed Jul 19 14:40:32 2023 done https://www.instagram.com/
# Wed Jul 19 14:40:32 2023 https://www.instagram.com/    :        HTTP/1.1 302 Found
# Wed Jul 19 14:40:32 2023 fetch https://www.baidu.com/
# Wed Jul 19 14:40:33 2023 done https://www.baidu.com/
# Wed Jul 19 14:40:33 2023 https://www.baidu.com/        :        HTTP/1.1 200 OK
# Wed Jul 19 14:40:33 2023 fetch https://wikipedia.com
# Wed Jul 19 14:40:33 2023 done https://wikipedia.com
# Wed Jul 19 14:40:33 2023 https://wikipedia.com         :        HTTP/1.1 400 Bad Request
# Wed Jul 19 14:40:33 2023 fetch https://yandex.ru
# Wed Jul 19 14:40:34 2023 done https://yandex.ru
# Wed Jul 19 14:40:34 2023 https://yandex.ru             :        HTTP/1.1 400 Bad request
# Wed Jul 19 14:40:34 2023 fetch https://yahoo.com
# Wed Jul 19 14:40:35 2023 done https://yahoo.com
# Wed Jul 19 14:40:35 2023 https://yahoo.com             :        HTTP/1.0 400 Invalid HTTP Request
# Wed Jul 19 14:40:35 2023 fetch https://www.whatsapp.com
# Wed Jul 19 14:40:35 2023 done https://www.whatsapp.com
# Wed Jul 19 14:40:35 2023 https://www.whatsapp.com      :        HTTP/1.1 400 Bad Request

