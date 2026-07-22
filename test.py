#update data base -- remainig 
# Save data in students.tx

class collage :
    
    stu = [{"name":"sunny","branch":"cybersecurity","roll":"bca 2025","marks":9},{"name":"sunny","branch":"cybersecurity","roll":"bca 2022","marks":17},{"name":"sunny","branch":"cybersecurity","roll":"bca 2026","marks":8}] 

    def extract (cyberangles,roll):
        roll = str(roll)
        for i in cyberangles.stu:
            for key , value  in i.items():
                if key == "roll" and value == roll:
                    return i
        else :
            return  
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

    
# this i search with by roll no and return index 
    def update_roll(cyberangeles,i):
        decide = cyberangeles.search()
        if decide == "null":
            print("ERROR : you entered incorrect roll no please try again ")
            return 
        else :
            print("---!!!now you can update the roll no")
            new_roll = input("enter new roll no : ")
            new_dict = {
                "roll":new_roll,
            }
            copy = cyberangeles.stu[0]
            cyberangeles.stu[0]["roll"] = new_roll


    def show (cyberangels):
       for show in cyberangels.stu:
           print (show)    

           # this is testing file to test exploit file's function test here 






c = collage()
print(c.show)
print("changes reflect")
c.update_roll(0)
print(c.show)