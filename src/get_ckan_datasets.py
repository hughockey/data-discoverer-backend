import json
import requests
from pymongo import ReplaceOne
import constants
from requests.compat import urljoin

def get_package_list(ckan_url):
    package_list_url = urljoin(ckan_url, 'api/3/action/package_list')
    response = requests.get(package_list_url)
    response.raise_for_status()

    package_list = json.loads(response.content)
    return package_list

def get_metadata_record(ckan_url, dataset_id):
    metadata_record_url = urljoin(ckan_url, 'api/3/action/package_show?id='+dataset_id)
    response = requests.get(metadata_record_url)
    response.raise_for_status()

    record = json.loads(response.content)
    return record

def add_operations_in_array(record, operations):
    # array of operations necessary for bulk insert
    operations.append(
        ReplaceOne({'id' : record['id']}, record, upsert=True)
    )
    

def main():
    ioos_url = 'https://data.ioos.us/'
    package_list = get_package_list(ioos_url)
    operations = []
    for metadata_record in package_list['result']:
        record = get_metadata_record(ioos_url, metadata_record)
        add_operations_in_array(record['result'], operations)

    constants.mycol_raw.bulk_write(operations)


if __name__ == '__main__':
    main()