from random import randint, shuffle

class Hat():
    def __init__(self, **kwargs):
        self.balls = kwargs
    
    def amount(self):
        return sum([self.balls[key] for key in self.balls])

def experiment(hat: Hat, expected_balls:dict, num_balls_drawn:int, num_experiments:int):
    count = hat.amount()
    
    M = 0
    for exp in range(num_experiments):
        balls = []

        for key in hat.balls:
            balls += [key for i in range(hat.balls[key])]

        shuffle(balls)

        picked_balls = {key:0 for key in expected_balls}
        
        for i in range(num_balls_drawn):
            index = randint(0, count-1)
            ball = balls[index]

            if ball in picked_balls:
                picked_balls[ball] += 1

                flag = False
                for pb in picked_balls:
                    if picked_balls[pb] == expected_balls[pb]:
                        flag = True
                    else:
                        flag = False
                        break
                        
                if flag: 
                    M += 1
    
    return M / num_experiments
