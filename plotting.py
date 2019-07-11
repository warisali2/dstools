from matplotlib import pyplot as plt
import seaborn as sns


def scatter_column(x_attrs, y_attr, df,
                   figsize=(20, 15),
                   alpha=1,
                   dtype='numerical',
                   sort=True):

    """
    Plots a column of graphs between y_attr (numerical) and list of x_attrs (numerical or categorical)
    Uses scatter plot for numerical x_attributes and seaborn's catplot for categorical attributes

    :param x_attrs: list of x_attributes
    :param y_attr: Y axis attribute to plot against
    :param df: Pandas DataFrame of data
    :param figsize: Size of each figure
    :param alpha: alpha value of each figure
    :param dtype: type of values in x_attributes i.e. numerical or categorical
    :param sort: sort x_attr by value counts?
    :return: None
    """

    fig, axarr = plt.subplots(len(x_attrs), 1, figsize=figsize)

    for i, attr in enumerate(x_attrs):
        if dtype is 'numerical':
            df.plot.scatter(x=attr, y=y_attr, ax=axarr[i], alpha=alpha)
        if dtype is 'categorical':
            if sort is True:
                sns.catplot(x=attr, y=y_attr, data=df, ax=axarr[i], order=df[attr].value_counts().index, alpha=alpha)
            else:
                sns.catplot(x=attr, y=y_attr, data=df, ax=axarr[i], alpha=alpha)
