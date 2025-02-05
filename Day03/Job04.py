class Player:
    def __init__(self, name, number, position):
        self.player_name = name
        self.player_number = number
        self.player_position = position
        self.player_goals_scored = 0
        self.player_assists = 0
        self.player_yellow_cards = 0
        self.player_red_cards = 0

    def score_goal(self):
        self.player_goals_scored += 1

    def make_assist(self):
        self.player_assists += 1

    def receive_yellow_card(self):
        self.player_yellow_cards += 1

    def receive_red_card(self):
        self.player_red_cards += 1

    def display_stats(self):
        print(f"Name: {self.player_name}")
        print(f"Number: {self.player_number}")
        print(f"Position: {self.player_position}")
        print(f"Goals Scored: {self.player_goals_scored}")
        print(f"Assists: {self.player_assists}")
        print(f"Yellow Cards: {self.player_yellow_cards}")
        print(f"Red Cards: {self.player_red_cards}")
        print("\n")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_player_stats(self):
        print(f"{self.team_name} Team:")
        for player in self.players:
            player.display_stats()

    def update_player_stats(self, player_name, action):
        for player in self.players:
            if player.player_name == player_name:
                if action == "goal":
                    player.score_goal()
                elif action == "assist":
                    player.make_assist()
                elif action == "yellow":
                    player.receive_yellow_card()
                elif action == "red":
                    player.receive_red_card()
                break

player1 = Player("John Doe", 10, "Striker")
player2 = Player("Jane Smith", 7, "Midfielder")
player3 = Player("Bob Johnson", 3, "Defender")
player4 = Player("Alice Williams", 22, "Goalkeeper")

team1 = Team("Red")
team2 = Team("Blue")

team1.add_player(player1)
team1.add_player(player2)
team2.add_player(player3)
team2.add_player(player4)

print("Initial Player Stats:")
team1.display_player_stats()
team2.display_player_stats()

# team1.update_player_stats("John Doe", "goal")
# team1.update_player_stats("Jane Smith", "assist")
# team2.update_player_stats("Bob Johnson", "yellow")
# team2.update_player_stats("Alice Williams", "red")


# print("\nUpdated Player Stats:")
# team1.display_player_stats()
# team2.display_player_stats()