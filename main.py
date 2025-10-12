import urllib.request
import os


def main():
    '''
    #print("Hello! Red Team Nation!")
    sample_string = "RedTeam National! @&- 100054"
    sample_int = 4444
    sample_float = 3.14
    sample_bool = True
    sample_none = None

    tmp_string = '5'
    result = 5 + int(tmp_string)
    #print(result)
    #print("type of result is:",type(result))
    #print("type of tmp_string is:",type(tmp_string))
    tmp_string=int(tmp_string)
    #print("type of tmp_string is:",type(tmp_string))
    #print("sample print - {0}, {1}, {2}, {3}, {4}".format(sample_string,sample_int,sample_float,sample_bool,sample_none))
    
    ##operators##
    tmp=10
    tmp/=2.5
    print(tmp)
   
    ##if/else
    age = 26
    name = 'Brandon'
    male = True

    if('Brandon' in name): #in this mean contain , == equall exact match!
        print("Here!")
    if(age == 26):
        print("Of Age!")
    if('Brandon'==name and age >=21):
        print("Boo!")
     
    
    ##Loops##
    tmp_str = 'Red'

    for char in tmp_str:
        print('{0} - {1}'.format(char,tmp_str))

    for x in range(10): # range(10) - start from 0 until 9
        print(x)
    
    print("\n")
    i=0
    while(i<=10):
        if (i==0):
            print(i)
            continue #continue - restart the loop until here each time
        if(i==5):
            break #break - out you from loop 
        i+=1
    

    ##Dictionary##
    tmp_dict = {
        'Name':'Brandon',
        'Age':26
    }

    print(tmp_dict['Name'])
    print(tmp_dict['Age'])
    if('Name' in tmp_dict):
        print("Found the key - Name")

    print("\n")
    #print key
    print("Keys:")
    for key in tmp_dict:
        print(key)

    print("\n")
    print("values:")
    for value in tmp_dict.values():
        print(value)

    print('\nPrint Values')
    for key,value in tmp_dict.items():
        print(f"Key: {key}\nValue: {value}")
    

    ##List##
    tmp_list = ['Brandon', 26 , 'RedTeam Nation']
    tmp_list[0]=25
    print(f"List one is : {tmp_list[0]}")
    '''
    print(os.system('dir'))

    response = urllib.request.urlopen('https://google.com')
    html = response.read()
    print(html)
    
if __name__== '__main__':
    main()