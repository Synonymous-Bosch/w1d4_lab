import pdb

def get_name(person):
    name = person["name"]
    return name

def get_favourite_tv_show(person):
    tv_show = person["favourites"]["tv_show"]
    return tv_show

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True
    else:
        return False
    
def add_friend(self, new_friend):
    self["friends"].append(new_friend)

def remove_friend(self, ex_friend):
    self["friends"].remove(ex_friend)

def total_money(people):
    money = 0
    for person in people:
        money += person["monies"]
    return money

def lend_money(lender, borrower, loan_amount):
    lender["monies"] -= loan_amount
    borrower["monies"] += loan_amount

def all_favourite_foods(people):
    favourite_foods = []
    for person in people:
        if person["favourites"]["snacks"] not in favourite_foods:
            favourite_foods.extend(person["favourites"]["snacks"])
    return favourite_foods

def find_no_friends(people):
    for person in people:
        if person["friends"] == []:
            return [person]

# def unique_favourite_tv_shows(people):
#     unique_shows = []
#     for person in people:
#         if person["favourites"]["tv_show"] not in unique_shows:
#                 unique_shows.append(person["favourites"]["tv_show"])
#     return unique_shows

def unique_favourite_tv_shows(people):
    favourite_shows = []
    for person in people:
        favourite_shows.append(person["favourites"]["tv_show"])
    unique_favourite_shows = set(favourite_shows)
    return sorted(list(unique_favourite_shows))

