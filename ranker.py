import pandas as pd
import numpy as np
import pickle

def main():

    d = pd.read_csv('../d.csv')

    mycodes =  ['4280','4240','78551']
    print d[:2] 
   
    #with open('dists_20.pkl', "rb") as f:
    #    dists = pickle.load(f)
  
    dists = pd.read_csv('dists_20.csv')

    #df = pd.read_pickle('dists_20.pkl') 
    #df = pd.DataFrame(dists)
    print "pickle shit here" 
    print dists.iloc[0:4,0:4]
    print "yeahhhh" 


def rank_indiv(patient_list,n, k):
    #### PRINT OUT THE FIRST k CODES
    my_codes = list(df_new[df_new.hadm_id==patient_list[n]]['icd9_code'])
    #print (my_codes)
    print " \t testing first {} codes ".format(k)
    for a, code in enumerate(my_codes): # my_codes[:k]
        if a == k: print " "
        if code not in list(d['icd9_code']):
            print "not here"
        else: 
            print code, "\t {}) ".format(a+1),  d.loc[d['icd9_code']== code, 'long_title'].values[0] 
           
    codes_summed=dists[my_codes].apply(lambda row: np.sum(row), axis=1)
    codes_summed = codes_summed.sort_values(ascending=False)
    
    ####### remove the ones used as input, rank 
    ranked_codes = codes_summed.index[codes_summed.index.isin(my_codes)==False]
    ranked_codes = ranked_codes.tolist()
    print " \n\t testing recommended {} codes".format(k) 
    print ranked_codes[:k]
    for a,code in enumerate(ranked_codes[:5]):
        if code not in d['icd9_code'].values: 
            print "\t code not here"
        else:
            print "\t{})".format(a+1), d.loc[d['icd9_code']==code, 'long_title'].values[0]    
    return ranked_codes

#End of file stuff
if __name__=='__main__':
  main()

