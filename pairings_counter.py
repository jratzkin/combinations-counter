import pandas as pd

# read in given survey data

survey = pd.read_csv('data/from_rebecca/survey_data.csv')

num_customers = survey.shape[0]

#these are the two program lists

first_program = ['La Traviata', 'The Pearl Fishers', 'The Rape of Lucrezia', 
                 'Jesus Christ Superstar', 'Les Miserables', 'Brahms German Requiem', 
                 'Andras Schiff', 'Jonas Kaufman', 'Roomful of Teeth', 'Master Class', 
                 'Hansel and Gretel']
second_program = ['Tosca', 'Billy Budd', 'Monsters of Grace', 'South Pacific', 'Rent', 
                  'Sweeney Todd', 'Brahms German Requiem', 'Joshua Bell', 'Angela Gheorghiu', 
                  'Roomful of Teeth', 'Master Class', 'youth opera'] 

# create data frame for the survey associated with the first of two programs

first_survey = pd.DataFrame()
first_survey['customer_no'] = survey['customer_no']

counter = 0
for name in first_program: 
    first_survey[name] = survey.iloc[:,7+counter]
    counter += 1
    
#create dictionary which records number of times an item on the program 
#is paired with another item on the program

first_program_pairings = {}

for i in range (len(first_program) - 1):
    for j in range (i+1, len(first_program)):
        first_program_pairings[(first_program[i], first_program[j])] = 0
        

for i in range (num_customers):
    a_row = first_survey.iloc[i]
    for j in range (1, len(a_row) - 1):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)):
                if a_row[k] == '1':
                    first_program_pairings[(first_program[j-1], first_program[k-1])] += 1

#dictionary recording number of triples, 
#same idea as pairings but with one more for loop
      
first_program_triples = {}

for i in range (len(first_program) - 2):
    for j in range (i+1, len(first_program)-1):
        for k in range(j+1, len(first_program)):
            first_program_triples[(first_program[i], first_program[j], first_program[k])] = 0
                   
for i in range (num_customers):
    a_row = first_survey.iloc[i]
    for j in range (1, len(a_row) - 2):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-1):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)):
                        if a_row[l] == '1':
                            first_program_triples[(first_program[j-1], first_program[k-1], first_program[l-1])] += 1

#dictionary recording quadruples

first_program_quadruples = {}

for i in range (len(first_program) - 3):
    for j in range (i+1, len(first_program)-2):
        for k in range(j+1, len(first_program)-1):
            for l in range(k+1, len(first_program)):
                first_program_quadruples[(first_program[i], first_program[j], first_program[k], first_program[l])] = 0
                   
for i in range (num_customers):
    a_row = first_survey.iloc[i]
    for j in range (1, len(a_row) - 3):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-2):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)-1):
                        if a_row[l] == '1':
                            for m in range(l+1, len(a_row)):
                                if a_row[m] == '1':
                                    first_program_quadruples[(first_program[j-1], first_program[k-1], first_program[l-1], first_program[m-1])] += 1

# create data frame for the survey associated with the first of two programs 
   
second_survey = pd.DataFrame()
second_survey['customer_no'] = survey['customer_no']

counter = 0
for name in second_program:
    second_survey[name] = survey.iloc[:,18+counter]
    counter += 1

#create dictionary which records number of times an item on the program 
#is paired with another item on the program

second_program_pairings = {}

for i in range (len(second_program) - 1):
    for j in range (i+1, len(second_program)):
        second_program_pairings[(second_program[i], second_program[j])] = 0
        
       
for i in range (num_customers):
    a_row = second_survey.iloc[i]
    for j in range (1, len(a_row) - 1):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)):
                if a_row[k] == '1':
                    second_program_pairings[(second_program[j-1], second_program[k-1])] += 1

#dictionary recording number of triples, 
#same idea as pairings but with one more for loop

second_program_triples = {}

for i in range (len(second_program) - 2):
    for j in range (i+1, len(second_program)-1):
        for k in range(j+1, len(second_program)):
            second_program_triples[(second_program[i], second_program[j], second_program[k])] = 0
                   
for i in range (num_customers):
    a_row = second_survey.iloc[i]
    for j in range (1, len(a_row) - 2):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-1):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)):
                        if a_row[l] == '1':
                            second_program_triples[(second_program[j-1], second_program[k-1], second_program[l-1])] += 1

#dictionary recording quadruples

second_program_quadruples = {}

for i in range (len(second_program) - 3):
    for j in range (i+1, len(second_program)-2):
        for k in range(j+1, len(second_program)-1):
            for l in range(k+1, len(second_program)):
                second_program_quadruples[(second_program[i], second_program[j], second_program[k], second_program[l])] = 0
                   
for i in range (num_customers):
    a_row = first_survey.iloc[i]
    for j in range (1, len(a_row) - 3):
        if a_row[j] == '1':
            for k in range (j+1,len(a_row)-2):
                if a_row[k] == '1':
                    for l in range(k+1, len(a_row)-1):
                        if a_row[l] == '1':
                            for m in range(l+1, len(a_row)):
                                if a_row[m] == '1':
                                    second_program_quadruples[(second_program[j-1], second_program[k-1], second_program[l-1], second_program[m-1])] += 1
 
# print out sorted dictionaries, so we can see which pairs, triples, 
# and quadruples were chosen the most, etc.

print ('Pairings for first program:\n')
print (sorted(first_program_pairings.items(), key=lambda x:x[1], reverse=True))
print ('\n Triples for the first program:\n')
print (sorted(first_program_triples.items(), key=lambda x:x[1], reverse=True))
print ('\n Quadruples for the first programs:\n')
print (sorted(first_program_quadruples.items(), key=lambda x:x[1], reverse=True))

print ('\n Pairings for the second program:\n')
print (sorted(second_program_pairings.items(), key=lambda x:x[1], reverse=True))
print ('\n Triples for the second program:\n')
print (sorted(second_program_triples.items(), key=lambda x:x[1], reverse=True))
print ('\n Quadruples for the second programs:\n')
print (sorted(second_program_quadruples.items(), key=lambda x:x[1], reverse=True))
