import pandas as pd

# read in given survey data

survey = pd.read_csv('data/from_rebecca/survey_data.csv')

# separate out sample3_2 == 1 and sample3_2 == 3

survey1 = survey[survey['sample3_2'] == 1]
survey3 = survey[survey['sample3_2'] == 3]

#num_customers = survey.shape[0]

#these are the two program lists

first_program = ['La Traviata', 'The Pearl Fishers', 'The Rape of Lucrezia', 
                 'Jesus Christ Superstar', 'Les Miserables', 'Brahms German Requiem', 
                 'Andras Schiff', 'Jonas Kaufman', 'Roomful of Teeth', 'Master Class', 
                 'Hansel and Gretel']
second_program = ['Tosca', 'Billy Budd', 'Monsters of Grace', 'South Pacific', 'Rent', 
                  'Sweeney Todd', 'Brahms German Requiem', 'Joshua Bell', 'Angela Gheorghiu', 
                  'Roomful of Teeth', 'Master Class', 'youth opera'] 

# create data frames for the survey associated with the first of two programs

first_survey1 = pd.DataFrame()
first_survey1['customer_no'] = survey1['customer_no']
first_survey3 = pd.DataFrame()
first_survey3['customer_no'] = survey3['customer_no']

counter = 0
for name in first_program: 
    first_survey1[name] = survey1.iloc[:,7+counter]
    counter += 1

counter = 0
for name in first_program: 
    first_survey3[name] = survey3.iloc[:,7+counter]
    counter += 1

#dictionary recording number of triples
      
first_program_triples1 = {}

for i in range (len(first_program) - 2):
    for j in range (i+1, len(first_program)-1):
        for k in range(j+1, len(first_program)):
            first_program_triples1[(first_program[i], first_program[j], first_program[k])] = 0
                   
for i in range (survey1.shape[0]):
    a_row = first_survey1.iloc[i]
    for j in range (1, len(a_row) - 2):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-1):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)):
                        if a_row[l] == '1':
                            first_program_triples1[(first_program[j-1], first_program[k-1], first_program[l-1])] += 1

first_program_triples3 = {}

for i in range (len(first_program) - 2):
    for j in range (i+1, len(first_program)-1):
        for k in range(j+1, len(first_program)):
            first_program_triples3[(first_program[i], first_program[j], first_program[k])] = 0
                   
for i in range (survey3.shape[0]):
    a_row = first_survey3.iloc[i]
    for j in range (1, len(a_row) - 2):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-1):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)):
                        if a_row[l] == '1':
                            first_program_triples3[(first_program[j-1], first_program[k-1], first_program[l-1])] += 1

# create data frames for the survey associated with the first of two programs 

second_survey1 = pd.DataFrame()
second_survey1['customer_no'] = survey1['customer_no']
second_survey3 = pd.DataFrame()
second_survey3['customer_no'] = survey3['customer_no']

counter = 0
for name in second_program: 
    second_survey1[name] = survey1.iloc[:,7+counter]
    counter += 1

counter = 0
for name in second_program: 
    second_survey3[name] = survey3.iloc[:,7+counter]
    counter += 1

#dictionary recording number of triples
      
second_program_triples1 = {}

for i in range (len(second_program) - 2):
    for j in range (i+1, len(second_program)-1):
        for k in range(j+1, len(second_program)):
            second_program_triples1[(second_program[i], second_program[j], second_program[k])] = 0
                   
for i in range (survey1.shape[0]):
    a_row = first_survey1.iloc[i]
    for j in range (1, len(a_row) - 2):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-1):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)):
                        if a_row[l] == '1':
                            second_program_triples1[(second_program[j-1], second_program[k-1], second_program[l-1])] += 1

second_program_triples3 = {}

for i in range (len(second_program) - 2):
    for j in range (i+1, len(second_program)-1):
        for k in range(j+1, len(second_program)):
            second_program_triples3[(second_program[i], second_program[j], second_program[k])] = 0
                   
for i in range (survey3.shape[0]):
    a_row = second_survey3.iloc[i]
    for j in range (1, len(a_row) - 2):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-1):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)):
                        if a_row[l] == '1':
                            second_program_triples3[(second_program[j-1], second_program[k-1], second_program[l-1])] += 1

# print out sorted dictionaries, so we can see which triples, 
# were chosen the most, etc.


print ('\n Triples for the first program, sample3_2 == 1:\n')
print (sorted(first_program_triples1.items(), key=lambda x:x[1], reverse=True))
print ('\n Triples for the first program, sample3_2 == 3:\n')
print (sorted(first_program_triples3.items(), key=lambda x:x[1], reverse=True))

print ('\n Triples for the second program, sample3_2 == 1:\n')
print (sorted(second_program_triples1.items(), key=lambda x:x[1], reverse=True))
print ('\n Triples for the second program, sample3_2 == 3:\n')
print (sorted(second_program_triples3.items(), key=lambda x:x[1], reverse=True))
