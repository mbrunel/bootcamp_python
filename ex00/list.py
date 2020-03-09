import xmlrpc.client
print(xmlrpc.client.ServerProxy('https://pypi.python.org/pypi').list_packages())