name: Convert JSON to M3U

on:
  push:
    paths:
      - '*.json' # Trigger only on JSON file changes

jobs:
  convert:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Install Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install json2m3u

    - name: Convert JSON to M3U
      run: |
        python convert.py input.json output.m3u
        
      print('#EXTM3U')

channel_list = open('../channel_list.json')
channel_data = json.load(channel_list)
for channel in channel_list:
    grp_title = channel['group-title']
    channel_logo = channel['tvg-logo']
    channel_id = channel['tvg-id']
    channel_name = channel['channel_name']
    print(
        f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{channel_logo}" tvg-id="{channel_id}", {channel_name}')

    streaming_url = channel['url']
    grab(url)
    print(url)

    - name: Commit Changes
      run: |
        git config --global user.name "${{ github.actor }}"
        git config --global user.email "${{ github.actor }}@users.noreply.github.com"
        git add output.m3u
        git commit -m "Convert JSON to M3U"
        git push
