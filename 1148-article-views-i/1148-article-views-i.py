import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[(views['author_id'] == views['viewer_id']), ['author_id']]
    return df.rename(columns = {'author_id': 'id'}).drop_duplicates().sort_values('id')
    