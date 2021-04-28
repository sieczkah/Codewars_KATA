"""https://www.codewars.com/kata/51646de80fd67f442c000013"""

def strip_url_params(url, params_to_strip=[]):
    splitted_url = url.split('?')
    if len(splitted_url) == 1:
        return url
    else:
        domain = splitted_url[0]
        params_str = splitted_url[1].split('&')
        params_str = list(map(lambda x: x.split('='), params_str))
        params_list, params = [], []
        
        for param, val in params_str:
            if param not in params_list + params_to_strip:
                params_list.append(param)
                params.append(f'{param}={val}')
        return domain + '?' + '&'.join(params) if params else domain

