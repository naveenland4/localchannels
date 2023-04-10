#! /usr/bin/python3
import os
import json
import requests


print('#EXTM3U')

channel_list = open('../channel_list.json')
channel_data = json.load(channel_list)
for channel in channel_data:
    grp_title = channel['group-title']
    channel_logo = channel['tvg-logo']
    channel_id = channel['tvg-id']
    channel_name = channel['channel_name']
    print(
        f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{channel_logo}" tvg-id="{channel_id}", {channel_name}')

    streaming_url = channel['url']
    grab(url)

m3u8_channel_list = open('../m3u8_channel_list.json')
m3u8_channel_data = json.load(m3u8_channel_list)
for channel in m3u8_channel_data:
    grp_title = channel['group-title']
    channel_logo = channel['tvg-logo']
    channel_id = channel['tvg-id']
    channel_name = channel['channel_name']
    print(
        f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{channel_logo}" tvg-id="{channel_id}", {channel_name}')

    url = channel['url']
    print(url)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
