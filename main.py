# FILE I/O JSON DEMO by MR. V

# Import JSON module
import json

# JSON stands for JavaScript Object Notation
# It is a notation for representing data
# JSON may be used to convert data to a string and vice versa
# JSON supports all basic data, lists and dictionaries (not objects)

# The dumps() method will convert data to a json string
data = [
    {"x": 11, "y": 1}, 
    {"x": 21, "y": 2}, 
    {"x": 31, "y": 3}]
json_string = json.dumps(data)
print("DATA AS A JSON STRING")
print(json_string)

# # The data as a JSON string may be easily saved to a file
file = open("data.txt", "w")
file.write(json_string)
file.close()


# Load a JSON string from a file
file = open("data2.txt", "r")
json_string_from_file = file.read()
file.close()

# the loads() method will convert a json string to data
data2 = json.loads(json_string_from_file)
print("DATA CONVERTED FROM JSON STRING FROM FILE")
print(data2)
for data in data2:
    print(data)
