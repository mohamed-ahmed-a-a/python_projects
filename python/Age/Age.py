print("\t\t" , "=" * 34)
print("\t\t" , "=" * 8 , "Age Application" , "=" * 8 )
print("\t\t" , "=" * 34)

print("\n\t\t   Welcome To Age Application ^_^\n")

print("\nChoose Your Age Unit : ")
print("  ==>^ Month | Week | Day | Hour | Minute | Second | All ^<==\n\n")


user_age = float(input("Please Enter Your Age : ") )



if user_age > 120:
    print("\n\nThis Is Not Valid :) Please Enter Your Real Age\n")
    exit()


age_in_months = user_age * 12
age_in_weeks = age_in_months * 4
age_in_days = user_age * 365.25
age_in_hours = age_in_days * 24
age_in_minutes = age_in_hours * 60
age_in_seconds = age_in_minutes * 60
        


def units():
    age_unit = input("\nPlease Enter Age Unit : ").strip().capitalize()

    if age_unit == "Month":
        print(f"\n\nYour Age In Months : {age_in_months:.1f} Month")

    elif age_unit == "Week":
        print(f"\nYour Age In Weeks : {age_in_weeks:.1f} Week")

    elif age_unit == "Day":
        print(f"\nYour Age In Days : {age_in_days:.1f} Day")

    elif age_unit == "Hour":
        print(f"\nYour Age In Hours : {age_in_hours:.2f} Hour")

    elif age_unit == "Minute":
        print(f"\nYour Age In Minute : {age_in_minutes:.2f} Minute")

    elif age_unit == "Second":
        print(f"\nYour Age In Seconds : {age_in_seconds:.2f} Second")
    
    elif age_unit == "All":
        print(f"\n\nYour Age In Months : {age_in_months:.1f} Month")
        print(f"\nYour Age In Weeks : {age_in_weeks:.1f} Week")
        print(f"\nYour Age In Days : {age_in_days:.1f} Day") 
        print(f"\nYour Age In Hours : {age_in_hours:.2f} Hour")           
        print(f"\nYour Age In Minute : {age_in_minutes:.2f} Minute")
        print(f"\nYour Age In Seconds : {age_in_seconds:.2f} Second")
        

    else:
        print("\n\nPlease Enter A Valid Age Unit :(")

units()


print("\n\n====>" , "Thank You For Using My Application :)" ,"<=====\n")