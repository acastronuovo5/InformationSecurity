sql_2.py


import hashlib

test= ""

goal1= "' or 1; -- "


char_array= list(string.printable)

for(a in range(len(char_array)))
    for(b in range(len(char_array)))
        for(c in range(len(char_array)))
            for(d in range(len(char_array)))
                for(e in range(len(char_array)))
                    for(f in range(len(char_array)))
                        for(g in range(len(char_array)))
                            for(h in range(len(char_array)))
                                for(i in range(len(char_array)))
                                    for(j in range(len(char_array)))
                                        for(k in range(len(char_array)))
                                            for(l in range(len(char_array)))
                                                for(m in range(len(char_array)))
                                                    for(n in range(len(char_array)))
                                                        for(o in range(len(char_array)))
                                                            for(p in range(len(char_array)))
                                                                test= char_array[a]+char_array[b]+
                                                                char_array[c]+
                                                                char_array[d]+char_array[e]+char_array[f]+
                                                                char_array[g]+char_array[h]+char_array[i]+
                                                                char_array[j]+char_array[k]+
                                                                char_array[l]+char_array[m]+
                                                                char_array[n]+
                                                                char_array[o]+char_array[p]


                                                                    if goal in test:
                                                                         return test
                                                                         
                                                                    