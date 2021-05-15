import urllib.request

connection = urllib.request.urlopen('http://localhost:8983/solr/collection_name/select?q=cheese&wt=python')
response = eval(connection.read())

print (response['response']['numFound'], "documents found.")