from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, MenuItem ,Base

engine = create_engine('sqlite:///myrestaurantapp.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
session = DBsession()


#Restaurant-1 Fishes
restaurant1 =  Restaurant(name = ' Restaurant Fishes ')
session.add(restaurant1)
session.commit()

menuitem1 = MenuItem(name ='Alaskan salmon', description = 'Salmon is a great option for your diet overall', price ='$5', course = 'fishes', restaurant = restaurant1)
session.add(menuitem1)
session.commit()

menuitem2 = MenuItem(name ='Cod', description = 'This flaky white fish is a great source of vitamin B-12', price ='$10', course = 'fishes', restaurant = restaurant1)
session.add(menuitem2)
session.commit()


menuitem3 = MenuItem(name ='Herring', description = 'A fatty fish similar to sardines', price ='$15', course = 'fishes', restaurant = restaurant1)
session.add(menuitem3)
session.commit()



menuitem4 = MenuItem(name ='Mahi-mahi', description = 'A tropical firm fish', price ='$20', course = 'fishes', restaurant = restaurant1)
session.add(menuitem4)
session.commit()


menuitem5 = MenuItem(name ='Mackerel', description = 'As opposed to leaner white fish', price ='$19', course = 'fishes', restaurant = restaurant1)
session.add(menuitem5)
session.commit()


menuitem6 = MenuItem(name ='Perch', description = 'Another white fish', price ='$17', course = 'fishes', restaurant = restaurant1)
session.add(menuitem6)
session.commit()


menuitem7 = MenuItem(name ='Rainbow trout', description = 'AFarmed rainbow trout is actually a safer option than wild', price ='$23', course = 'fishes', restaurant = restaurant1)
session.add(menuitem7)
session.commit()

menuitem8 = MenuItem(name ='Sardines', description = 'Also an oily fish', price ='$7', course = 'fishes', restaurant = restaurant1)
session.add(menuitem8)
session.commit()



#restaurant-2 for meets

restaurant2 = Restaurant(name = 'Restaurant Meets')
session.add(restaurant2)
session.commit()


menuitem1 = MenuItem(name ='Beef', description = 'Excessive beef consumption can increase circulating iron to unhealthy levels in some individuals.', price ='$7', course = 'meats', restaurant = restaurant2)
session.add(menuitem1)
session.commit()


menuitem2 = MenuItem(name ='Lamb and Mutton', description = 'Generally speaking, both lamb and mutton is very healthy.', price ='$9', course = 'meats', restaurant = restaurant2)
session.add(menuitem2)
session.commit()


menuitem3 = MenuItem(name ='Chicken', description = 'Chicken is very cheap and easily affordable.', price ='$4', course = 'meats', restaurant = restaurant2)
session.add(menuitem3)
session.commit()


menuitem4 = MenuItem(name ='Turkey', description = 'offering 17.5 grams of protein in only 149 calories.', price ='$8', course = 'meats', restaurant = restaurant2)
session.add(menuitem4)
session.commit()


menuitem5 = MenuItem(name ='Wild Boar', description = 'wild boar contains a higher proportion of omega-3 fatty acids.', price ='$10', course = 'meats', restaurant = restaurant2)
session.add(menuitem5)
session.commit()





#restaurant3 for vegetables

restaurant3 = Restaurant(name = 'Restaurant vegetables')
session.add(restaurant3)
session.commit()


menuitem1 = MenuItem(name ='Artichoke', description = 'Calories: 47 kcal', price ='$5', course = 'vegetables', restaurant = restaurant3)
session.add(menuitem1)
session.commit()


menuitem2 = MenuItem(name ='Arugula', description = 'Calories: 25 kcal', price ='$4', course = 'vegetables', restaurant = restaurant3)
session.add(menuitem2)
session.commit()


menuitem3 = MenuItem(name ='Beet Greens', description = 'Calories: 22 kcal', price ='$3', course = 'vegetables', restaurant = restaurant3)
session.add(menuitem3)
session.commit()


menuitem4 = MenuItem(name ='Beetroot', description = 'Calories: 43 kcal', price ='$6', course = 'vegetables', restaurant = restaurant3)
session.add(menuitem4)
session.commit()


menuitem5 = MenuItem(name ='Bok Choy', description = 'Calories: 13 kcal', price ='$3.5', course = 'vegetables', restaurant = restaurant3)
session.add(menuitem5)
session.commit()




#restaurant4 for pizza

restaurant4 = Restaurant(name = 'Restaurant Pizza')
session.add(restaurant4)
session.commit()


menuitem1 = MenuItem(name ='Neapolitan Pizza ', description = 'Variations of Neapolitan Pizza', price ='$7', course = 'pizza', restaurant = restaurant4)
session.add(menuitem1)
session.commit()


menuitem2 = MenuItem(name ='Chicago Pizza ', description = 'Chicago Pizza Traditional Toppings', price ='$5', course = 'pizza', restaurant = restaurant4)
session.add(menuitem2)
session.commit()


menuitem3 = MenuItem(name ='Sicilian Pizza', description = 'Sicilian Pizza Baking', price ='$8', course = 'pizza', restaurant = restaurant4)
session.add(menuitem3)
session.commit()


menuitem4 = MenuItem(name ='Greek Pizza', description = 'Greek Pizza Traditional ', price ='$9', course = 'pizza', restaurant = restaurant4)
session.add(menuitem4)
session.commit()


menuitem5 = MenuItem(name ='California Pizza', description = 'California Pizza Baking', price ='$9', course = 'pizza', restaurant = restaurant4)
session.add(menuitem5)
session.commit()



print ("added menu items!")
