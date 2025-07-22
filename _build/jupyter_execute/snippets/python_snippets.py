#!/usr/bin/env python
# coding: utf-8

# # Python snippets
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
# ### Scatter plot with lmplot and correlation for each group
# 
# ```python
# f, ax = plt.subplots(1,1,figsize=(5,5))
# cols= ["black", "red"]
# for lidx, lvl in enumerate(["high", "low"]):
#     ttdf = behdf.loc[behdf["TF2_PhysiolAnx_ms"].isin([lvl])]
#     sns.regplot(data=ttdf, x="prob_safe", y="shnosh_diff_mflr", color=cols[lidx], ax=ax)
#     corrfunc(ttdf["prob_safe"], ttdf["shnosh_diff_mflr"], tests=[ "spearman"], drop_missing=True, xanchor=0.4, yanchor=0+lidx*0.06, boxcolor=cols[lidx])
# ```
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

# ## Statistics in Python
# 
# ### Universal correlation function to add to plots
# ```python
# def corrfunc(x, y, tests=["pearson"], drop_missing=False, ax=None, xanchor=0.4, yanchor = 0.1, randomanchor=False, boxcolor='purple', **kws):
#     if (ax is None):
#         ax = plt.gca()
#     
#     if randomanchor:
#         yanchor=0.1 + np.random.normal(0, 0.2)
#         
#         
#     if drop_missing:
#         d = pd.DataFrame({'x':np.array(x), 'y':np.array(y)})
#         d = d.dropna()
#         x = d["x"]
#         y = d["y"]
# 
#     #["pearson", "spearman", "kendall", "distcor"]
#     
#     ycoord = yanchor*len(tests) + 0.05
#     if "pearson" in tests:
#         r,p = stats.pearsonr(x, y)
#         t = plt.text(xanchor, ycoord, "Pearson r = {:.2f}, p={:.2g}".format(r,p), transform=ax.transAxes, fontsize=10)
#         t.set_bbox(dict(facecolor='white', alpha=1, edgecolor=boxcolor))
#         ycoord = ycoord-0.1
#         
#     if "spearman" in tests:
#         r,p = stats.spearmanr(x, y)
#         t = plt.text(xanchor, ycoord, "Spearman r = {:.2f}, p={:.2g}".format(r,p), transform=ax.transAxes, fontsize=10)
#         t.set_bbox(dict(facecolor='white', alpha=1, edgecolor=boxcolor))
#         ycoord = ycoord-0.1
# 
#     if "xicor" in tests:
#         r = xicor(x,y, ties=True)
#         t = plt.text(xanchor, 0.05, "xicor. xi= {:.2f}".format(r), transform=ax.transAxes, fontsize=10)
#         t.set_bbox(dict(facecolor='white', alpha=1, edgecolor=boxcolor))
#         ycoord = ycoord-0.1
#     
#     if "distcor" in tests:
#         r2 = Dcorr(x,y)
#         t = plt.text(xanchor, 0.05, "Dist. corr = {:.2f}".format(r2), transform=ax.transAxes, fontsize=10)
#         t.set_bbox(dict(facecolor='white', alpha=1, edgecolor=boxcolor))
# 
# # More info in xicor: https://arxiv.org/abs/1909.10140
# def xicor(X, Y, ties=True):
#     random.seed(42)
#     n = len(X)
#     order = array([i[0] for i in sorted(enumerate(X), key=lambda x: x[1])])
#     if ties:
#         l = array([sum(y >= Y[order]) for y in Y[order]])
#         r = l.copy()
#         for j in range(n):
#             if sum([r[j] == r[i] for i in range(n)]) > 1:
#                 tie_index = array([r[j] == r[i] for i in range(n)])
#                 r[tie_index] = random.choice(r[tie_index] - arange(0, sum([r[j] == r[i] for i in range(n)])), sum(tie_index), replace=False)
#         return 1 - n*sum( abs(r[1:] - r[:n-1]) ) / (2*sum(l*(n - l)))
#     else:
#         r = array([sum(y >= Y[order]) for y in Y[order]])
#         return 1 - 3 * sum( abs(r[1:] - r[:n-1]) ) / (n**2 - 1)
# ```
# 
# ### Mixed ANOVA with posthocs in Python
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

# 
