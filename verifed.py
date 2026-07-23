#update data base -- remainig 
# Save data in students.tx


class collage :
    
    stu = [{"name":"sunny","branch":"cybersecurity","roll":"bca 2025","marks":9},{"name":"sunny","branch":"cybersecurity","roll":"bca 2025","marks":17},{"name":"sunny","branch":"cybersecurity","roll":"bca 2025","marks":8}]   

    
    # take a mark 1
    def sor(cyberangels):
       mark = []
       for i in cyberangels.stu:
           for key , value  in i.items():
               if key == "marks":
                   m = value
                   mark.append(m)
       return mark
    

   # short number 2
    def shorta(cyberangels,mark = []):
       
        p = 0 
        while p < len(mark)-1:

            i = 0
            while i < len(mark)-1:

                for k in range(i,len(mark)):
                 if mark[i] < mark[i+1]:
                    copy = mark[i]
                    mark[i] = mark[i+1]
                    mark[i+1] = copy
                i = i+  1
            p += 1
        return mark    

#  take marks and return new list of dictionary   3 
    def num_stu(cyberangles,marks):
        new = [{}]
        # mark [17, 9, 8]
        i = 0 
        while i < len(marks):

            search = marks[i]
            for l in cyberangles.stu:
                for key , value in l.items():
                    if key == "marks" and value == search :
        
                        new.append(l)
            i += 1
        return new

            
        
s1 = collage()
mark = s1.sor()
st = s1.shorta(mark)
print(mark,st)
arr = s1.num_stu(st)
print(arr)

# this is a fully functioned short by student function 

# this verified file is under expolit.py file and verify the function 



#update data base -- we are  working on it 
# Save data in students.txt after that update function we will work on it
 #update data base -- remainig 
# Save data in students.tx

class collage :
    
    stu = [{"name":"sunny","branch":"cybersecurity","roll":"bca 2025","marks":9},{"name":"rajjo","branch":"bms","roll":"bca 2022","marks":17},{"name":"bhawesh","branch":"ba","roll":"bca 2026","marks":8}] 
    # search is first 1   
    def search (cyberangels):
            # same logic we can apply but we use efficiently
            print(">? search a student by roll no -----*** ")
            src = input("enter student roll number : ")
        
            p = False
            for i in cyberangels.stu:
                for key , value in i.items() :
                    if key =="roll" and value == src :
                     
                     p = True
                     break
            if p == True:
                print(src,"present in data base ")
                return src 
            elif p== False:
                return "null"   
    
        
    # this i search with by roll no and return index sequence  3
    def update_roll(cyberangeles,i):
            decide = cyberangeles.search()
            if decide == "null":
                print("ERROR : you entered incorrect roll no please try again ")
                return 
            else :
                print("---!!!now you can update the roll no")
                new_roll = input("enter new roll no : ").strip()
                
                copy = cyberangeles.stu[i]
                cyberangeles.stu[i]["roll"] = new_roll

    
    
    def show (cyberangels):
           for show in cyberangels.stu:
               print (show)    

    # only data base admin can use only  sequnce 2 
    def location (cyberangels):
        location = input("enter your roll number : ").strip()
        i = 0 
        stop = True
        for l in cyberangels.stu:

            if stop == False:
                break
            for key , value in l.items():
                if key == "roll" and value == location:
                    stop = False
                    break
            else :
                i += 1 

        return i

    def update_mark(cyberangles,i):
         decide = cyberangles.search()
         if decide == "null":
            print("ERROR : you entered incorrect roll no please try again ")
            return 
         else :
            print("---!!!now you can update the marks ")
            if marks >100 :
                print("ERROR : you entered a marks greater than 100 please try again !!!!!")
            elif marks < 0 :
                print("ERROR : less than 0 not vaid ")
            else :    
                marks = int(input("enter new marks : "))
           
            copy = cyberangles.stu[i]
            cyberangles.stu[i]["marks"] = marks

    def update_name (cyberangles,i):
        decide = cyberangles.search()
        if decide == "null":
            print("ERROR : you entered incorrect roll no please try again ")
            return 
        else :
            print("---!!!now you can update the name ")
            name = input("enter new name : ").strip()
                   
            copy = cyberangles.stu[i]
            cyberangles.stu[i]["name"] = name



s1 = collage()
s1.show()
location = s1.location()
s1.update_name(location)
s1.show()

# updation function 

class collage :
    
    stu = [{"name":"sunny","branch":"cybersecurity","roll":"bca 2025","marks":9},{"name":"rajjo","branch":"bms","roll":"bca 2022","marks":17},{"name":"bhawesh","branch":"ba","roll":"bca 2026","marks":8}] 
 
    def show (cyberangels):
           for show in cyberangels.stu:
               print (show)    

    def save_data(cyberangels):
         file = input("enter your file name with .txt or other extension: ").strip()

         with open(file,"a") as save:
             
              for temp in cyberangels.stu:
                   temp1 = str(temp).strip()
                   print(temp1)
                   save.write(temp1)
                   save.write("\n")
                


save = collage  ()
save.save_data()
               
         
# file save function done 

