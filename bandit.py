#Name : Divya Saxena
#ID: 1001773376

import numpy as np
import graphplt as graphplt

class BanditArmed:
    def __init__(self, k=5, exp_rate=.1, lr=0.1, ucb=False, seed=None, c=2,prob = "U",factor = 1):
        self.k = k
        #actions = floors 0 to 5
        self.actions = range(self.k)
        print("range")
        print(range(self.k))
        self.exp_rate = exp_rate
        self.lr = lr
        self.total_reward = 0
        self.avg_reward = []
        self.prob = prob
        self.factor = factor
        self.TrueValue = []
        np.random.seed(seed)
        self.values = np.zeros(self.k)
        self.times = 0#no of actions
        self.action_times = np.zeros(self.k)
        self.ucb = ucb
        self.c = c
        self.utility = []
        self.liftfloorpos = []

    def vargenerated(self,prob):
        if prob == "U":
            return  np.random.uniform(0, 1)
        elif prob == "G":
            return np.random.gamma(0, 1)
        elif prob == "N":
            return np.random.normal(0, 1)
        else:
            return np.random.exponential(0, 1)



    def liftfloor(self):
        # explore
        print("explore")
        print(np.random.uniform(0, 1))
        x=self.vargenerated(self.prob)
        if x <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # exploit
            print("exploit")
            if self.ucb:
                if self.times == 0:
                    print("self.actions",self.actions)
                    action = np.random.choice(self.actions)
                else:
                    confidence_bound = self.values + self.c * np.sqrt(
                        np.log(self.times) / (self.action_times + 0.1))  # c=2
                    action = np.argmax(confidence_bound)
            else:
                action = np.argmax(self.values)
        print("final action")
        print(action)
        return action

    def callfloor(self):
        # explore
        print("explore")
        print(np.random.uniform(0, 1))
        x = self.vargenerated(self.prob)
        if x <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # exploit
            print("exploit")
            if self.ucb:
                if self.times == 0:
                    print("self.actions",self.actions)
                    action = np.random.choice(self.actions)
                else:
                    confidence_bound = self.values + self.c * np.sqrt(
                        np.log(self.times) / (self.action_times + 0.1))  # c=2
                    action = np.argmax(confidence_bound)
            else:
                action = np.argmax(self.values)
        print("final action")
        print(action)
        return action

    def exitfloor(self):
        # explore
        print("explore")
        print(np.random.uniform(0, 1))
        x = self.vargenerated(self.prob)
        if x <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # exploit
            print("exploit")
            if self.ucb:
                if self.times == 0:
                    print("self.actions",self.actions)
                    action = np.random.choice(self.actions)
                else:
                    confidence_bound = self.values + self.c * np.sqrt(
                        np.log(self.times) / (self.action_times + 0.1))  # c=2
                    action = np.argmax(confidence_bound)
            else:
                action = np.argmax(self.values)
        print("final action")
        print(action)
        return action



    def takeAction(self, liftfloor,callfloor,exitfloor):
        self.times += 1
        self.action_times[callfloor] += 1
        # take action and update value estimates
        reward = self.reward(liftfloor,callfloor,exitfloor)
        print("reward")
        print(reward)
        # using incremental method to propagate
        self.values[liftfloor] += self.lr * (reward - self.values[liftfloor])
        self.total_reward += reward
        self.avg_reward.append(self.total_reward / self.times)
        utility = self.totalutility(liftfloor,callfloor,exitfloor)
        self.utility.append(utility)
        self.liftfloorpos.append(liftfloor)
        print(self.utility)
        print(self.liftfloorpos)




    def reward(self,liftfloor,callfloor,exitfloor):
        reward=(abs(liftfloor-callfloor)+abs(callfloor-exitfloor)+1)
        rewardfact = pow(reward,self.factor)
        rewardf = -7 * rewardfact
        return rewardf

    def totalutility(self, liftfloor, callfloor, exitfloor):

        if callfloor > exitfloor:  # going down
            if callfloor == 6:  # exit floor 4 3 2 1
                return 1 * 1 / 4 * self.reward(liftfloor, callfloor, exitfloor)
            elif callfloor == 5:  # exit floor  3 2 1
                return 1 * 1 / 3 * self.reward(liftfloor, callfloor, exitfloor)
            elif callfloor == 4:  # exit floor   2 1
                return 1 * 1 / 2 * self.reward(liftfloor, callfloor, exitfloor)
            elif callfloor == 3:  # exit floor    1
                return 1 * 1 * self.reward(liftfloor, callfloor, exitfloor)
            elif callfloor == 2:  # exit floor    1
                return 0
            elif callfloor == 1:  # exit floor    1
                return 0

        else:  # going up
            return 1 * 1 / 5 * self.reward(liftfloor, callfloor, exitfloor)

    def iterations(self, iteration):
        for _ in range(iteration):
            liftfloor =self.liftfloor()
            callfloor =self.callfloor()
            exitfloor  =self.exitfloor()
            if callfloor == exitfloor :
                print("call floor and exit floor cant be same")
            else:
                self.takeAction(liftfloor,callfloor,exitfloor)





