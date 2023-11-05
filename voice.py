from resemble import Resemble
Resemble.api_key('5vzXHXdX7kGGcp9tYRedKAtt')

name = 'sonic'

response = Resemble.v2.voices.create(name, dataset_url="http://../dataset.zip", callback_uri="http://example.com/cb")
voice = response['item']


