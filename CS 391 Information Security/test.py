#test.py


cookie= "csrf_token"

doc_string= "xss= ; csrf_token= 2398yhm983279 ; other= "
c_split= doc_string.replace(' ', '').split(';')
print(c_split)


for i in range(len(c_split)):
    if cookie in c_split[i]:
        print(c_split[i])

        ncookie=c_split[i]
        ncookie.split('=')
        print(ncookie)

        value= ncookie[1]
        print(value)

#print(c_split) 