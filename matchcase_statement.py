#Match-case statement (switch): An alternative to using many elif statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "Its Monday"
        case 2:
            return "Its Tuesday"
        case 3:
            return "Its Wednesday"
        case 4:
            return "Its Thursday"
        case 5:
            return "Its Friday"
        case 6:
            return "Its Saturday"
        case 7:
            return "Its Sunday"
        case _:
            return "Not a valid day"
        
print(day_of_week(3))


#def is_weekend(day):
#    match day:
#        case "Monday":
#            return False
#        case "Tuesday":
#            return False
#        case "Wednesday":
#            return False
#        case "Thursday":
#            return False
#        case "Friday":
#            return False
#        case "Saturday":
#            return True
#        case "Sunday":
#            return True
#        case _:
#            return False
# print(is_weekend("Sunday"))

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return False
print(is_weekend("Sunday"))