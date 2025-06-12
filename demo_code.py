
def first_non_repating_char(string):
    for j in range(len(string)):
        string2 = string
        string2 = string2[:j] + string2[j+1:]
        if string[j] not in string2 :
            return string2[j]

    return None

print(first_non_repating_char("abababab"))
        
    
    
    


def wastebag_replicate_in_cpcb(data):
    file_name = data.get("file_name", None)
    if not file_name:
        return {"status": "Failed", "message": "File name not provided"}
    file = os.path.normpath(file_name)
    if not os.path.exists(file):
        return {"status": "Failed", "message": "File does not exist"}
    bson_data = dir.readJsonData(file)
    data_list = bson_data    
    for json_data in data_list:
      
        json_data.pop("_id", None)
        doc_dtno = json_data["dtno"]
        
        if doc_dtno == "45684":
            json_data["olddtno"] = "45710"
        if doc_dtno == "45685":
            json_data["olddtno"] = "45711"
        if doc_dtno == "45686":
            json_data["olddtno"] = "45712"
        if doc_dtno == "45687":
            json_data["olddtno"] = "45713"
        if doc_dtno == "45688":
            json_data["olddtno"] = "45714"
        if doc_dtno == "45689":
            json_data["olddtno"] = "45715"
        if doc_dtno == "45690":
            json_data["olddtno"] = "45716"
        if doc_dtno == "45691":
            json_data["olddtno"] = "45717"
        if doc_dtno == "45692":
            json_data["olddtno"] = "45718"
        if doc_dtno == "45693":
            json_data["olddtno"] = "45719"
        json_data.pop("dtno",None)
        json_data.pop("wstbgid",None)
        json_data.pop("cdt",None)
        json_data.pop("ctm",None)
        json_data.pop("user_scanning_in_hcf",None)
        json_data.pop("msg",None)
        json_data.pop("dn",None)
        json_data.pop("tmtkn",None)
        json_data.pop("wt",None)
        json_data.pop("tmno",None)
        json_data.pop("in",None)
        
        
        bag_recorded_cpcb = my_urllib.send_wastebag(json_data)


    