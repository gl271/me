TODO: Reflect on what you learned this week and what is still unclear.

By looking into previous weeks exercises it helped to recall what to do.

#with auto opens and closes for the write json files and all that jazz

the other way if rewritten
fname ="dict_cache.json"
dumped = json.dump(dict_fill, dict)
dict = open(fname, "r")
dict.write (dumped)
dict.close()

    fname ="dict_cache.json"
    dumped = make_filler_text_dictionary
    dict = open(fname, "w")
    dict.write (dumped)
    dict.close()
