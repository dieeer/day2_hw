users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": {
      
        "name": "monty",
        "species": "snake"
      
  }
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users ["Jonathan"] ["twitter"])

# 2. Get Erik's hometown

print(users ["Erik"] ["home_town"])

# 3. Get the list of Erik's lottery numbers

print(users["Erik"] ["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

print(users["Avril"] ["pets"] ["species"])

# 5. Get the smallest of Erik's lottery numbers

sortednum = sorted(users["Erik"]["lottery_numbers"])
smallest = sortednum[0]
print(smallest)

# 6. Return an list of Avril's lottery numbers that are even

lottery_numbers = users["Avril"]["lottery_numbers"]
even_nums = []
for lottery_number in lottery_numbers:
     if lottery_number % 2 == 0:
         even_nums.append(lottery_number)

print(even_nums)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

users ["Erik"] ["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh

users ["Erik"] ["home_town"] = "Edinburgh"
print(users["Erik"] ["home_town"])

# 9. Add a pet dog to Erik called "fluffy"

users["Erik"]["pets"].append: ({"name": "fluffy", "species": "dog"})

# 10. Add another person to the users dictionary

users["mac"] = {
     "twitter": "MacMiller",
     "lottery_numbers": [92, 2, "infinity"],
     "home_town": "Pittsburgh",
     "pets": [
       {
         "name": "Ralphie",
         "species": "dog"
       }
     ]
 }

print(users["mac"])