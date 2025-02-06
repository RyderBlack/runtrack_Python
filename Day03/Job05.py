class Character:
    def __init__(self,char_name, char_lives):
        self.__char_name = char_name
        self.__char_lives = char_lives
        
    def get_char_name(self):
        return self.__char_name
    
    def get_char_lives(self):
        return self.__char_lives
    
    def attack_player(self):
        if self.__char_lives > 0:
            self.__char_lives -= 1
            print(f"{self.__char_name} has been hit! Lives remaining: {self.__char_lives}")
        else:
            print("You are already dead!")
            
    
class GameManager:
    level = None
    
    def choose_level(self):
        choosed_level = int(input("Choose your level between 1 and 3, 1 being the easiest mode: "))
        match choosed_level:
            case 1:
                GameManager.level = 1
                print("You chose the Easy mode")
            case 2:
                GameManager.level = 2
                print("You chose the Normal mode")
            case 3:
                GameManager.level = 3
                print("You chose the Hard mode")
            case _:
                print("Please make a valid choice")
                return self.choose_level()
        return GameManager.level
    
    def check_health(self, player, enemy):
        print(f"\nHealth status:")
        print(f"{player.get_char_name()}: {player.get_char_lives()} lives")
        print(f"{enemy.get_char_name()}: {enemy.get_char_lives()} lives")
        
    def check_winner(self, player, enemy):
        if player.get_char_lives() <= 0:
            return f"{enemy.get_char_name()} wins!"
        elif enemy.get_char_lives() <= 0:
            return f"{player.get_char_name()} wins!"
        return None
    
    def launch_game(self):
        if GameManager.level is None:
            self.choose_level()
            
        match GameManager.level:
            case 1: 
                player_lives = 5
                enemy_lives = 3
            case 2: 
                player_lives = 4
                enemy_lives = 4
            case 3: 
                player_lives = 3
                enemy_lives = 5
                
        player = Character("Player", player_lives)
        enemy = Character("Enemy", enemy_lives)
        
        print(f"\nGame started!")
        self.check_health(player, enemy)
        
        return player, enemy
        
        
def main():
    game = GameManager()
    player, enemy = game.launch_game()
    
    while True:
        input("\nPress Enter to attack...")
        enemy.attack_player()
        
        winner = game.check_winner(player, enemy)
        if winner:
            print(winner)
            break
            
        print("\nEnemy's turn...")
        player.attack_player() 
        
        winner = game.check_winner(player, enemy)
        if winner:
            print(winner)
            break
        
        game.check_health(player, enemy)


if __name__ == "__main__":
    main()        
        
        
            
            
