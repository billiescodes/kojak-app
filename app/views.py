"""
Contains main routes for the Prediction App
"""
from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

from . import app, estimator, target_names

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

d=pd.read_csv('d.csv')
#dists = pd.read_csv('../dists_20.csv')

def return_codes(input_code_list):
    my_codes = input_code_list
     
    #codes_summed=dists[my_codes].apply(lambda row: np.sum(row), axis=1)
    #codes_summed = codes_summed.sort_values(ascending=False) 
        ####### remove the ones used as input, rank 
    #ranked_codes = codes_summed.index[codes_summed.index.isin(my_codes)==False]
    #ranked_codes = ranked_codes.tolist()
    #ranked_codes = [ str(a) for a in ranked_codes[:5] ]
    
    #return ['c1','c2','c3','c4','c5'] 
    #return ranked_codes[:5]
    return ['5849', '42731', '3970', '53081', '4019', 'V4501'] 


class PredictForm(Form):
    """Fields for Predict"""

    first_code = fields.TextField('First Code:', default=4280, validators=[Required()])
    second_code = fields.TextField('Second Code:', default=4240, validators=[Required()])
    third_code = fields.TextField('Third Code:', default=78551, validators=[Required()])
    #petal_width = fields.DecimalField('Petal Width:', places=2, validators=[Required()])
    submit = fields.SubmitField('Submit')

def get_long_title(code):
    """ retrieve descriptive title of diagnostic code"""
    return d.loc[d['icd9_code']==str(code), 'long_title'].values[0]


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    prediction = None
    display_recommends = []
    iris_table = []
    code_instance = []

    #### Insert ICD9-codes into data frame, ADD long_title from diagnoses
    #df = pd.DataFrame({
    #    "icd9-code" : ['4280','4240','78551']
    #    })
    #titles=[get_long_title(a)  for a in df['icd9-code']]
    #df['diagnosis'] = titles 
    #iris_table = df.to_html( index=False)
     
    
   # now pass into html tfile see below
    #plt.plot([1, 2, 3], [4,5, 6])
    #plt.savefig('app/static/fig/myfig.png')


    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)
        
        #iris_table = df.to_html( index=False)
            #### Insert ICD9-codes into data frame, ADD long_title from diagnoses
        df = pd.DataFrame({
        "icd9-code" : ['4280','4240','78551']
                    })
        titles=[get_long_title(a)  for a in df['icd9-code']]
        df['diagnosis'] = titles
   

        iris_table = df.to_html( index=False)        


        # Retrieve values from form
        first_code = str(submitted_data['first_code'])
        second_code = str(submitted_data['second_code'])
        third_code = str(submitted_data['third_code'])

        #petal_width = float(submitted_data['petal_width'])

        # Create array from values
        #code_instance = [first_code, second_code , third_code]
        code_instance =  ['4280','4240','78551']
       
        recommended = return_codes(code_instance)
        df_r = pd.DataFrame({
            "icd9-code" : recommended
            })
        titles_r=[ get_long_title(a) for a in df_r['icd9-code']]
        df_r['diagnosis'] = titles_r 
        display_recommends = df_r.to_html( index=False)#index=[1,2,3,4,5] #index=False)


    return render_template('index.html', form=form, code_instance = code_instance, iris_table=iris_table, display_recommends=display_recommends)

