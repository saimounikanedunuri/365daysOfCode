from urlextract import URLExtract
from wordcloud import WordCloud
extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user!= 'Overall':
        df=df[df['user'] == selected_user]

    #fetch the number of messages
    num_messages = df.shape[0]

    #fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    #fetch number of media messages
    num_media_messages = df[df['message'].str.contains('<Media omitted>')].shape[0]

    #fetch number od links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x=df['user'].value_counts().head()
    df_percent=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()
    df_percent.columns=['name','percent']
    return x,df_percent

def create_wordcloud(selected_user,df):
    if selected_user!= 'Overall':
        df=df[df['user'] == selected_user]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc
