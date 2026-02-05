class MultipleFunctions():
    def Subfields():
        list1 =['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for types in list1:
            print(types)

    def OddEven():
        num = int(input("Enter a number"))
        if num%2 == 0:
            print (num,"is even number")
        else:
            print (num,"is odd number")

    def Eligible():
        Gender = input("Enter yot gender:")
        Age = int(input("Enter your Age"))
        print('Gender:',Gender)
        print('Age:',Age)
        if (Gender == 'male' and Age >=21):
            print("ELIGIBLE")
        elif (Gender == 'female' and Age>=18):
            print('ELIGIBLE')
        else:
            print("NOT ELIGIBLE")

    def percentage():
        subject1 =int(input("Enter subject1 mark:"))
        subject2 =int(input("Enter subject2 mark:"))
        subject3 =int(input("Enter subject3 mark:"))
        subject4 =int(input("Enter subject4 mark:"))
        subject5 =int(input("Enter subject5 mark:"))
        total = (subject1+subject2+subject3+subject4+subject5)
        percentage = (total/500)*100
        return percentage
    
    def Triangle():
        height= int(input(" Enter Height:"))
        base = int(input("Enter Base"))
        print("Area formula: (Height*Base)/2")
        Area= (height*base)/2
        print("Area of triangle:",Area)
        side1=int(input("Side1:"))
        side2=int(input("Side2:"))
        base=int(input("Base:"))
        print("Perimeter formula: Side1+Side2+Base")
        Perimeter= side1+side2+base        
        print("Perimeter of Triangle:",Perimeter)
