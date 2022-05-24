import pandas as pd
import numpy as np
from IPython.display import display

def add_prefix_to_colnames(df, prefix, fixed_col_name='account_id'):
    df = df.add_prefix(prefix)
    df = df.rename(index=str, columns={prefix+fixed_col_name : fixed_col_name})
    return df

def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)
    percentile_.__name__ = 'pct_%s' % n
    return percentile_

def onehot(df, col_name, prefix=None, drop=True):
    df = df.join(pd.get_dummies(df[col_name], prefix=prefix))
    if drop:
        df = df.drop([col_name], axis=1)
    return df

def summary_group_cate_data(main_df, add_df, col_names=list, how='left', on=['account_id'], validate='one_to_many', by="account_id"):
    t = pd.merge(main_df, add_df, how=how, on=on, validate=validate)
    t = t.groupby(by=by, as_index=False)[col_names].sum()
    return t

def summary_group_num_data(main_df, add_df, col_name=str, how='left', on=['account_id'], validate='one_to_many', by="account_id", high_freq=False):
    t = pd.merge(main_df, add_df, how=how, on=on, validate=validate)
    if high_freq:
        tt = t.groupby(by=by)[col_name].agg([min, max, np.var, percentile(25), percentile(50), percentile(75), sum]).reset_index()       
    else:
        tt = t.groupby(by=by)[col_name].agg([min, max, sum]).reset_index()

    tt['mean'] = t.groupby(by=by)[col_name].mean().reset_index(drop=True)
    tt['count'] = t.groupby(by=by)[col_name].count().reset_index(drop=True)

    return tt

def day_to_int(day_serie):
    return np.array([d.days for d in day_serie]).astype('int64')

def str_to_datetime(series, format='%Y-%m-%d'):
    return pd.to_datetime(series, format=format)

def summary_df(df, table_name=''):
    print(table_name)
    print(df.shape)
    display(df.head())
    print('missing value')
    display(df.isnull().sum())