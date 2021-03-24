# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json 
import logging
  
# Opening JSON file 


# Iterating through the json 
# list 
#for i in data: 
    #print(i) 
  
# Closing file 

logging.basicConfig(filename='/Users/joel_ena/foundations/foundations-sample-website/color_check/data/log.txt', filemode='w',format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logging.info("admin has logged in ")


def get_color_code(color_name):
    
    with open('color_check/data/css-color-names.json', "r") as data:
  
    # returns JSON object as  
    # a dictionary 
        dictionary = json.load(data) 

    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    
        hex_code= dictionary.get(color_name,"this color doesnt exist")

    return (hex_code)
         
    

