from bom_game import search_user_in_a_dictionary, random_position, read_list, verify_answer
import pytest

def test_search_user():
    """
    Test the function to find users, it will return true if found and false if not.
    Returns TRUE if that user exists or FALSE if that user does not exist in the csv file.
    """
    list_of_usernames = ["Brivanmito", "Dario", "Luis"]
    assert search_user_in_a_dictionary("Brivanmito", list_of_usernames) == True
    assert search_user_in_a_dictionary("Eduardo", list_of_usernames) == False

def test_random_position():
    """
    Test that the options are completely mixed, so that no matter how many times the user takes the quiz, he sees them in different order:
    This function receives 1 list, and returns it unordered.
    """
    list_of_elements = ["Opcion A", "Opcion B", "Opcion C", "Opcion D"]
    new_list = random_position(list_of_elements)
    # Tests that the returned list is out of order
    assert list_of_elements != new_list

def test_read_list():
    """"
    Tests that the function reads a csv file and returns a list, if it returns an empty list, it means that there are no elements in the list, and if it returns a full list it means that it found elements.
    """
    filename = "windows.csv"
    list_of_elements = read_list(filename)
    assert len(list_of_elements) > 0

def test_verify_answer():
    """
    Tests whether the options sent are correct or incorrect, if they are correct it returns True, and if they are true it returns False.
    """
    opcion_selected = "A"
    correct_opcion = "A"
    assert verify_answer(opcion_selected, correct_opcion) == True
    opcion_selected = "A"
    correct_opcion = "B"
    assert verify_answer(opcion_selected, correct_opcion) == False



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", "test_bom_game.py"])