import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def data_analysis():
    pd.read_csv("train.csv")
    pd.crosstab( df.target).plot(kind="bar", figsize=(15,6), colour=['#0ff0000', '#0000'])
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.legend([])
    plt.xtricks(rotation=0)
    plt.savefig('')

    pd.crosstab(df.target).plot(kind="bar", figsize=(15, 6), colour=['#0ff0000', '#0000'])
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.legend([])
    plt.xtricks(rotation=0)
    plt.savefig('')


    df.target.value_counts()
    sns.countplot(x="target", data=df, palette="bwr")
    plt.xlabel('')
    plt.ylabel('')
    plt.legend([])
    plt.savefig('')
