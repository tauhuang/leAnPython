# -*-: UTF-8 -*-


import json


def convert_to_str(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ convert_to_str(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            convert_to_str(key, ignore_dicts=True): convert_to_str(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data
    

def load_json_from_file(filep):
    # read a file which saved json string, and convert to dict
    try:
        file_handler = open(filep, 'rt')
    except IOError:
        file_handler.close()
        raise SystemExit(" ".join(["Can't read", file_name]))

    json_obj = convert_to_str(json.load(file_handler, object_hook=convert_to_str), ignore_dicts=True)
    file_handler.close()
    return json_obj


def load_json_from_str(str):
    # convert json string to dict
    return convert_to_str(json.loads(str))
