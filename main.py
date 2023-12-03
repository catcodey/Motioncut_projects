
import csv
import pandas as pd
filename = "tasks.csv"

c=0
ans='y'
with open(filename, 'a',newline="") as csvfile0:
        csvwriter0 = csv.writer(csvfile0)
        csvwriter0.writerow(["sno","name","description","date","no"]) 
def add_task():
    global c
    c=c+1
    with open(filename, 'a',newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            #csvwriter.writerow(["name","des","date","no"])
            task = input("Enter task: ")
            des = input("Enter description: ")
            date = input('Enter date (DD/MM/YY): ')
            prio = input("Set priority (H/M/L)   H: High   M: Medium   L: Low\nPriority?: ")
            csvwriter.writerow([str(c),task, des, date, prio])
    print("\n\t\ttask added successfully.\n")
def display():
    print("\t\t\t\t\tTO DO LIST\n")
    with open(filename,"r") as csvfile1:
        csvreader=csv.reader(csvfile1)
        print("sno\t\t name\t\t\tdescription\t\t  date\t\t  priority\n")
        arr=[]
        
        for i in csvreader:
            arr.append(i)
        arr.pop(0)
        for j in arr:
            for k in j:
                print(k,end="\t\t ")
            print("\n")
def mark_complete():
    with open(filename, "r+", newline="") as csvfile2:
        comp = input("\t\tEnter task number completed: ")
        c1read = csv.reader(csvfile2)  # tasks reader
        c1write = csv.writer(csvfile2)  # tasks writer
    
        for row in c1read:
            if row[0] == comp:
                t=row[4]
                dict_priority={'H':'High','M':'Medium','L':'Low'}
                print(f"\t\t\tGreat!!! You completed a {dict_priority[t]} priority task!!\n")
    
                with open("completed.csv", "a", newline="") as completed:
                    comp1write = csv.writer(completed) 
                    comp1write.writerow(row)

                    df = pd.read_csv("tasks.csv")
                    df = df[df['sno'] != int(comp)]  #imp
                    df.to_csv("tasks.csv", index=False)
                    break


    show_comp=input("\n\t\tshow completed tasks(y/n)?:")
    if show_comp=="y":
        print("\n\t\t\t\t\tCOMPLETED TASKS\t\t\t\n\n\t\t\t\t\t  GOOD JOB!!!\n")
        with open("completed.csv","r") as csvfile1:
            csvreader=csv.reader(csvfile1)
            print("sno\t\t name\t\t\tdescription\t\tdate\t\tpriority\n")
            
            for j in csvreader:
                for k in j:
                    print(k,end="\t\t ")
                print("\n")

def update():
    found='n'
    count=0
    with open(filename,"r+",newline="") as csvfile3:
        import pandas as pd
        df=pd.read_csv("tasks.csv")
        df['sno'] = df['sno'].astype(str)
        task=input("enter task number to update: ")
        
        
        c2read=csv.reader(csvfile3)
        c2write=csv.writer(csvfile3)
        
        
        
        for index, row in df.iterrows():
            if row['sno'] == task:
                print("Task found.\n")
                found='yes'
                newdate=input("enetr newdate(DD//MM//YY): ")
                newprio=input("enter new priority:(H/M/L) ")
                df.at[index, 'date'] = newdate
                df.at[index, 'no'] = newprio
                df.to_csv("tasks.csv", index=False)
                print("\n\t\tTask updated successfully.\n")
                break
        if(found!='yes'):
            print("Task not found.")
while(ans=='y'):
    print("\t\t\t\t\t  TO DO LIST\n")
    print("\t\t\tEveryday is a chance to get better.Don't waste it\n")
    print("\tFocus sharpens the mind, and time, when managed with purpose, becomes the currency of success.\n")
    print("\t\t\t1. ADD TASK\n")
    print("\t\t\t2. DISPLAY TASKS\n")
    print("\t\t\t3. MARK  AS COMPLETED\n")
    print("\t\t\t4. UPDATE TASK\n")
    print("\t\t\t5.EXIT\n")
    ch=int(input("enter choice(1/2/3/4/5): "))
    if ch==1:
        
        print("\n")
        add_task()
        print("\n") 
        
    elif  ch==2:
        
        print("\n")
        display()
        print("\n")  
        
    elif ch==3:
        
        print("\n")
        display()
        mark_complete()
        print("\n")
        
    elif ch==4:
        
        print("\n")
        display()
        update()
        print("\n")
        
    elif ch==5:
        ans="n"
    else:
        print("invalid coice")
    #ch=int(input("enter choice(1/2/3/4): "))
                
	# writing the data rows
#csvwriter.writerows(rows)
