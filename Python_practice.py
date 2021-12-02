# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# #Lists of dictionaries
# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# #Membership Operators
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
# #Logical operators
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")
# #Repetition Statements
# #Iterate Through Lists and Tuples
# for county in counties:
#     print(county)
# for i in range(len(counties)):
#     print(counties[i])
# #Iterate Through Dictionary
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# #Skill Drill-Print each county from the counties dictionary using the keys() method
# #?

# #Get the values of a dictionary
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
# for county in counties_dict:
#     print(counties_dict.get(county))
# #Get key-value pairs of dictionary
# for county, voters in counties_dict.items():
#     print(county, voters)
# #Skill Drill
# #print Arapahoe county has 422829 registered voters, etc.
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# #Multiline
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

#Format Floating-Point Decimals
#f'{value:{width}.{precision}}'
#message_to_candidate = (
   # f"You received {candidate_votes:,} number of votes. "
  #  f"The total number of votes in the election was {total_votes:,}. "
 #   f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    