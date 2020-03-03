#Name : Divya Saxena
#ID: 1001773376
import matplotlib.pyplot as plt

def graphplt(reward,graphseq,label) :
        plt.figure(figsize=[8, 6])

        if graphseq == 1 :
                plt.plot(reward,label = label)
                plt.xlabel("Iteration", fontsize=14)
                plt.ylabel("avg reward", fontsize=14)
        else:
                 plt.plot(reward,color='olive',label = label)
                 plt.xlabel("Iteration", fontsize=14)
                 plt.ylabel("Utility", fontsize=14)
        plt.legend()
        plt.show()

