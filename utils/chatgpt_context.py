import json
import os


def getConext(id):
    folder_path = './data/'
    file_path = folder_path + id + '.json'

    if not os.path.isfile(file_path):
        with open(folder_path + 'template.json', 'r') as tem:
            json_data = json.load(tem)

            tem.close()

            return json_data
    else:
        with open(file_path, 'r') as ct:
            json_data = json.load(ct)

            ct.close()
            return json_data


def updateConext(id, req, res):
    folder_path = './data/'
    file_path = folder_path + id + '.json'
    file_path_letter = folder_path + id + 'letters.json'
    json_data = None

    if not os.path.isfile(file_path):
        with open(folder_path + 'template.json', 'r') as tem:
            json_data = json.load(tem)
            tem.close()
    else:
        with open(file_path, 'r') as cr:
            json_data = json.load(cr)
            cr.close()

    with open(file_path, 'w+') as ct:
        json_add_user = {"role": "user", "content": req}
        json_data.append(json_add_user)
        json_add_assistant = {"role": "assistant", "content": res}
        json_data.append(json_add_assistant)

        json.dump(json_data, ct, indent=4)
        ct.close()

    msg = [res]
    if os.path.isfile(file_path_letter):
        with open(file_path_letter, 'r') as cl:
            msg = json.load(cl)
            msg.append(res)
            cl.close()

    with open(file_path_letter, 'w+') as cl:
        json.dump(msg, cl, indent=4)
        cl.close()


def getLastLetter(id):
    folder_path = './data/'
    file_path_letter = folder_path + id + 'letters.json'
    if os.path.isfile(file_path_letter):
        with open(file_path_letter, 'r') as cl:
            msg = json.load(cl)
            return msg[-1]

    else:
        return None
