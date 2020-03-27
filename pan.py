pan = input("Enter your pan number ")
if (len(pan)==10) & (pan[0:5]+pan[9]).isalpha() & pan[5:9].isdigit():
    print("It is a valid pan")
    print("Surname of the applicants begins with '",pan[4],"'")
    if pan[3]=='p':
        print("This pan card belongs to a Individual(Proprietor)")
    elif pan[3]=='c':
        print("This pan card belongs to a Company")
    elif pan[3]=='a':
        print("This pan card belongs to the Association of persons")
    elif pan[3]=='f':
        print("This pan card belongs to a Firm")
    elif pan[3]=='h':
        print("This pan card belongs to a Hindu undivided family")
    elif pan[3]=='t':
        print("This pan card belongs to a Trust")
    elif pan[3]=='b':
        print("This pan card belongs to a Body of individuals")
    elif pan[3]=='g':
        print("This pan card belongs to the Government")
    elif pan[3]=='l':
        print("This pan card belongs to the Local authority")
    elif pan[3]=='j':
        print("This pan card belongs to the Artificial juridical person")
    elif pan[3]=='e':
        print("This pan card belongs to the limited liability partnership")
    else:
        print("please enter a valid pan number")
    
    
else:
    print("please enter a valid pan number")
