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

    - name: Commit Changes
      run: |
        git config --global user.name "${{ github.actor }}"
        git config --global user.email "${{ github.actor }}@users.noreply.github.com"
        git add output.m3u
        git commit -m "Convert JSON to M3U"
        git push
