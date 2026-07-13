================================================================================
FORENSIC DNA KINSHIP PROJECT - PHASE 1
Relationship Analysis Project
================================================================================ ABOUT THE PROJECT
================================================================================
This project is a Python application that determines the kinship relationship between two individuals using a family tree structure. It is designed for use in forensic DNA analysis. The project analyzes relationships between individuals in a family tree and can detect the following types of relationships:
- Parent-child relationships (father_son, mother_daughter, etc.)
- Sibling relationships (full_siblings)
- Grandparent-grandchild relationships
- Uncle/aunt-nephew/niece relationships
- Cousin relationships (first_cousins, second_cousins, etc.)
- Unrelated individuals (unrelated) PROJECT STRUCTURE
================================================================================
The project consists of the following files: 1. kinship/family_tree.py - Contains family tree data structures - person, male_person, female_person classes - partnership (marriage/partnership) class - Tree traversal functions 2. kinship/__init__.py - Package initialization file 3. analyze_family_tree.py - Function to find relationship between two individuals (extract_relationship) - Lowest Common Ancestor (LCA) finding algorithm - Functions to generate relationship strings 4. family1_config.py - Example family tree configuration - Individual definitions and relationships - Start person (start_person) definition 5. run_example.py - Example usage script - Runs test scenarios and displays results 6. test_kinship.py - Unit tests - Can be run with pytest or directly REQUIREMENTS
================================================================================
- Python 3.6 or higher
- Standard Python libraries (typing, dataclasses, collections)
- Optional: pytest (for tests) INSTALLATION
================================================================================
1. Download or clone the project to your computer 2. Make sure Python is installed: python --version 3. No additional package installation required (uses standard libraries) HOW TO RUN
================================================================================ 1. EXAMPLE USAGE (run_example.py): -------------------------------- Navigate to the project directory in terminal/command line and run: python run_example.py This command runs predefined test scenarios and displays relationship results for each pair of individuals. Example output: ====================================================================== Forensic DNA Kinship Project - Phase 1 Relationship Analysis Results ====================================================================== [OK] T19_F1_XX16 <-> T19_F1_XY24 : unrelated [OK] T19_F1_XX19 <-> T19_F1_XX18 : unrelated [OK] T19_F1_XY22 <-> T19_F1_XX18 : first_cousins ... 2. RUNNING TESTS (test_kinship.py): --------------------------------------- With pytest: pytest test_kinship.py Or directly: python test_kinship.py This command runs all unit tests and displays results. 3. USING IN YOUR OWN CODE: -------------------------- from analyze_family_tree import extract_relationship import family1_config # Find relationship between two individuals relationship = extract_relationship("T19_F1_XY22", "T19_F1_XX18", family1_config) print(relationship) # Output: "first_cousins" HOW IT WORKS?
================================================================================ 1. CREATING FAMILY TREE: --------------------- - Individuals are defined in family1_config.py file - Male and female individuals are created with male_person() and female_person() - Marriages/partnerships are defined with partnership() - Relationships are established with add_parents() and add_children() Example: f1_xy07 = male_person(name="T19_F1_XY07") f1_xx04 = female_person(name="T19_F1_XX04") p1 = partnership(name="p1") p1.add_parents(f1_xy07, f1_xx04) p1.add_children(f1_xx13, f1_xx17) 2. RELATIONSHIP FINDING ALGORITHM: ------------------------- The extract_relationship() function follows these steps: a) Tree Traversal: - The entire family tree is traversed starting from the start person - BFS (Breadth-First Search) algorithm is used - All individuals and their levels are determined b) Person Finding: - Individuals are found in the tree using the given IDs - NoSuchPersonError is raised if a person is not found - IdenticalPersonError is raised if the same person is given twice c) Finding Lowest Common Ancestor (LCA): - All ancestors of both individuals are found - Common ancestors are identified - The closest common ancestor (LCA) is selected - Distance from both individuals to LCA is calculated d) Relationship Determination: - Relationship type is determined using distances and gender information - Example: dist_a=2, dist_b=2 → first_cousins - Example: dist_a=1, dist_b=2 → uncle_nephew or aunt_niece e) Returning Result: - Relationship string is returned - Returns "unrelated" if there is no common ancestor 3. SUPPORTED RELATIONSHIP TYPES: ---------------------------- - Parent-Child: father_son, father_daughter, mother_son, mother_daughter - Siblings: full_siblings - Grandparent: grandfather_grandson, grandmother_granddaughter, etc. - Uncle/Aunt: uncle_nephew, uncle_niece, aunt_nephew, aunt_niece - Great Uncle/Aunt: greatuncle_greatnephew, greataunt_greatniece, etc. - Great Grandparent: greatgrandfather_greatgrandson, etc. - Cousins: first_cousins, second_cousins - Distant Cousins: first_cousins_once_removed, first_cousins_twice_removed, etc. - Unrelated: unrelated - Unrecognized: unrecognized (for unsupported relationships) ERROR HANDLING
================================================================================
The program can raise the following errors: 1. NoSuchPersonError: - When the given person ID is not found in the family tree - Example: extract_relationship("T19_F1_XX16", "T19_F1_XY99", family1_config) 2. IdenticalPersonError: - When the same person ID is given twice - Example: extract_relationship("T19_F1_XX16", "T19_F1_XX16", family1_config) EXAMPLE USAGE SCENARIOS
================================================================================ Scenario 1: Finding relationship between two individuals
---------------------------------------------
from analyze_family_tree import extract_relationship, NoSuchPersonError, IdenticalPersonError
import family1_config person_a = "T19_F1_XY22"
person_b = "T19_F1_XX18" try: relationship = extract_relationship(person_a, person_b, family1_config) print(f"Relationship between {person_a} and {person_b}: {relationship}")
except NoSuchPersonError as e: print(f"Error: {e}")
except IdenticalPersonError as e: print(f"Error: {e}") Scenario 2: Creating a new family tree
-----------------------------------------
from kinship.family_tree import male_person, female_person, partnership # Create individuals
adam = male_person(name="Adam")
mary = female_person(name="Mary")
john = male_person(name="John") # Create partnership
partnership1 = partnership(name="partnership1")
partnership1.add_parents(adam, mary)
partnership1.add_children(john) # Create configuration module
class my_family_config: start_person = adam # Find relationship
from analyze_family_tree import extract_relationship
relationship = extract_relationship("Adam", "John", my_family_config)
print(relationship) # Output: "father_son" NOTES
================================================================================
- The project uses the partnership concept to represent family tree structure. This represents marriages or couples with children. - Tree traversal uses BFS (Breadth-First Search) algorithm. - Relationship determination is based on Lowest Common Ancestor (LCA) and distance calculations. - Gender information is used to distinguish between some relationship types (e.g., uncle_nephew vs aunt_niece). TROUBLESHOOTING
================================================================================
1. If you get "ModuleNotFoundError": - Make sure you are in the project directory - Make sure you are using the correct Python version 2. If you get "NoSuchPersonError": - Make sure person IDs are correct - Check the family tree configuration 3. If you get unexpected relationship results: - Check the family tree configuration - Make sure relationships are established correctly CONTACT AND SUPPORT
================================================================================
For questions about the project, you can contact the project team. LICENSE
================================================================================
This project is developed for educational purposes. ================================================================================
Last Updated: 2024
================================================================================
