sample_list = [1,2,3,4,"a","b",(1, "18"), [1,4,76,100], {"something":42, "something_else": 18}]

sample_list[0]
sample_list[0]=15
sample_list

# lists can change, tuples can't 

sample_tuple = (1,"a", 3)
sample_tuple[1]
sample_tuple[1] = 2 # gives an error

playing_card1 = ("Hearts", "King", 10)

def get_lat_long(location):
    # insert code here
    if location == "here":
        lat = 39
        long = 79
    elif location == "there":
        lat = 43
        long = 83
    return lat, long 

my_latitude_and_longitude = get_lat_long(my_location)
type(my_latitude_and_longitude)
my_latitude_and_longitude[0]
my_latitude_and_longitude[1]
mylat, mylong = get_lat_long("there")

sample_dictionary = {"location": "College Park", 
                     "population":"more than a dozen",
                     "some_incomes": [18,23,10,177,8]}

sample_dictionary["location"]
sample_dictionary["some_incomes"]

sample_dictionary.keys()
sample_dictionary.values()
sample_dictionary.items()

