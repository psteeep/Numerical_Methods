import matplotlib.pyplot as plt
import pandas as pd


def plot_graph(X, Y, ax=None):
    plt.figure(figsize=(15, 10))
    plt.plot(X, Y)
    # plt.axhline(linewidth=1.5, color='black')
    # plt.axvline(linewidth=1.5, color='black')
    plt.grid()
    plt.show()


# def plot_table(table_data, ax=None):
#     table_data = plt.np.round(table_data, decimals=2)
#     table = plt.table(
#         cellText=table_data.transpose(), rowLabels=("x¹", "x²", "x³"), cellLoc="center",
#     )
#     ax.axis("off")
#     ax.add_table(table)


def print_table(table_data):
    pd.options.display.float_format = '{:.4f}'.format
    df = pd.DataFrame(table_data, columns=("x¹", "x²", "x³"))
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
