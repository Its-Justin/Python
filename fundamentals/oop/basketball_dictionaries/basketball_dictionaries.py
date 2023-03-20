players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]





class Player:
    def __init__(self, info):
        self.name = info['name']
        self.age = info['age']
        self.position = info['position']
        self.team = info['team']

    def display_info(self):
        print(f"Player: {self.name}, Age:{self.age}, Position:{self.position}, Team: {self.team}")
        return

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    }
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    }
justin = {
    "name": "Justin Ramirez", 
    "age":28, "position": "Point Guard", 
    "team": "Lakers"
    }


player1 = Player(kevin)
player2 = Player(jason)
player3 = Player(kyrie)
player4 = Player(justin)

player1.display_info()
player2.display_info()
player3.display_info()
player4.display_info()
