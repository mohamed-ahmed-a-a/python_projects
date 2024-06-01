print("\t\t" , "=" * 34)
print("\t\t" , "=" * 8 , "User Application" , "=" * 8 )
print("\t\t" , "=" * 34)

print("\n\t\t   Welcome To User Application ^_^\n")

# I Will take from the user : name , id  , age  , country , city , jobtitle , salary 
# I Will make id is primary key and when the user went any information about any user he just enter his id 
# Every Users Information will be in database file called user.db

# ---------------------------------------------------
# ----------------- User Choice Part ----------------
# ---------------------------------------------------

import maskpass

print("Hint : ")
print("\n- Add | add ==> For Adding A New User")
print("\t\n- Update | update ==> For Update The User Details")
print("\t\n- Remove | remove ==> For Removing  User Data")
print("\t\n- Delete | delete ==> For Delete The Whole Users Data")
print("\t\n- Display | display ==> For Show All Users Details")
print("\t\n- Press \'y\' of \'Y\' To Continue")
print("\t\n- Press \'n\' of \'N\' To Exit")
print("\t\n-------------------------------------------------------")


while True:

    print("\n\n\t\tYou Can Do The Following For The User : \n")
    print("\t    ==>^ Add || Update || Remove ^<====")
    print("\t    ==>^    Delete || Show All  ^<=====\n")


    cont = input("\nDo You Want To Continue (y/n) : ").strip().capitalize()


    if cont == "N" or cont == "Exit" or cont == "End":
        print("\n\nExiting the application. Goodbye!")
        break


    elif cont != "Y":
        print("\nPlease Enter A Valid Operation ^_^")
        continue





    # Database Part
    import sqlite3

    # Create Database And Connect
    db = sqlite3.connect("User.db")

    # Create The Table And Connect
    db.execute("CREATE TABLE if not exists Users (Name text , Id intger , Age intger  , Country text , City text  , Jobtitle text , Salary float) ")

    # Seting Up The Cursor
    cr = db.cursor()

    user_choice = input("\nPlease Choice The Operation : ").strip().capitalize()


    if user_choice in ["Add" , "Update" , "Delete" , "Remove" ,"Show"]:

        # Inserting Data  
        if user_choice == "Add":

            name = input("\nPlease Enter Your Name : ").strip().capitalize()
            id = int(input("\nPlease Enter Your Id : "))
            age = float(input("\nPlease Enter Your Age : "))
            country = input ("\nPlease Enter Your Country : ").strip().upper()
            city = input ("\nPlease Enter Your City : ").strip().upper()
            job = input ("\nPlease Enter Your Job Title : ").strip().capitalize()
            salary = float(input("\nPlease Enter Your Salary : "))
            
            
            # Check If Id is exist
            cr.execute("SELECT * FROM Users WHERE Id=?", (id,))
            existing_user = cr.fetchone()

            if existing_user :
                print("\nThis ID is already exists . You Can't add it") 
                print("Please Choose Another ID")
                continue
            else:
            # Inserting Data 
                cr.execute("insert into Users (Name , Id , Age  , Country , City , Jobtitle , Salary) values (?  , ? , ? , ? , ? , ? , ?)"
                        , (name , id , age  , country , city , job , salary))
                
            print("\n\tThe Data Has Been Inserted Successfully :) ")    
            
            # Save(Commit) Changes
            db.commit()


        

            # Close Database 
            db.close()



        elif user_choice == "Update":
            
            # user input
            updated_user = int(input("\nPlease Enter The Id Of The User To Update It : "))


            # updated data
            uname = input("\nPlease Enter Your Name : ").strip().capitalize()
            uid = int(input("\nPlease Enter Your Id : "))
            uage = float(input("\nPlease Enter Your Age : "))
            ucountry = input ("\nPlease Enter Your Country : ").strip().capitalize()
            ucity = input ("\nPlease Enter Your City : ").strip().capitalize()
            ujob = input ("\nPlease Enter Your Job Title : ").strip().capitalize()
            usalary = float(input("\nPlease Enter Your Salary : "))


            
            import sqlite3

            # Create Database And Connect
            db = sqlite3.connect("User.db")

            # Create The Table And Connect
            db.execute("CREATE TABLE if not exists Users (Name text , Id intger , Age intger  , Country text , City text  , Jobtitle text , Salary float) ")

            # Seting Up The Cursor
            cr = db.cursor()

            # Updating From Database 
            db.execute("update Users set Name = ? , Id = ? , Age = ? , Country = ? , City = ?  , Jobtitle = ? , Salary = ? where Id = ?" ,
                    (uname , uid , uage , ucountry , ucity  , ujob , usalary , updated_user))


            # Save(Commit) Changes
            db.commit()

            print("\n\tThe Data Has Been Updated Successfully ^_^")

            # Close Database 
            db.close()




        # Deleting one user Data
        elif user_choice == "Remove":
            deleted_id = int(input("\nPlease Enter The Id Of The User To Delete It : "))
            
            import sqlite3

            # Create Database And Connect
            db = sqlite3.connect("User.db")

            # Create The Table And Connect
            db.execute("CREATE TABLE if not exists Users (Name text , Id intger , Age intger  , Country text , City text  , Jobtitle text , Salary float) ")

            # Seting Up The Cursor
            cr = db.cursor()

            
            # Deleting From Database 
            cr.execute("delete from Users where Id = (?)" , (deleted_id , ))
            
            
            # Save(Commit) Changes
            db.commit()

            print("\nThe User Has Been Deleted Successfully ^_^")

            # Close Database 
            db.close()






        # Deleting All Data
        elif user_choice == "Delete":
            
            import sqlite3

            # Create Database And Connect
            db = sqlite3.connect("User.db")

            # Create The Table And Connect
            db.execute("CREATE TABLE if not exists Users (Name text , Id intger , Age intger  , Country text , City text  , Jobtitle text , Salary float) ")

            # Seting Up The Cursor
            cr = db.cursor()

            deleted_data = (input("\nDo You Want to Delete All Users (y/n) : ")).capitalize().strip()
            
            if deleted_data == "Y":
                ack = input("\nAre You sure that you want to delete the All Users Data (y/n): ").capitalize().strip()
                if ack == "Y":
                    Password = password = maskpass.askpass()

                    if Password == "mohamed":

                        # Deleting From Database 
                        cr.execute("delete from Users")

                    print("\nThe All Data Has Been Deleted Successfully ^_^")

                elif ack == "n":
                    continue

            elif deleted_data == "n":

                continue
            
            
            # Save(Commit) Changes
            db.commit()


            # Close Database 
            db.close()






        # Showing All Users Data
        elif user_choice == "Show":
            
            show_or_no = input("\nDo You Want To Show All Users Data (y/n) : ").strip().capitalize()

            if show_or_no == "Y":

                password = maskpass.askpass()
                # password = input("\nPlease Enter The Password : ").strip()
                
                if password == "mohamed":
                    import sqlite3

                    # Create Database And Connect
                    db = sqlite3.connect("User.db")

                    # Create The Table And Connect
                    db.execute("CREATE TABLE if not exists Users (Name text , Id intger , Age intger  , Country text , City text  , Jobtitle text , Salary float) ")

                    # Seting Up The Cursor
                    cr = db.cursor()

                    
                    # Fetching Data From DataBase
                    cr.execute("select * from Users")

                    print("\n")
                    
                    result = cr.fetchall()

                    print("=" * 42)
                    print("\tVery Good ! Correct Password")
                    print("=" * 42 )
                    print("\t    Showing Users Data")
                    print("=" * 42 , "\n")
                    for row in result:

                        print(f"\n\t  ==>^ User Data ^<==\n")
                        print(f"\nUser Name : {row[0]}\n")
                        print(f"User Id : {row[1]}\n")
                        print(f"User Age : {row[2]}\n")
                        print(f"User Country : {row[3]}\n")
                        print(f"User City : {row[4]}\n")
                        print(f"User Job Title : {row[5]}\n")
                        print(f"User Salary : {row[6]}\n")
                        print("-" * 40)

                    
                    # Save(Commit) Changes
                    db.commit()

                    print("\n\n  The All Data Has Been Printed Successfully ^_^\n")

                    # Close Database 
                    db.close()


                else:
                    print("\nPlease Enter A Valid Password :)")

            elif show_or_no == "N":
                pass
            
            else:
                print("Please Enter A Vaild Choice :)")

    else:
        print("\nPlease Enter A Vaild Choice :)")         


print("\n\n====>" , "Thank You For Using My Application :)" ,"<=====\n")