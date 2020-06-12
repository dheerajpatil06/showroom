import pyodbc
conn= pyodbc.connect('Driver={SQL Server};'
                     'Server=DHEERAJ\SQLEXPRESS;'
                     'Database=Dheeraj;'
                     'Trusted_connection=yes;')
cursor=conn.cursor()
cursor.execute('select * from customer)
    
def showroom(Ture=1):
    print("Welcome to Volkswagen")
    firstname=str(input("Enter the First Name"))
    Surname=str(input("Eneter Surname"))
    Mobile=str(input("Enter the mobile number"))
    email=str(input("Enter email id"))
    address=str(input("Enter The address"))
    print("Select Profession")
    print("1.Salaried")
    print("2.Self Employed")
    print("3.Businessman")
    print("4.Any other")
    while Ture:
        Profession=input("Enter option")
        Nameofcompany=str(input("Enter the Name of Comapny"))
        Designation=str(input("Enter the Designation"))
        print("The User of Vehicle")
        print("1.Self")
        print("2.Son")
        print("3.Doughter")
        print("4.Other")
        while Ture:
            TheUserofVehicle=input("Enter the option")
            DailyRunning=int(input("Enter The daily runing In KM"))
            print("Model Interested")
            print("1.POLO")
            print("2.VENTO")
            print("3.T-ROC")
            print("4.TiguanAS")
            while Ture:
                Model=input("Model Interested")
                print("Varient")
                print("1.Trendline")
                print("2.Comfortline")
                print("3.Highline")
                while Ture:
                    Variant=input("Varient")
                    Budget=int(input("Enter the Budget in lac"))
                    Finance=str(input("Finance requird YES or NO"))
                    Bank=str(input("Banking patner"))
                    Purchase=str(input("Time of Parchase"))
                    Exchange=str(input("Trade in required Yes Or NO"))
                    SpeceficRequirment=str(input("Enter any specific requirement if any"))
                    oldcar=str(input("Give details of old car year,make,model,running,colour"))

                    TD=str(input("Date of test drive or appointment date"))
showroom()



