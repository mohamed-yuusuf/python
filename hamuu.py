#
import json

#
data1 = {
    
    'name':'mohamed yuusuf',
    'age':'30',
    'city':'hargeisa somlialnd',
    'interest':['Travelling','Soccer','Playstation','Astronomy','Driving'],
    'is_student': True
}

with open ('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)

print("you have succesfully written to data1.jason")


with open('data1.json','r') as json_file:

    loaded_data = json.load(json_file)

print("successfully able to read data1.jason")
print(loaded_data)

####
#change the content of the json dicitionary.

loaded_data['age'] = 11
loaded_data['interest'].append('silly')

#loaded data ['interests]. remove('kmemeiemdje)

#resave the altered JSON file.
with open('data1.json','w') as json_file:

    #dump the dictionary into json file .
    json.dump(data1,json_file,indent=4)


print("data has been re-written to data1.json")
