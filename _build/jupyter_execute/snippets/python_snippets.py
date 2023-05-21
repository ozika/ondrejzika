#!/usr/bin/env python
# coding: utf-8

# ## Pandas tricks
# 
# ### DF Transformations
# #### Wide to long
# ```python
# tdf = tdf.melt(id_vars = ["Session", "PROLIFICID"], value_vars=columns)
# ```

# ### Lambda function
# 
# Take first value of each subgroup 
# 
# ```python
# df.groupby(by="Session")["date"].apply(lambda x: np.array(x.reset_index().iloc[0,1]))
# 
# ```

# ## Plotting (Seaborn and MPL)
# 
# ### Legend manipulation
# 
# Change labels on existing legend
# ```python
# for t, l  in zip(ax.get_legend().texts, new_labels):
#     t.set_text(l)
# ```
# 
# Remove legend border
# ```python
# ax.get_legend().get_frame().set_linewidth(0.0)
# ```
# 

# ## Statistics
# ```python
# import pingouin as pg
# from statsmodels.stats.multitest import multipletests
# aov = pg.mixed_anova(data=stdf, dv='value', between='cl', within='variable',
#                      subject='id', correction=False, effsize="np2")
# pg.print_table(aov)
# resdf = pd.DataFrame()
# for c in [0,1]:
#     tdf = stdf.loc[stdf["cl"]==c,:]
#     res = pg.ttest( x=tdf.loc[tdf["variable"]=="TF3_NegativeAffect","value"],
#                     y=tdf.loc[tdf["variable"]=="TF2_PhysiolAnx","value"],
#                     paired=True)
#     res["contrast"] = "TF3>TF2, cluster "+str(c)
#     resdf = pd.concat([resdf, res], axis=0)
# 
#     res = pg.ttest( x=tdf.loc[tdf["variable"]=="TF3_NegativeAffect","value"],
#                     y=tdf.loc[tdf["variable"]=="TF1_CognAnxDepr","value"],
#                     paired=True)
#     res["contrast"] = "TF3>TF1, cluster "+str(c)
#     resdf = pd.concat([resdf, res], axis=0)
# 
#     res = pg.ttest( x=tdf.loc[tdf["variable"]=="TF1_CognAnxDepr","value"],
#                     y=tdf.loc[tdf["variable"]=="TF2_PhysiolAnx","value"],
#                     paired=True)
#     res["contrast"] = "TF1>TF2, cluster "+str(c)
#     resdf = pd.concat([resdf, res], axis=0)
# 
# 
# 
# for t in trait_factor_names:
#     tdf = stdf.loc[stdf["variable"]==t,:]
#     res = pg.ttest( x=tdf.loc[tdf["cl"]==0,"value"],
#                     y=tdf.loc[tdf["cl"]==1,"value"],
#                     paired=False)
#     res["contrast"] = "cl0>cl1"+t
#     resdf = pd.concat([resdf, res], axis=0)
# 
# resdf["p-holm"] = np.round(multipletests(resdf["p-val"], alpha=0.05, method="holm")[1],4)
# pg.print_table(resdf)
# 
# ```
