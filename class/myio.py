import json

json_file = "P:/UE/Megascan/Downloaded/assetsData.json"

edit_file = "P:/UE/Megascan/Downloaded/assetsData_rev2.json"


foo_dict ={"abc":{"abc0020":{"fps":24}}}

"""
def loadJson(json_file):
    with open(json_file) as data_file:
        data = json.load(data_file)
            #data = [s.encode('utf-8') for s in data_file]        
    return data

def dumpJson(json_file, dic_data):
    with open(json_file, 'w') as filename:
        json.dump(dic_data, filename, sort_keys=True, indent=4) 
"""

#json_data = loadJson(json_file)        
#print(json_data)
#dumpJson(edit_file, json_data)


class IO():
    import json

    def __init__(self, json_file):
        self.data = self.load_json(json_file)

    @staticmethod                    
    def load_json(json_file) -> dict:
        with open(json_file) as data_file:
            data = json.load(data_file)
            #data = [s.encode('utf-8') for s in data_file]        
        return data

    @staticmethod
    def dump_json(json_file, dic_data) -> None:
        with open(json_file, 'w') as filename:
            json.dump(dic_data, filename, sort_keys=True, indent=4) 


class myjson(IO):
    def __init__(self, json_file):
        #io = IO()
        #self.json_data = io.load_json(json_file)
        self.json_data = IO.load_json(json_file)

        

        
#mydb = myjson(json_file)
