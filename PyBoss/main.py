#dependencies
import pandas as pd

#create file names for csv

file_1 = "employee_data1.csv"

file_2 = "employee_data2.csv"

#import files
file_1_df = pd.read_csv(file_1)

file_2_df = pd.read_csv(file_2)

#print(file_2_df.head())

#combine data frames 
employeeData_df = file_1_df.append(file_2_df, ignore_index=True)
#print(employeeData_df)

#split name column

nameSplit_df = pd.DataFrame(employeeData_df.Name.str.split(' ',1).tolist(),
                    columns = ['First Name','Last Name'])

#drop old name column from df
employeeData_df = employeeData_df.drop('Name', axis=1)

#add names back to df
employeeData_df = pd.concat([employeeData_df, nameSplit_df], axis=1)


#print(employeeData_df)
#change dob format
employeeData_df['DOB'] = pd.to_datetime(employeeData_df['DOB'])
employeeData_df.dtypes
employeeData_df['DOB'] = employeeData_df['DOB'].dt.strftime('%m/%d/%Y')

#print(employeeData_df)
#hides ssn

for i in range(0,len(employeeData_df)):
    employeeData_df.iloc[i]['SSN'] = '***-**' + employeeData_df.iloc[i]['SSN'][6:]
    print('***-**' + employeeData_df.iloc[i]['SSN'][6:])


#change states
    
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employeeData_df['State'].replace(us_state_abbrev, inplace=True)
#print(employeeData_df.head())


