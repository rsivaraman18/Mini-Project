'''collecting data from DB'''
import sqlite3
connection=sqlite3.connect('Rank.db')
cursor=connection.cursor()
cursor.execute("SELECT name,total,result,rank,rollno FROM school order by total DESC ")
result=cursor.fetchall()
#print(result)
 
'''convert tuple to list'''
mylist1=[]
for i in result:
    mylist1.append(list(i))
#for i in mylist1:    
    #print(i)
    

'''now ranking the data'''
n=1
old=0
for i in mylist1:
    if i[2]=='pass':        #i[2]=result
        if old==i[1]:       #i[1] total
            old=i[1]
            n=n-1
            i[3]=n          #i[3] rank
        else:
            old=i[1]
            i[3]=n          #i[3] rank
        n=n+1
        #print("Rank holders",i[3],i[0])
    else:
        continue

    

MYLIST2=[]
for i in mylist1:
    MYLIST2.append(tuple(i))
print(MYLIST2)

connection=sqlite3.connect('Rank.db')
cursor=connection.cursor()    
qry="UPDATE school SET name=?,total=?,result=?,rank=? WHERE rollno=?"
for i in MYLIST2:
    cursor.execute(qry,i)
connection.commit()
print('successfully added')





    





