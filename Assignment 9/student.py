#******************************************************************************
# student.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# NONE
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

class Student:
    """
    A class for students
    Attributes: ._name, ._test scores
    Methods: constructor, .average(), .display(), .passes() 
    """
    
    # Constructor
    # n is the student's name (string)
    # s is a list of the student's test scores (list of floats)
    def __init__(self, n, s):
        self._name = n
        self._scores = s
    
    def average(self):
        """Calculate and return the average of the test scores of a student"""
        rs = 0
        for i in range(len(self._scores)):
            rs += self._scores[i]
        
        if (len(self._scores) > 0):
            avg = rs / len(self._scores)
        else:
            avg = 0
        
        return avg
    
    def display(self):
        """Display the student's name and his/her test score average"""
        print("{0}, Average = {1}".format(self._name, self.average()))
    
    def passes(self):
        """Returns True if the test score average is 60 or greater, or False
        otherwise"""
        avg = self.average()
        
        if avg >= 60:
            return True
        else:
            return False
################################################################################
# PUT YOUR CLASS DEFINITION ABOVE!
################################################################################

# The main function
def main():
    a = Student("Alice", [40, 80, 90, 78])
    b = Student("Bob", [80, 70, 60])
    c = Student("Carol", [])
    d = Student("Dennis", [50, 40, 30])
    e = Student("Evan", [1, 2, 3, 4, 5])
    f = Student("Frank", [90, 90, 90])

    print("This should print: Alice, Average = 72.0")
    a.display()

    print("This should print: 70.0 True") 
    print(b.average(), b.passes())
 
    print("This should print: 0 False") 
    print(c.average(), c.passes())
 
    all_students = [a, b, c, d, e, f]

    ####################################################
    # Write code which displays info for the students in
    # all_students who have passing averages.
    ####################################################

    for st in all_students:
        if st.passes():
            st.display()

# Run the main function
main()    
















