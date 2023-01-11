email =input("Enter the email:")
a,b,c=0, 0, 0
if len(email)>= 6:
    if email[0].isalpha:
        if ("@" in email) and email.count("@")==1:
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        a=1
                    elif i.isalpha():
                        if i==i.upper():
                            b=1
                    elif i.isdigit:
                        continue
                    elif i=="_" or i=="."or i=="@":
                        continue
                    else:
                        c=1
                if a==1 or b==1 or c==1:
                    print("wrong email : Does not satisfy the condition")
                else:
                    print("You Entered the right Email.")            

            else:
                print("wrong email :'.' is not placed at right position")
        else:
            print("wrong email : @ use more than 1 time") 
    else:
        print("wrong email:numbric value not alowed at the first place")
else:
    print("wrong email:length condition does not match ")