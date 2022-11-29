from pydoc import describe
import pandas as pd
from Tab import tab 
from Sportsbet import sb
from Bookmaker import bk
# tab1 = pd.read_csv("Tab.csv")
# bk1 = pd.read_csv("Bookmaker.csv")
# sb1 = pd.read_csv("Sportsbet.csv")
tab1 = tab()
bk1 = bk()
sb1 = sb()
sb1["site"] = "SportsBet"
bk1["site"] = "BookMaker"
tab1["site"] = "Tab"
frames = [sb1,bk1,tab1]
final = pd.concat(frames, axis = 0, join='outer', ignore_index=True)

final["name1"] = final["name1"].str.lower()
final["name2"] = final["name2"].str.lower()

for a,b in set(zip(list(final["name1"]),list(final["name2"]))):
    match = final.loc[(final["name1"]==a) & (final["name2"]==b)]
    if len(match)>1:
        try:
            od1 = match["odds1"].max()
            od2 = match["odds2"].max()
            site1 = str(match[match["odds1"]==od1]["site"].values)
            site2 = str(match[match["odds2"]==od2]["site"].values)
            od1 = float(od1)
            od2 = float(od2)
            total = od1+od2
            bet1 = round(od2/total,2)
            bet2 = round(od1/total,2)
            comp = str(match["comp"].values)
            if (1/od1+1/od2)*100<100:
                print("Comp: {} {} v {}: odds: {} \n{} : {} multiplier: {} \n{} : {} multiplier: {}\n".format(comp,a,b,round((1/od1+1/od2)*100,2),site1,od1,bet1,site2,od2,bet2))
        except:
            continue