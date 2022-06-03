config = {
    'db':{
        'user': 'KumaBattler',
        'address': 'cluster0.yangws4.mongodb.net',
        'port': '27017',
        'password': '$kumaNeko1408',
        'info': '?retryWrites=true&w=majority',
        'option': '{ useNewUrlParser: true }',
        'db':'develop',
        'collection': 'users'
    }
}

if 'urlMongo' not in config['db']:
    if config['db']['user'] is not '':
        config['db']['urlMongo'] = 'mongodb+srv://' + config['db']['user'] + ':' + config['db']['password'] + '@' + config['db']['address'] + '/'+ config['db']['info']
    else:
        config['db']['urlMongo'] = 'mongodb://' + config['db']['address'] + ':' + config['db']['port'] + '/'