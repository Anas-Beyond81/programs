# university = {
# "name" : "university of malakand",
# "departments" : ["data science","computer science","AI","cyber security"],
# "founded" : 2000,
# "gender" : ("males", "females"),
# "student" : {
#     "name" : "anas khan",
#     "subject" : {
#         "phy" : 75,
#         "chem" : 57,
#         "bio": 95,

#     }
# }
# }
# # print(university["student"]["subject"]["phy"])

# # print(university["departments"])
# # student = {
# #     "name" : "anas khan",
# #     "subject" : {
# #         "phy" : 75,
# #         "chem" : 57,
# #         "bio": 95,

# #     }
# # }
# # print(student["subject"],["chem"],)


# # print(university.values())
# # print(university.items())
# # fortupple = (list(university.items()))
# # print(fortupple[4])

# # university.update("location : malakand")
# # print(university.get("gender7")),print(),print()
# # print(university["student"]["name"])


# home = {
#     "name" : "Anas home",
#     "rooms" : {
#         "right" : 2,
#         "left" : 2,
#         "center" : 1,
#     },
#     "well" : "yes",
#     "underground" : "basement",
#     "bathrooms" : 5,
# }
# home.get(home.update({"registered" : "yes"}))
# print(home)
# print(home["rooms"]["center"])
# print(type(home))
# collection = {4,5,4,5,"name","anas","name",6}
# print(collection)
# print(type(collection))
# print(len(collection))


# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# print(set1.union(set2))

# print(set1.intersection(set2))

# simpledic = {
#     "table" : "a piece of furniture or anything",
#     "cat" : "a small animal"
# }
# print(simpledic)

# department = {
#     "subject1" : "python",
#     "subject2" : "java",
#     "subject3" : "c++",
#     "subject4" : "javascript",
#     "subject5" : "java",
#     "subject6" : "c++",
#     "subject7" : "python",
#     "subject8" : "c",
#     "subject9" : "c",
# }
# print(len(department))

# department = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(department))



dictionary = {

}
sub1 = input("enter first subject name : " )
marks1 = input("enter marks : ")
dictionary.update({sub1:marks1})
sub2 = input("enter second subject name : " )
marks2 = input("enter marks : ")
dictionary.update({sub2:marks2})
sub3 = input("enter third subject name : " )
marks3 = input("enter marks : ")
dictionary.update({sub3:marks3})

print(dictionary)



