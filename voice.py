from resemble import Resemble
Resemble.api_key('RESEMBLE_KEY')

voice = 'sonic'

response = Resemble.v2.voices.create(name, dataset_url="http://../dataset.zip", callback_uri="http://example.com/cb")
voice = response['item']


