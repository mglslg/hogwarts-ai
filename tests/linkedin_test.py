from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('suolongga1988@gmail.com', '****')

# GET a profile
profile = api.get_profile('billy-g')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('billy-g')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('1234asc12304')
