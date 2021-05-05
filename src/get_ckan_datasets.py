import json
import requests
from requests.compat import urljoin

def get_package_list(ckan_url):
    package_list_url = urljoin(ckan_url, 'api/3/action/package_list')
    response = requests.get(package_list_url)
    response.raise_for_status()

    package_list = json.loads(response.content)
    return package_list

def get_metadata_record(ckan_url, dataset_id):
    pass

def main():
    ioos_url = 'https://data.ioos.us/'
    get_package_list(ioos_url)


if __name__ == '__main__':
    main()