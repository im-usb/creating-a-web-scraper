class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.xp = 1500

    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.team}.")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        new_player = Player(player, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        print(f"Players in {self.team_name}:")
        for player in self.players:
            print(f"{player.name}")

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f"Player {player.name} removed.")
                return
        print(f"Player with name {player_name} not found.")

    def total_xp(self):
        total = 0
        for player in self.players:
            total += player.xp
        print(f"Total XP of {self.team_name}: {total}")


team_x = Team("Team X")
team_x.add_player("Nico")


# team_x.show_players()
# team_blue.show_players()

team_x.add_player("Jaden")
team_x.add_player("Rose")
team_x.show_players()
team_x.total_xp()

team_x.remove_player("Jaden")
team_x.show_players()
team_x.total_xp()
