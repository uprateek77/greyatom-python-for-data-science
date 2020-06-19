# --------------
#Code starts here

#Function to read file
def read_file(path):

#Opening of the file located in the path in 'read' mode
#Reading of the first line of the file and storing it in a variable
    file = open(path,'r')
#Closing of the file
    sentence = file.readline()
    file.close()
#Returning the first line of the file
    return sentence

#Calling the function to read file
sample_message = read_file(file_path)
#Printing the line of the file
print(sample_message)

#Function to fuse message
def fuse_msg(message_a,message_b):
#Integer division of two numbers
    quotient = int(message_b)//int(message_a)

#Returning the quotient in string format
    return quotient
#Calling the function to read file
message_1 = read_file(file_path_1)
print(message_1)
#Calling the function to read file
message_2 = read_file(file_path_2)
print(message_2)

#Calling the function 'fuse_msg'
secret_msg_1 = fuse_msg(message_1,message_2)

#Printing the secret message
print(secret_msg_1)

#Function to substitute the message
def substitute_msg(message_c):
#If-else to compare the contents of the file
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    else:
        sub = 'Marine Biologist'
#Returning the substitute of the message
    return sub

#Calling the function to read file
message_3 = read_file(file_path_3)
print(message_3)


#Calling the function 'substitute_msg'

secret_msg_2=substitute_msg(message_3)
#Printing the secret message
print(secret_msg_2)


#Function to compare message
def compare_msg(message_d,message_e):
#Splitting the message into a list
    a_list = message_d.split(" ")

#Splitting the message into a list
    b_list = message_e.split(" ")
#Comparing the elements from both the lists
    c_list =[item for item in a_list if item not in b_list]
#Combining the words of a list back to a single string sentence
    final_msg = ' '.join(c_list)
# str1 = ''.join(str(e) for e in list1)
#Returning the sentence
    return final_msg
#Calling the function to read file
message_4 = read_file(file_path_4)
print(message_4)

#Calling the function to read file
message_5= read_file(file_path_5)
print(message_5)
def extract_msg(message_f):
    a_list=message_f.split(" ")
    even_word=lambda x: (len(x)%2==0)
    b_list=list(filter(even_word,a_list))
    final_msg = ' '.join(b_list)
    return final_msg
message_6= read_file(file_path_6)
print (message_6)

secret_msg_3= compare_msg(message_4, message_5)
print(secret_msg_3)

secret_msg_4=extract_msg(message_6) 
print(secret_msg_4)   
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
print(message_parts)
# define the path where you
final_path= user_data_dir + '/secret_message.txt'
secret_msg = ' '.join([str(i) for i in message_parts])
def write_file(secret_msg,path):
    file = open(path,'a+')
    file.write(secret_msg)
    file.close()
write_file(secret_msg,final_path)
print(secret_msg)

