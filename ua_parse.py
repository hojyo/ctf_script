def parse_ua_str():
    fp_frame = []
    for ua_str_list in list(fp_ua_string['http_user_agent']):
        string = str(ua_str_list)
        ua = parse_ua(string)
        
        parse_dict = {'device': ua.device.family, 
                      'os': ua.os.family, 
                      'version_string': ua.os.version_string }
        fp_frame.append(parse_dict)
    dataframe = pd.DataFrame([], columns = parse_dict.keys())
    dataframe = pd.concat([dataframe, pd.DataFrame.from_dict(fp_frame)])
    return dataframe
