import pandas as pd

df = pd.read_excel('officer_breakdown.xlsx')

accepted_words =['chief executive officer', 'chief underwriting officer', 'chief financial officer',  'chief technical officer', 
'chief risk officer', 'chief information officer', 'chief operating officer','chief operations officer',
'chief accounting officer','chief investment officer', 
'head of claims','chief of claims', 'claims head', 'senior claims officer', 'chief actuary','chief actuarial',
'chief digital transformation officer','chief digital','digital','head of counsel','general counsel',
'head of data', 'chief internal auditor', 'chief strategy and innovation officer', 'chief audit executive',
 'chief human resources officer', 'chief administrative officer', 'chief claims officer', 'chief communications officer',
 'chief sustainability officer', 'chief finance officer', 'finance director']

accepted_acronyms = ['CEO', 'CUO', 'CFO', 'CTO', 'CRO', 'CIO', 'COO','CAO']

officer_map = {'chief executive officer': 'CEO', 'chief underwriting officer': 'CUO', 'chief financial officer':
'CFO', 'chief finance officer':'CFO ', 'chief technical officer': 'CTO', 'chief risk officer':'CRO', 
'chief information officer': 'CIO', 'chief operations officer':'COO', 'chief operating officer':'COO',
'chief accounting officer': 'CAO','chief investment officer':'CInvestmentO', 'chief human resources officer': 'CHRO',
'chief strategy and innovation officer':'CSIO', 'chief audit executive':'CAE',
'chief administrative officer':'CAdminO', 'chief claims officer':'CCO', 'chief communications officer':'CComsO',
'chief sustainability officer':'CSO'
}


df.drop('simplified_role', axis=1, inplace = True)
df['simplified_role'] = ""

for i, role in enumerate(df['role']):
    simple_r = ""
    for j in accepted_words:
        if j.lower() in str(df['role'][i]).lower():
            simple_r = simple_r + " " + j
    for j in accepted_acronyms:
        if j in str(df['role'][i]):
            if j == 'CTO':
                if 'DIRECTOR' not in df['role'][i]:
                    simple_r = simple_r + " " + j
            elif 'ASSISTANT' in df['role'][i].upper():
                simple_r = ""
            else:
                simple_r = simple_r + " " + j
    for word, acronym in officer_map.items():
        simple_r = simple_r.replace(word.lower(), acronym)

    df['simplified_role'][i] = simple_r

df.to_excel('TEST.xlsx')

