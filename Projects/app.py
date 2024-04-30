import streamlit as st
from preprocessor import rawToDf
import helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp chat analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    # Assuming 'file' and 'key' parameters for the rawToDf function
    file = 'whatsapp-chat-data.txt'  # Provide the name of your input file here or specify its path
    key = '12hr'  # Specify the key for splitting and formatting, could be '12hr', '24hr', or 'custom'

    # Call the rawToDf function
    df = rawToDf(file, key)

    st.dataframe(df)

    #fetch unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(num_links)

        #finding the busiest users in the group(group level)
        if selected_user == 'Overall':
            st.title('Most busy users')
            x,new_df=helper.most_busy_users(df)
        else:
            st.title(f'Most busy users in {selected_user}')
            filtered_df = df[df['user'] == selected_user]
            x, new_df = helper.most_busy_users(filtered_df)

            fig,ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        #WordCloud
        st.title("WordCloud")
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
