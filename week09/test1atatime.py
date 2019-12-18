from zstudentDAO import studentDAO

#create
latestid = studentDAO.create(('mark', 45))



#update
studentDAO.update(('Fred',21,13))
print("is this working")
result = studentDAO.findByID(latestid);
print(result)

#get all
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

#delete
studentDAO.delete(latestid)