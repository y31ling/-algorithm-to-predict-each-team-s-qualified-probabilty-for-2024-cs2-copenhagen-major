
import random
from collections import defaultdict

# Define the power values for each team
power_values = {f"team_{i}": 1000  for i in range(1, 17) }
seed_no = {f"team_{i}": i for i in range(1, 17) }
# y= 820 + 0.3x
power_values["team_1"] = 1100-25-25   #FAZE
power_values["team_2"] = 1050   #SPIR
power_values["team_3"] = 1032 +18  #VIT
power_values["team_4"] = 990-15   #MOUZ
power_values["team_5"] = 888 -18  #CPLX
power_values["team_6"] = 1050        #930+50   #VP
power_values["team_7"] = 950   #NAVI
power_values["team_8"] = 1050 #961   #G2
power_values["team_9"] = 910  +15 #C9
power_values["team_10"] = 896 +4   #HRC
power_values["team_11"] = 887  +3 #EF
power_values["team_12"] = 950-25-25  #ECS
power_values["team_13"] = 850 +20  #PAIN
power_values["team_14"] = 880   #SAW
power_values["team_15"] = 883   #GL
power_values["team_16"] = 850 +20 #MGLZ


pr30 = set() # tracks of 3:0 teams
promoted = set()  # Tracks promoted teams
eliminated = set()  # Tracks eliminated teams

# Define a function to simulate a match between two teams, considering random fluctuation
history = defaultdict(list)  # Tracks each team's opponents
total = set() 
def simulate_match(team_a, team_b):
    fluctuation_a = power_values[team_a] * (1 + random.uniform(-0.2, 0.2))
    fluctuation_b = power_values[team_b] * (1 + random.uniform(-0.2, 0.2))
    return team_a if fluctuation_a > fluctuation_b else team_b





# Define a function to simulate a tournament and return the promoted teams
def simulate_tournament():
    # Initial pairing based on the problem statement
    pairs_round_1 = [(f"team_{i}", f"team_{i+8}") for i in range(1, 9)]
    winners = {team: 0 for team in power_values}  # Tracks number of wins for each team
    losers = {team: 0 for team in power_values}  # Tracks number of losses for each team
    global pr30, promoted, eliminated, history
    pr30 = set() 
    promoted = set()  
    eliminated = set() 
    total = set() 
    history = defaultdict(list)
    q =0
    # Simulate first round
    round_matches = pairs_round_1
    for team_a, team_b in round_matches:
        winner = simulate_match(team_a, team_b)
        winners[winner] += 1
        loser = team_a if winner == team_b else team_b
        losers[loser] += 1
        history[winner].append(loser)
        history[loser].append(winner)
    
    q+=1

    # Function to decide the next round's matches based on winners and selection rules
    def decide_next_round_matches(current_winners, current_losers):
        next_round_matches = []
        sorted_teams = sorted(current_winners.keys(), key=lambda x: (-current_winners[x], seed_no[x]))
        while sorted_teams:
            team_a = sorted_teams.pop(0)
            for opponent in reversed(sorted_teams):
                if current_winners[team_a] == current_winners[opponent]:
                    next_round_matches.append((team_a, opponent))
                    sorted_teams.remove(opponent)
                    break
        return next_round_matches
    # ROUND 2
    round_matches = decide_next_round_matches(winners, losers)
    for team_a, team_b in round_matches:
            
        winner = simulate_match(team_a, team_b)
        winners[winner] += 1
         
        loser = team_a if winner == team_b else team_b
        losers[loser] += 1

    q+=1

    # Rounds 3 to N until promotion and elimination conditions are met
    def calculate_points():
        points = {}
        for team, opponents in history.items():
            team_points = sum(winners[opponent] - losers[opponent] for opponent in opponents)
            points[team] = team_points
        return points

    def decide_next_round_matches_based_on_points(winners, losers, points):
        grouped_by_record = defaultdict(list)
        for team in winners:
            if team not in promoted and team not in eliminated:
                record = (winners[team], losers[team])
                grouped_by_record[record].append(team)
    
        next_round_matches = []
        for record, teams in grouped_by_record.items():
            teams.sort(key=lambda x: (points[x], seed_no[x]))
            while teams:
                team_a = teams.pop(0)
                team_b = teams.pop() if teams else None
                if team_b:
                    next_round_matches.append((team_a, team_b))
        #print (points)
        return next_round_matches
    while q <5:
        q+=1
        
        # Calculate points for remaining teams
        points = calculate_points()
        # Decide next round matches based on points and win-loss records
        round_matches = decide_next_round_matches_based_on_points(winners, losers, points)
        for team_a, team_b in round_matches:
            winner = simulate_match(team_a, team_b)
            winners[winner] += 1
            loser = team_a if winner == team_b else team_b
            losers[loser] += 1
            # Update history
            history[winner].append(loser)
            history[loser].append(winner)
            # Check for promotions or eliminations after each match
            
            if winners[winner] == 3 and q!=3 :
                
                promoted.add(winner)
               
                   #debug using, just ignore
                #print(promoted)
            elif losers[loser] == 3 and q ==3:
                eliminated.add(loser)
               # print ("2")
                
            elif winners[winner] == 3 :
                pr30.add(winner)
            #print(q)
            #print(promoted)
            #print(pr30)

      
    return promoted
       

# Simulate the tournament 1000 times and track promotion probabilities
simulation_results = defaultdict(int)
res30 = defaultdict(int)
res03 = defaultdict(int)
#totaladv = defaultdict(int)

for _ in range(10000):
    promoted_teams = simulate_tournament()
    for team in promoted_teams:
        simulation_results[team] += 1
        
    for team in pr30:
        res30[team] += 1
        
    for team in eliminated:
       res03[team] += 1

  #  for team in  total:
   #    totaladv[team]  +=1


# Calculate probabilities

probq = {team: results / 100 for team, results in simulation_results.items()}
prob3_0 = {team: results / 100 for team, results in res30.items()}
prob0_3 = {team: results / 100 for team, results in res03.items()}
#totalprob = {team: results / 10 for team, results in totaladv.items()}



sorted_prob3 = {k: prob3_0[k] for k in sorted(prob3_0, key=lambda x: int(x.split('_')[1]))}
formatted_output3 = "\n".join([f"{team}: {prob:.3f}%" for team, prob in sorted_prob3.items()])

sorted_probq = {k: probq[k] for k in sorted(probq, key=lambda x: int(x.split('_')[1]))}
formatted_outputq = "\n".join([f"{team}: {prob:.3f}%" for team, prob in sorted_probq.items()])

sorted_prob0 = {k: prob0_3[k] for k in sorted(prob0_3, key=lambda x: int(x.split('_')[1]))}
formatted_output0 = "\n".join([f"{team}: {prob:.3f}%" for team, prob in sorted_prob0.items()])

#sorted_probt = {k: totalprob[k] for k in sorted(totalprob, key=lambda x: int(x.split('_')[1]))}
#formatted_outputtt = "\n".join([f"{team}: {prob:.3f}%" for team, prob in sorted_probt.items()])



print('prob of being advanved with 3:0')
print(formatted_output3)


print('prob of being advanved with 3:1 or 3:2')
print(formatted_outputq)


print('prob of being eliminated by 0:3')
print(formatted_output0)

#print('total prob of being advanced')
#print(formatted_outputtt)
