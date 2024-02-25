import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot(file):
    df = pd.read_csv(file)
    fig = plt.figure(figsize=(25, 10))
    sns.lineplot(data=df, x="day", y="views")
    plt.xticks(rotation=45)
    return fig
