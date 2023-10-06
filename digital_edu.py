#створи тут свій індивідуальний проект!
import pandas as pd

df = pd.read_csv("train.csv")

print(df[['occupation_type','occupation_name','career_start','career_end']].tail(20))

df.drop(['id','education_status',
      'life_main','people_main','city','last_seen',
      'occupation_type','occupation_name','career_start', 
      'career_end'],
      axis=1, inplace=True)



def set_age(age: str):
     try:
          age = age.split('.')
          year = int(age[2])
     except:
          year = pd.NA
     return year

df['bdate'] = df['bdate'].apply(set_age)   
df['bdate'].fillna(df['bdate'].median(), inplace=True) 

#print(df.bdate.tail(25))

#df.info()



print(df.langs.tail(25))

def set_langs(langs: str):
     langs=langs.replace('Русский;','')
     langs=langs.replace('Русский','')
     
     if langs == 'False' or langs == '':
          return ['English']
     return langs.split(';')

df.langs = df.langs.apply(set_langs)

df.education_form.fillna('Full-time', inplace=True)

columns_names=list(pd.get_dummies(df.education_form).columns)

df[columns_names] = pd.get_dummies(df.education_form)

print(df[columns_names].head(50))

df.drop('education_form', axis=1, inplace=True)

df.info()