import unicodedata

class Utilities(object):
    def validateString(string):
        try:
            if not string:
                return False
            else:
                remove = ''.join(c for c in unicodedata.normalize('NFKD', string))
                return remove.encode('ASCII', 'ignore').decode("utf-8")      
        except ValueError as err:
            print(err)
            return False