import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ctr = ads.groupby('ad_id')['action'].apply(lambda x: round(
        (100 * sum(x == "Clicked")/(sum(x == "Clicked") + sum(x == "Viewed"))) if 
        (sum(x == "Clicked") + sum(x == "Viewed")) > 0 else 0.00
    , 2)).reset_index()
    ctr.columns = ['ad_id', 'ctr']
    

    return ctr.sort_values(by = ['ctr', 'ad_id'], ascending = [False, True])
    