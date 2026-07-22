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