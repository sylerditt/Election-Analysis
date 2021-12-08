# Election_Analysis

## Project Overview
Tasked with determining winning results for election given data for US congressional precinct in CO. 
1. Calculate total votes cast
2. Get complete list of candidates
3. Calculate total votes received for each candidate
4. Calculate percentage of votes won for each candidate
5. Determine winner based on popular vote

## Resources
--Data source: election_results.csv
--Software: Python 3.7.6, Visual Studio Code, 1.62.3

## Summary
The analysis of the election shows:
--There were 369,711 votes cast in the election
--The candidates were:
    --Charles Casper Stockham
    --Diana DeGette
    --Raymon Anthony Doane
--The candidate results were:
    --Charles Casper Stockham received 23.0% of the vote and 85,213 votes
    --Diana DeGette received 73.8% of the vote and 272,892 votes
    --Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
--The winner of the election was:
    --Diana DeGette who received 73.8% of the vote and 272,892 votes

## Challenge Overview
We used python via VS Code to determine the results of the election. Using the csv file, we read the data and consolidated it into the needed information. In this case, we pulled the candidates, their total votes, and determined their percentage of overall votes based on the total votes cast. We used python to input the necessary information into the election_analysis.txt file in VS code then pushed it to GitHub. 
## Challenge Summary
Diana DeGette won the vote based on our analysis as she had the most votes cast in her favor, 73.8% of the vote. 

## Overview of Election Audit
The purpose of this eleciton audit analysis was to use the skills we developed in the module 3 lesson and apply it to different data of interest. For this audit, we used the county column to determine which county had the largest voter turnout and print the results, including all county turnouts, to the election analysis text file. 

## Election-Audit Results
 * Votes cast: 369,711
 * Jefferson: 38,855 (10.5%)
 * Denver: 306,055 (82.8%)
 * Arapahoe: 24,801 (6.7%)
 * Largest turnout: Denver
 * Winning Candidate: Diana DeGette
 * Winning Vote Count: 272,892
 * Winning Percentage: 73.8%

![image](https://user-images.githubusercontent.com/85717241/145269092-16c07e11-c497-448a-8c45-2b90c752753c.png)

## Election-Audit Summary:
In order to apply this code to any election results, simply upload your own csv file with election results in place of our election_results.csv (see example 1 below). Then you would just have to either make sure your headings are in the same place (i.e. county and candidate as rows 2 and 3) or just change the name of the rows and numbers to suit your data set (see example 2 below). Then just make sure all instances of those row names match and create your own statements based on which information you want to convey. This process makes it much easier to display meaningful data given a large data set. 

### Example 1:
file_to_load = os.path.join("Resources", "election_results.csv")
### Example 2:
candidate_name = row[2]
