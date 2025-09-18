from core import methods_json, methods_urlencoded, methods_get

def try_bypass(url: str, req: str, token = None):
    bypass_list = [0,0,0,0,0]
    if "GET" in req[0:req.find("\n")]:
        if "?" in url:
            url = url[0:url.find("?")]
        bypass_list[0] = methods_get.bypass_method_1_get(url, req, token)
        bypass_list[1] = methods_get.bypass_method_2_get(url, req, token)
        bypass_list[2] = methods_get.bypass_method_3_get(url, req, token)
        bypass_list[3] = methods_get.bypass_method_4_post(url, req, token)
        bypass_list[4] = methods_get.bypass_method_4_put(url, req, token)
    elif "content-type: application/json" in req.lower():
        bypass_list[0] = methods_json.bypass_method_1_json(url, req, token)
        bypass_list[1] = methods_json.bypass_method_2_json(url, req, token)
        bypass_list[2] = methods_json.bypass_method_3_json(url, req, token)
        bypass_list[3] = methods_json.bypass_method_4_json_get(url, req, token)
        bypass_list[4] = methods_json.bypass_method_4_json_put(url, req, token)

    elif "content-type: application/x-www-form-urlencoded" in req.lower():
        bypass_list[0] = methods_urlencoded.bypass_method_1_urlencoded(url, req, token)
        bypass_list[1] = methods_urlencoded.bypass_method_2_urlencoded(url, req, token)
        bypass_list[2] = methods_urlencoded.bypass_method_3_urlencoded(url, req, token)
        bypass_list[3] = methods_urlencoded.bypass_method_4_urlencoded_get(url, req, token)
        bypass_list[4] = methods_urlencoded.bypass_method_4_urlencoded_put(url, req, token)

    return bypass_list