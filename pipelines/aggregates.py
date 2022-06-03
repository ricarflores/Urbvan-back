class Aggregations(object):
    def getAllUsers(page, limit):
        try:
            pipeline = []
            filter = {
                '$match':{
                    "active": True
                }
            }
            pipeline.append(filter)
            skip = (int(page) -1) * int(limit)
            skipMatch = {
                '$skip': skip
            }
            pipeline.append(skipMatch)
            limit = {
                '$limit': int(limit)
            }
            pipeline.append(limit)
            project = {
                '$project':{
                    '_id':{
                        '$toString': '$_id'
                    },
                    'dateEntry': {
                        '$dateToString':{
                            'date': "$dateEntry",
                            'format': '%Y-%m-%d'
                        }
                    },
                    'uniqueId': 1,
                    'last_name': 1,
                    'name': 1
                }
            }
            pipeline.append(project)
            return pipeline
        except Exception as err:
            print(err)
            return []