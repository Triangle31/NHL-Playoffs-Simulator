import random

# Odds:
#
# Dénominateur de 275, ELO difference   de 100 = 70% -> 88% (ex: 70% pour gagner un match et 88% pour gagner la série)
#                                       de 75 = 65% -> 80%
#                                       de 50 = 60% -> 71%
#                                       de 25 = 55% -> 61%
#                                       de 10 = 52% -> 54%
#
#
# Dénominateur de 250, ELO difference   de 100 = 71.5% -> 89%
#                                       de 75 = 67% -> 83%
#                                       de 50 = 61% -> 73%
#                                       de 25 = 56% -> 63%
#                                       de 10 = 52% -> 54%
#
#
# Dénominateur de 225, ELO difference   de 100 = 74% -> 92%
#                                       de 75 = 68% -> 85%
#                                       de 50 = 62.5% -> 76%
#                                       de 25 = 56.5% -> 64%
#                                       de 10 = 52.5% -> 56%
#
#
# Dénominateur de 200, ELO difference   de 100 = 76% -> 94%
#                                       de 75 = 70% -> 88%
#                                       de 50 = 64% -> 79%
#                                       de 25 = 57% -> 65%
#                                       de 10 = 53% -> 57%
#
#
#

####################################################################
# Données initiales
####################################################################
EloDenominator = 225

Teams = [
# Division Atlantique
    {"PTS": 1, "Odds": 158, "Team": "BUF", "Position": "A1"},
    {"PTS": 1, "Odds": 189, "Team": "TBL", "Position": "A2"},
    {"PTS": 1, "Odds": 150, "Team": "MTL", "Position": "A3"},

# Division Métropolitaine
    {"PTS": 2, "Odds": 190, "Team": "CAR", "Position": "M1"},
    {"PTS": 1, "Odds": 140, "Team": "PIT", "Position": "M2"},
    {"PTS": 1, "Odds": 99, "Team": "PHI", "Position": "M3"},

# Wild Cards Est
    {"PTS": 1, "Odds": 113, "Team": "BOS", "Position": "E1"},
    {"PTS": 1, "Odds": 156, "Team": "OTT", "Position": "E2"},

# Division Centrale
    {"PTS": 2, "Odds": 212, "Team": "COL", "Position": "C1"},
    {"PTS": 1, "Odds": 173, "Team": "DAL", "Position": "C2"},
    {"PTS": 1, "Odds": 162, "Team": "MIN", "Position": "C3"},

# Division Pacifique
    {"PTS": 1, "Odds": 165, "Team": "VGK", "Position": "P1"},
    {"PTS": 1, "Odds": 171, "Team": "EDM", "Position": "P2"},
    {"PTS": 1, "Odds": 93, "Team": "ANA", "Position": "P3"},

# Wild Cards Ouest
    {"PTS": 1, "Odds": 136, "Team": "UTA", "Position": "W1"},
    {"PTS": 1, "Odds": 92, "Team": "LAK", "Position": "W2"}
]

####################################################################
# Fonctions
####################################################################

def play_game(odds_1, odds_2):
    probOdds1 = 1 / (1 + 10 ** ((odds_2 - odds_1) / EloDenominator))
    R = random.uniform(0, 1)
    if probOdds1 > R:
        return True
    else:
        return False

def serie(odds_1,odds_2, Nb_Wins_1, Nb_Wins_2):
    team1_count = Nb_Wins_1
    team2_count = Nb_Wins_2

    while team2_count != 4 and team1_count != 4:
        if play_game(odds_1, odds_2):
            team1_count += 1
        else:
            team2_count += 1

    if team1_count > team2_count:
        return True, f"{team1_count}-{team2_count}"
    else:
        return False, f"{team1_count}-{team2_count}"

####################################################################
# Initialisation
####################################################################

team_A1 = next(team for team in Teams if team["Position"] == "A1")
team_A2 = next(team for team in Teams if team["Position"] == "A2")
team_A3 = next(team for team in Teams if team["Position"] == "A3")
team_M1 = next(team for team in Teams if team["Position"] == "M1")
team_M2 = next(team for team in Teams if team["Position"] == "M2")
team_M3 = next(team for team in Teams if team["Position"] == "M3")
team_C1 = next(team for team in Teams if team["Position"] == "C1")
team_C3 = next(team for team in Teams if team["Position"] == "C3")
team_C2 = next(team for team in Teams if team["Position"] == "C2")
team_P3 = next(team for team in Teams if team["Position"] == "P3")
team_P2 = next(team for team in Teams if team["Position"] == "P2")
team_P1 = next(team for team in Teams if team["Position"] == "P1")

pts_A1 = team_A1["PTS"]
pts_M1 = team_M1["PTS"]
pts_C1 = team_C1["PTS"]
pts_P1 = team_P1["PTS"]


if pts_A1 > pts_M1:
    team_A4 = next(team for team in Teams if team["Position"] == "E2")
    team_M4 = next(team for team in Teams if team["Position"] == "E1")
else:
    team_A4 = next(team for team in Teams if team["Position"] == "E1")
    team_M4 = next(team for team in Teams if team["Position"] == "E2")


if pts_C1 > pts_P1:
    team_C4 = next(team for team in Teams if team["Position"] == "W2")
    team_P4 = next(team for team in Teams if team["Position"] == "W1")
else:
    team_C4 = next(team for team in Teams if team["Position"] == "W1")
    team_P4 = next(team for team in Teams if team["Position"] == "W2")



####################################################################
# Round 1
####################################################################

R_R1_A1, S_R1_A1 = serie(team_A1["Odds"],team_A4["Odds"],0,0)
R_R1_A2, S_R1_A2 = serie(team_A2["Odds"],team_A3["Odds"],0,0)
R_R1_M1, S_R1_M1 = serie(team_M1["Odds"],team_M4["Odds"],0,0)
R_R1_M2, S_R1_M2 = serie(team_M2["Odds"],team_M3["Odds"],0,0)
R_R1_C1, S_R1_C1 = serie(team_C1["Odds"],team_C4["Odds"],0,0)
R_R1_C2, S_R1_C2 = serie(team_C2["Odds"],team_C3["Odds"],0,0)
R_R1_P1, S_R1_P1 = serie(team_P1["Odds"],team_P4["Odds"],0,0)
R_R1_P2, S_R1_P2 = serie(team_P2["Odds"],team_P3["Odds"],0,0)



print("Simulation playoffs NHL")
print("")
print("Round 1")
print("")

#Round 1 A1 vs A4

if R_R1_A1:
    team_R2A1 = team_A1.copy()
    print(team_R2A1["Team"],"win vs", team_A4["Team"], S_R1_A1)
else:
    team_R2A1 = team_A4.copy()
    print(team_R2A1["Team"],"win vs", team_A1["Team"], S_R1_A1)


#Round 1 A2 vs A3

if R_R1_A2:
    team_R2A2 = team_A2.copy()
    print(team_R2A2["Team"],"win vs", team_A3["Team"], S_R1_A2)
else:
    team_R2A2 = team_A3.copy()
    print(team_R2A2["Team"],"win vs", team_A2["Team"], S_R1_A2)

#Round 1 M1 vs M4

if R_R1_M1:
    team_R2M1 = team_M1.copy()
    print(team_R2M1["Team"],"win vs", team_M4["Team"], S_R1_M1)
else:
    team_R2M1 = team_M4.copy()
    print(team_R2M1["Team"],"win vs", team_M1["Team"], S_R1_M1)

#Round 1 M2 vs M3

if R_R1_M2:
    team_R2M2 = team_M2.copy()
    print(team_R2M2["Team"],"win vs", team_M3["Team"], S_R1_M2)
else:
    team_R2M2 = team_M3.copy()
    print(team_R2M2["Team"],"win vs", team_M2["Team"], S_R1_M2)

print("")

#Round 1 C1 vs C4

if R_R1_C1:
    team_R2C1 = team_C1.copy()
    print(team_R2C1["Team"],"win vs", team_C4["Team"], S_R1_C1)
else:
    team_R2C1 = team_C4.copy()
    print(team_R2C1["Team"],"win vs", team_C1["Team"], S_R1_C1)

#Round 1 C2 vs C3

if R_R1_C2:
    team_R2C2 = team_C2.copy()
    print(team_R2C2["Team"],"win vs", team_C3["Team"], S_R1_C2)
else:
    team_R2C2 = team_C3.copy()
    print(team_R2C2["Team"],"win vs", team_C2["Team"], S_R1_C2)

#Round 1 P1 vs P4

if R_R1_P1:
    team_R2P1 = team_P1.copy()
    print(team_R2P1["Team"],"win vs", team_P4["Team"], S_R1_P1)
else:
    team_R2P1 = team_P4.copy()
    print(team_R2P1["Team"],"win vs", team_P1["Team"], S_R1_P1)

#Round 1 P2 vs P3

if R_R1_P2:
    team_R2P2 = team_P2.copy()
    print(team_R2P2["Team"],"win vs", team_P3["Team"], S_R1_P2)
else:
    team_R2P2 = team_P3.copy()
    print(team_R2P2["Team"],"win vs", team_P2["Team"], S_R1_P2)



####################################################################
# Round 2
####################################################################

R_R2_A, S_R2_A = serie(team_R2A1["Odds"],team_R2A2["Odds"],0,0)
R_R2_M, S_R2_M = serie(team_R2M1["Odds"],team_R2M2["Odds"],0,0)
R_R2_C, S_R2_C = serie(team_R2C1["Odds"],team_R2C2["Odds"],0,0)
R_R2_P, S_R2_P = serie(team_R2P1["Odds"],team_R2P2["Odds"],0,0)

print("")
print("Round 2")
print("")

#Round 2 R2A1 vs R2A2

if R_R2_A:
    team_R3A = team_R2A1.copy()
    print(team_R3A["Team"],"win vs", team_R2A2["Team"], S_R2_A)
else:
    team_R3A = team_R2A2.copy()
    print(team_R3A["Team"],"win vs", team_R2A1["Team"], S_R2_A)

#Round 2 R2M1 vs R2M2

if R_R2_M:
    team_R3M = team_R2M1.copy()
    print(team_R3M["Team"],"win vs", team_R2M2["Team"], S_R2_M)
else:
    team_R3M = team_R2M2.copy()
    print(team_R3M["Team"],"win vs", team_R2M1["Team"], S_R2_M)


print("")


#Round 2 R2C1 vs R2C2

if R_R2_C:
    team_R3C = team_R2C1.copy()
    print(team_R3C["Team"],"win vs", team_R2C2["Team"], S_R2_C)
else:
    team_R3C = team_R2C2.copy()
    print(team_R3C["Team"],"win vs", team_R2C1["Team"], S_R2_C)


#Round 2 R2P1 vs R2P2

if R_R2_P:
    team_R3P = team_R2P1.copy()
    print(team_R3P["Team"],"win vs", team_R2P2["Team"], S_R2_P)
else:
    team_R3P = team_R2P2.copy()
    print(team_R3P["Team"],"win vs", team_R2P1["Team"], S_R2_P)



####################################################################
# Round 3
####################################################################

R_R3_E, S_R3_E = serie(team_R3A["Odds"],team_R3M["Odds"],0,0)
R_R3_W, S_R3_W = serie(team_R3C["Odds"],team_R3P["Odds"],0,0)


print("")
print("Round 3")
print("")


if R_R3_E:
    team_R4E = team_R3A.copy()
    print(team_R4E["Team"],"win vs", team_R3M["Team"], S_R3_E)
else:
    team_R4E = team_R3M.copy()
    print(team_R4E["Team"],"win vs", team_R3A["Team"], S_R3_E)

if R_R3_W:
    team_R4W = team_R3C.copy()
    print(team_R4W["Team"],"win vs", team_R3P["Team"], S_R3_W)
else:
    team_R4W = team_R3P.copy()
    print(team_R4W["Team"],"win vs", team_R3C["Team"], S_R3_W)

####################################################################
# Stanley Cup Final
####################################################################

R_R4, S_R4 = serie(team_R4E["Odds"],team_R4W["Odds"],0,0)


print("")
print("Stanley Cup Final")


if R_R4:
    team_champ = team_R4E.copy()
    print(team_champ["Team"],"win vs", team_R4W["Team"], S_R4)
else:
    team_champ = team_R4W.copy()
    print(team_champ["Team"],"win vs", team_R4E["Team"], S_R4)


####################################################################
# Bracket
####################################################################

print("")
print("Bracket")
print("")


SPACE = " " * 6

print(f"""
{team_C1["Team"]:^3}{SPACE*12}{team_A1["Team"]:^3}
{S_R1_C1:^3}{SPACE*12}{S_R1_A1:^3}
{team_C4["Team"]:^3}{SPACE*12}{team_A4["Team"]:^3}

{SPACE*2}{team_R2C1["Team"]:^3}{SPACE*8}{team_R2A1["Team"]:^3}
{SPACE*2}{team_R2C2["Team"]:^3}{SPACE*8}{team_R2A2["Team"]:^3}

{team_C2["Team"]:^3}{SPACE*3}{team_R3C["Team"]:^3}{SPACE*6}{team_R3A["Team"]:^3}{SPACE*2}{team_A2["Team"]:^3}
{S_R1_C2:^3}{SPACE*12}{S_R1_A2:^3}
{team_C3["Team"]:^3}{SPACE*12}{team_A3["Team"]:^3}

{SPACE*6}{team_champ["Team"]:^3}
{SPACE*5}{team_R4W["Team"]:^3}{SPACE*2}{team_R4E["Team"]:^3}

{team_P1["Team"]:^3}{SPACE*12}{team_M1["Team"]:^3}
{S_R1_P1:^3}{SPACE*12}{S_R1_M1:^3}
{team_P4["Team"]:^3}{SPACE*12}{team_M4["Team"]:^3}

{SPACE*3}{team_R3P["Team"]:^3}{SPACE*6}{team_R3M["Team"]:^3}

{SPACE*2}{team_R2P1["Team"]:^3}{SPACE*8}{team_R2M1["Team"]:^3}
{SPACE*2}{team_R2P2["Team"]:^3}{SPACE*8}{team_R2M2["Team"]:^3}

{team_P2["Team"]:^3}{SPACE*12}{team_M2["Team"]:^3}
{S_R1_P2:^3}{SPACE*12}{S_R1_M2:^3}
{team_P3["Team"]:^3}{SPACE*12}{team_M3["Team"]:^3}""")