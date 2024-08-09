import urllib.request as request, json, os
from datetime import datetime

def main():
    response = request.urlopen('https://api.github.com/repos/cyclus/cyclus/releases')
    releases = json.loads(response.read())
    table_text = \
'''.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Version
     - Date
     - Zip
     - Tar'''
    for release in releases:
        version = release['tag_name']
        date = release['published_at']
        date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        date_formatted = date_object.strftime("%m/%d/%Y")
        zip_url = release['zipball_url']
        tar_url = release['tarball_url']
        table_text += f'''
   * - {version}
     - {date_formatted} 
     - `zip {version} <{zip_url}>`_
     - `tar {version} <{tar_url}>`_'''

    filename = os.path.dirname(os.path.realpath(__file__)) + '/previous/release_table.rst'

    if not os.path.isfile(filename):
        open(filename, 'x')
    with open(filename, 'w') as f:
        f.write(table_text)

if __name__ == "__main__":
    main()
