
import random
from collections import defaultdict

# Define the power values for each team
power_values = {f"team_{i}": 850 for i in range(1, 17) }
power_values["team_1"] = 950   #C9
power_values["team_2"] = 900   #EF
power_values["team_3"] = 900   #ENCE
power_values["team_4"] = 870   #APEKS
power_values["team_5"] = 875   #HEROIC
power_values["team_6"] = 810   #9PAND
power_values["team_7"] = 840   #SAW
power_values["team_8"] = 910   #FUR
power_values["team_9"] = 800   #ECST
power_values["team_10"] = 880   #MGLZ
power_values["team_11"] = 850   #IMP
power_values["team_12"] = 800   #PAIN
power_values["team_13"] = 800   #LVG
power_values["team_14"] = 835   #AMK
power_values["team_15"] = 800   #KOI
power_values["team_16"] = 785   #LEG

# Define a function to simulate a match between two teams, considering random fluctuation
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
    promoted = set()  # Tracks promoted teams
    eliminated = set()  # Tracks eliminated teams

    # Simulate first round
    round_matches = pairs_round_1
    for team_a, team_b in round_matches:
        winner = simulate_match(team_a, team_b)
        winners[winner] += 1
        losers[team_a if winner == team_b else team_b] += 1

    # Function to decide the next round's matches based on winners and selection rules
    def decide_next_round_matches(current_winners, current_losers):
        next_round_matches = []
        sorted_teams = sorted(current_winners.keys(), key=lambda x: (-current_winners[x], -power_values[x]))
        while sorted_teams:
            team_a = sorted_teams.pop(0)
            for opponent in reversed(sorted_teams):
                if current_winners[team_a] == current_winners[opponent]:
                    next_round_matches.append((team_a, opponent))
                    sorted_teams.remove(opponent)
                    break
        return next_round_matches

    # The swiss rounds start from round 3
    while len(promoted) < len(power_values) / 2:
        round_matches = decide_next_round_matches(winners, losers)
        for team_a, team_b in round_matches:
            winner = simulate_match(team_a, team_b)
            winners[winner] += 1
            losers[team_a if winner == team_b else team_b] += 1

            # Check for promotion
            if winners[winner] == 3:
                promoted.add(winner)

            # Check for elimination
            loser_team = team_a if winner == team_b else team_b
            if losers[loser_team] == 3:
                eliminated.add(loser_team)

    return promoted

# Simulate the tournament  n times and track probabilities to be qualified. n=10000 here
simulation_results = defaultdict(int)

for _ in range(10000):
    promoted_teams = simulate_tournament()
    for team in promoted_teams:
        simulation_results[team] += 1

# Calculate probabilities
probabilities = {team: results / 100 for team, results in simulation_results.items()}
sorted_probabilities = {k: probabilities[k] for k in sorted(probabilities, key=lambda x: int(x.split('_')[1]))}
formatted_output = "\n".join([f"{team}: {prob:.3f}%" for team, prob in sorted_probabilities.items()])
print(formatted_output)

