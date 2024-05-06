# person = {
#     "fname" : "Jerome",
#     "lname" : "Mariano",
#     "Bday" : " 30 March 2005",
#     "Bloodtype" : "A",
#     "its_active" : "True"

# print(person(Bday))    

# }

band = {
    "vocals" : "Plant",
    "drums"  : "page"
}
band2 = dict (vocals = "Plant", drums = "Page")
print(band)
print(band2)
print(type(band))
print(len(band2))

#access items
print(band["vocals"])
print(band.get("druns"))
#list all keys
print(band.keys())
#list all values
print(band.values())

# print( "drums" in band)
# print("triangle" in band )

# band["vocals"] = "Coverdale"
# band.update = ({"bass" : "JPJ"})

#sets
nums = {1,2,3,4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums2))


nums = {1, 2, 2, 3}
print(nums)
