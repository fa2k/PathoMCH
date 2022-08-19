
import sys
import requests
import itertools

req = {
    "filters":{
        "op":"and",
        "content":[
            {
                "op":"=",
                "content":{
                    "field":"files.file_name",
                    "value":"{}"
                }
            },
            {
                "op":"=",
                "content":{
                    "field":"files.experimental_strategy",
                    "value":"Diagnostic Slide"
                }
            }
        ]
    },
    "format":"tsv",
    "fields":"id",
    "size":"1000"
}

manifest_file_name = sys.argv[1]
man = open(manifest_file_name)
if manifest_file_name[-4:] == ".txt":
    out = open(manifest_file_name.replace(".txt", "_new.txt"), 'w')
else:
    print("Not TXT - error")
    sys.exit(1)
    
for linenum, lin in enumerate(man):
    mf_parts = lin.split("\t")
    if linenum > 0:
        filename = mf_parts[1]
        reqcopy = dict(req)
        reqcopy['filters']['content'][0]['content']['value'] = filename
        r = requests.post('https://api.gdc.cancer.gov/files', json=reqcopy)
        header, data = r.text.splitlines()[0:2]
        idindex = header.split("\t").index("id")
        ide = data.split("\t")[idindex]
        print(ide)
        mf_parts[0] = ide
    out.write("\t".join(mf_parts))
