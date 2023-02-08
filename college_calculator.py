'''
Your Name(s): Nathan Wang
Program Purpose/Description: Multi-purpose GPA Calculator based on USER GPA Scale
Calculate unweighted
Calculate weighted
Recommend Colleges
    - Use College Ranking API
'''

#start your program here

#ask user for number of courses
num_classes=int(input("How many courses are you taking? "))
    
#function that converts numerical grade to marple GPA scale
def convert_scale(class_grade):
    gpa=0
    if class_grade>=98:
        gpa=4.3
    elif class_grade>=94:
        gpa=4.0
    elif class_grade>=90:
        gpa=3.7
    elif class_grade>=87:
        gpa=3.3
    elif class_grade>=83:
        gpa=3.0
    elif class_grade>=80:
        gpa=2.7
    elif class_grade>=77:
        gpa=2.3
    elif class_grade>=73:
        gpa=2.0
    elif class_grade>=70:
        gpa=1.7
    elif class_grade>=67:
        gpa=1.3
    elif class_grade>=63:
        gpa=1.0
    elif class_grade>=60:
        gpa=0.7
    else:
        gpa=0
    return gpa

#function to calculate real gpa
def calculate_gpa(x):
    return x/num_classes

#make loop with num_classes to ask for a grade in a respective class
totaluw=0.0
totalw=0.0
for i in range(num_classes):
    class_grade=float(input("Enter grade for course " +str(i+1)+ ": "))
    
    #convert numerical grade to marple GPA scale
    gpa=convert_scale(class_grade)
    #add gpa to total unweighted
    totaluw+=gpa
        
    #ask if class is basic, honors, or AP
    while True:
        level=input("Is the course basic, honors, or AP? ")
        
        #add weight to GPA
        if level.lower()=="basic":
            totalw+=gpa
            break
        elif level.lower()=="honors":
            totalw+=gpa+.5
            break
        elif level.lower()=="ap":
            totalw+=gpa+1
            break
        else:
            print("invalid input")
        
    #newline
    print()   
    
#print results
print("Your unweighted GPA for these " + str(num_classes)+ " classes is: " + str(calculate_gpa(totaluw)))
print("Your weighted GPA for these " + str(num_classes)+ " classes is: " + str(calculate_gpa(totalw)))
print()

#test print to console
'''
print(totaluw)
print(totalw)

print(calculate_gpa(totaluw))
print(calculate_gpa(totalw))
'''

'''
Lists of top schools in respective fields

Information Sourced from:
usnews.com
collegefactual.com
'''
#medical schools
top_medical_school_list=["#1 Harvard University", "#2 New York University", "#3 Columbia University", "#4 Johns Hopkins University", "#5 University of California - San Francisco", "#6 Duke University", "#7 University of Pennsylvania", "#8 Stanford University", "#9 University of Washington", "#10 Yale University"]
#engineering schools
top_engineering_school_list=["#1 Massachusetts Institute of Technology", "#2 Stanford University", "#3 University of California - Berkeley", "#4 Carnegie Mellon University", "#5 Purdue University", "#6 University of Texas - Austin", "#7 California Institute of Technology", "#8 Georgia Institute of Technology", "#9 University of Michigan - Ann Arbor", "#10 University of Illinois - Urbana Champaign"]
#liberal arts
top_liberal_arts_school_list=["#1 Williams College", "#2 Amherst College", "#3 Swarthmore College", "#4 Pomona College", "#5 Wellesley College", "#6 Bowdoin College", "#7 United States Naval Academy", "#8 Claremont McKenna College", "#9 Carleton College", "#10 Middlebury College"]
#visual and performing arts
top_arts_school_list=["#1 Stanford University", "#2 University of Notre Dame", "#3 Duke University", "#4 Cornell University", "#5 American Film Institute Conservatory", "#6 Colgate University", "#7 Rensselaer Polytechnic Institute", "#8 Dartmouth College", "#9 Lafayette College", "#10 College of the Holy Cross"]
#business
top_business_school_list=["#1 University of Pennsylania", "#2 University of Chicago", "#3 Northwestern University", "#4 Stanford University", "#5 Harvard University", "#6 Massachusetts Institute of Technology", "#7 Yale University", "#8 Columbia University", "#9 University of California - Berkeley", "#10 University of Michigan - Ann Arbor"]

print("We will provide top 10 lists of colleges in the United States based on your preferred major")
#ask user for preferred major
major=input("What college major are you interested in?(medical, engineering, business, liberal arts, visual and performing arts) ")
if major.lower()=="medical":
    print("Here is a list of the top 10 colleges for your preferred major")
    print(*top_medical_school_list, sep = "\n")
elif major.lower()=="engineering":
    print("Here is a list of the top 10 colleges for your preferred major")
    print(*top_engineering_school_list, sep = "\n")
elif major.lower()=="business":
    print("Here is a list of the top 10 colleges for your preferred major")
    print(*top_business_school_list, sep = "\n")
elif major.lower()=="liberal arts":
    print("Here is a list of the top 10 colleges for your preferred major")
    print(*top_liberal_arts_school_list, sep = "\n")
elif major.lower()=="visual and performing arts":
    print("Here is a list of the top 10 colleges for your preferred major")
    print(*top_arts_school_list, sep = "\n")
else:
    print("invalid input")
    
print()
print("Goodluck in the college application process!")