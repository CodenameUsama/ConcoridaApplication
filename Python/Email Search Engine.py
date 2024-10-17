# TO TEST THIS PROGRAM PLEASE REPLACE 'dataset' FILE DIRECTORY TO DESIRED ONE (ON LINE 41 AND LINE 44)

import tkinter as tk
import os 
import math





#   GUI 
# Defining main window
window = tk.Tk()
window.title('Simple Search Engine')
window.geometry('700x250')

search_label = tk.Label(window, text= '''Enter KEYWORD you'd like to find in the dataset:''')
search_label.grid(row=2, column=1, padx=200, pady=25)

search_entry = tk.Entry(window)
search_entry.grid(row=3, column=1, padx=200, pady=10, ipadx= 32)

# Defining result window
window2 = tk.Tk()
window2.title('Search Engine Results')
window2.geometry('265x200')

sb = tk.Scrollbar(window2)  
sb.pack(side=tk.RIGHT, fill=tk.Y)
  
listBox = tk.Listbox(window2, yscrollcommand=sb.set, height=20, width=40 )  





# Creating dictionnary
dict = {}

#   Retriving all files in dataset
for file in os.scandir(r'C:\Users\ousam\OneDrive\Bureau\Learning Python\Intro to Python\Assignement 2\dataset\\'):

    # Trimming down file name
    filename = str(file.path).replace(r'C:\Users\ousam\OneDrive\Bureau\Learning Python\Intro to Python\Assignement 2\dataset\\', '')

    # Openning and preparing filebody
    filebody = str(open(file.path, 'r').read()).upper()





#   TOKENIZE
    # Replacing special characters (ponctuation) with space
    sCharacter_list = ['#','/','\\',',','<','>','\n','.',':','$','|','{','}','[',']','?','@','!','~','=','+','(',')','-','_','*','\t',"'",'"','%','&',';','`','  ']

    for sCharacter in sCharacter_list:
        filebody = filebody.replace(sCharacter, ' ')


    # Replacing stop words with space
    sWord_list = [' A ', ' AN ', ' AND ', ' ARE ', ' AS ', ' AT ', ' BE ', ' BUT ', ' BY ', ' FOR ', ' IF ', ' IN ', ' INTO ', ' IS ', ' IT ', ' NO ', ' NOT ', ' OF ', ' ON ', ' OR ', ' SUCH ', ' THAT ', ' THE ', ' THEIR ', 'THERE', ' THESE ', ' THEY ', ' THIS ', ' TO ', ' WAS ', ' WILL ', ' WITH ', ' I ', ' M ', ' MY ', ' HIS ', ' HER ', ' S ', ' DONT ', ' T ', ' VE '] 

    for sWord in sWord_list:
        filebody = filebody.replace(sWord, ' ')

    # Splitting filebody word by word 
    filebody = filebody.split(' ')

    # Populating dictionnary (k = file name   v = tokenized word contained in the file)
    dict[filename] = filebody





#   SEARCH ENGINE
def search_engine():
    # Ask user to input a keyword
    keyword = search_entry.get().upper()

    # Defining variables
    tfIDF_dict={}
    word_found = False
    doc_count = 0

    # Count number of document containing the keyword(for IDF calculation)
    for x in range(1):
        for k in dict.keys():
            if keyword in dict[f'{k}']:
                doc_count += 1

    # Check if keyword in files
    for x in range(1):
        for k in dict.keys():
            if keyword in dict[f'{k}']:
                word_found = True

                # Counting frequency of the keyword in each file
                freq = 0
                for word in dict[f'{k}']:
                    if word == keyword: 
                        freq += 1

                # Calulating term frequency
                tf = freq/len(dict[f'{k}'])

                # Calculating inverse document frequency
                idf = math.log(1000/ doc_count)       

                # Populating dictionnary (k = file name   v = TF-IDF score)
                tfIDF_dict[f'{k}'] = round(tf*idf, 5)



    # Output when word not found
    if not word_found:
        listBox.delete(0, tk.END)
        r = str('\nThere is no such KEYWORD in this database.                         ')
        result_message = tk.Label(window, text = r)
        result_message.grid(row=5, column=1, padx=50, pady=10, ipadx= 32) 

    # Output when word found
    if word_found:  
        # Error handling
        if idf == 0:
            listBox.delete(0, tk.END)
            result_message = tk.Label(window, text = '\nThe KEYWORD could be found in every file.                         ')
            result_message.grid(row=5, column=1, padx=50, pady=10, ipadx= 32)

        else:
            listBox.delete(0, tk.END)
            result_message = tk.Label(window, text = 'The KEYWORD could be found in the next file(s):\n (Sorted by TF-IDF score where best match is first)')
            result_message.grid(row=5, column=1, padx=50, pady=10, ipadx= 32)

            for key, value in sorted(tfIDF_dict.items(), key=lambda x:x[1], reverse = True):
                r = ('Filename =', key, 'TF-IDF score=', value)
                r = str(r).replace("'", '').replace(',', '')
                listBox.insert(tk.END, r)  
            
            listBox.pack(side = tk.LEFT)  
            sb.config(command = listBox.yview)  





#   GUI(continuation)
# Search button
search_button = tk.Button(window, text='SEARCH', command=search_engine)
search_button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()