import matplotlib.pyplot as plt
import json

with open("data_join_hyper_1_500_.json","r") as fp:
    data = json.load(fp)
    x_axis = data["ticks"]
    others = {}
    for k in data.keys():
        if k != "ticks":
            others[k] = data[k]
    for k in others.keys():
        p = plt.plot(x_axis,others[k],label=k, marker='o')
        plt.legend()
    plt.show()