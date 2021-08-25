import csv
def read():
    f = open("det.csv",'r',newline='\r\n')
    s_reader = csv.DictReader(f)
    for i in s_reader:
        print (i)
    f.close()
def write():
    f = open ("det.csv","w",newline='')
    s_writer = csv.writer(f)
    s_writer.writerow(['id','Name','E-mail'])
    studentdetails = []
    while True:
        r = int(input("enter id"))
        n = input("enter name")
        m = input("enter email")
        lst=[r,n,m]
        studentdetails.append(lst)
        ch =input("Do you want to add more student details? (y/n)")
        if(ch=='n'):
            break
    s_writer.writerows(studentdetails)
    f.close()
write()
read()