import sys
inp = sys.argv[1]
names = ""
student_info = {}
with open(inp) as f:
    for line in f:
        names = line.split(":")[0]
        student_info[names] = (line.split(":")[1]).split(",")
for item in sys.argv[2].split(","):
    try:
        university = student_info[item][0]
        department = student_info[item][1]
        print(f"Name: {str(item)} \nUniversity: {str(university)} \nDepartment: {str(department)}", end="")
    except:
        print(f"\nNo record of {item} was found!\n")