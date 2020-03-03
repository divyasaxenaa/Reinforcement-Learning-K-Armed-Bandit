#Name : Divya Saxena
#ID: 1001773376
import numpy as np
import graphplt as graphplt
import bandit as bandit

if __name__ == "__main__":
    bdt = bandit.BanditArmed(k=5, exp_rate=0.1, seed=1234,prob = "U",factor = 2)
    bdt.iterations(3500)
    avg_reward = bdt.avg_reward
    graphplt.graphplt(avg_reward, 1,"2. Uniform Distribution for Quadratic")
    graphplt.graphplt(bdt.utility, 2,"2. Uniform Distribution for Quadratic")

