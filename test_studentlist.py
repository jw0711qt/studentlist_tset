'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    ## TODO write a test that adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised

    
    def test_remove_student_not_in_list(self):
        test_class = ClassList(5)
        test_class.add_student("Filmon")
        test_class.add_student("Michael")
        test_class.add_student("Libsu")
        self.assertRaises(StudentError, test_class.remove_student, "sami")


    ## TODO write a test that removes a student from an 
    # empty list, and asserts a StudentError is raised

    def test_remove_student_from_empty_list(self):
        test_class = ClassList(5)
        self.assertRaises(StudentError, test_class.remove_student, "sami")




    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.

    
    def tset_student_who_is_not_enrolled(self):
        test_class = ClassList(5)
        test_class.add_student("Senay")
        test_class.add_student("josi")
        test_class.add_student("solomon")
        self.assertFalse(test_class.is_enrolled("peter"))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## TODO write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.

    
    def test_index_of_student_returns_none_if_list_is_empty(self):
        test_class = ClassList(5)
        self.assertIsNone(test_class.index_of_student("kald"))
 
 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.

    def test_index_of_student_no_in_list_returns_none(self):
        test_class = ClassList(5)
        test_class.add_student('abel')
        test_class.add_student('adonay')
        self.assertIsNone(test_class.index_of_student("meron"))

   
    ## TODO write a test for your new is_class_full method when the class is full. 
    # use assertTrue.

    def test_for_is_class_full(self):
        test_class = ClassList(3)
        test_class.add_student("george floyd")
        test_class.add_student('bryana telear')
        test_class.add_student('ahmudi arbur')
        self.assertTrue(test_class.is_class_full())
    
    ## TODO write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.

    def test_is_class_full_empty_and_not_full(self):
        test_class = ClassList(3)
        self.assertFalse(test_class.is_class_full())
        test_class.add_student("filamingo")
        test_class.add_student('filaman')
        self.assertFalse(test_class.is_class_full())



    
