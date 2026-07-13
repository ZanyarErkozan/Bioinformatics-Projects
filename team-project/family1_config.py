# family-1 tree structure from kinship.family_tree import ( male_person, female_person, partnership,
) # males
f1_xy07 = male_person(name="T19_F1_XY07")
f1_xy21 = male_person(name="T19_F1_XY21")
f1_xyu1 = male_person(name="T19_F1_XYU1")
f1_xy06 = male_person(name="T19_F1_XY06")
f1_xy15 = male_person(name="T19_F1_XY15")
f1_xy22 = male_person(name="T19_F1_XY22")
f1_xy24 = male_person(name="T19_F1_XY24") # females
f1_xx04 = female_person(name="T19_F1_XX04")
f1_xx13 = female_person(name="T19_F1_XX13")
f1_xx17 = female_person(name="T19_F1_XX17")
f1_xxu2 = female_person(name="T19_F1_XXU2")
f1_xx16 = female_person(name="T19_F1_XX16")
f1_xx19 = female_person(name="T19_F1_XX19")
f1_xx46 = female_person(name="T19_F1_XX46")
f1_xx14 = female_person(name="T19_F1_XX14")
f1_xx03 = female_person(name="T19_F1_XX03")
f1_xx18 = female_person(name="T19_F1_XX18") # partnerships and relationships
p1 = partnership(name="p1")
p1.add_parents(f1_xy07, f1_xx04)
p1.add_children(f1_xx13, f1_xx17, f1_xy06, f1_xy15) p2 = partnership(name="p2")
p2.add_parents(f1_xy21, f1_xx13)
p2.add_children(f1_xy22) p3 = partnership(name="p3")
p3.add_parents(f1_xyu1, f1_xx17)
p3.add_children(f1_xx46) p4 = partnership(name="p4")
p4.add_parents(f1_xy06, f1_xxu2)
p4.add_children(f1_xx14, f1_xx03) p5 = partnership(name="p5")
p5.add_parents(f1_xy15, f1_xx16)
p5.add_children(f1_xx18) p6 = partnership(name="p6")
p6.add_parents(f1_xy22, f1_xx19)
p6.add_children(f1_xy24) # start person
start_person = f1_xy07 