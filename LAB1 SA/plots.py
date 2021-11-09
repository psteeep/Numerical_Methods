import matplotlib.pyplot as plt
import pandas as pd


def plot_graph(X, Y, ax=None):
    plt.figure(figsize=(15, 10))
    plt.plot(X, Y)
    plt.grid()
    plt.show()


def print_table(table_data):
    pd.options.display.float_format = '{:.4f}'.format
    df = pd.DataFrame(table_data, columns=("x¹", "x²", "x³"))
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
