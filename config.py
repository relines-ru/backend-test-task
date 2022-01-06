class Config():
    FLASK_DEBUG_MODE = True
    DEFAULT_HEADERS = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    
    data = {
        'flask_restful': {
            'site': 'https://flask-restful.readthedocs.io/en/latest/',
            'site_name': '"test"',
            'base_pref': 'http://',
        }
    }

    def get(self, site, key=''):
        if key != '':
            return self.data.get(site).get(key)
        
        if key == '' and self.data.get(site) != None:
            return site
        else:
            raise ValueError("This site doesn't exist")

# Export Config instance
cfg = Config()