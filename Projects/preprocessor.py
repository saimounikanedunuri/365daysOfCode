import re
import pandas as pd


def rawToDf(file, key):
    '''Converts raw .txt file into a Data Frame'''

    split_formats = {
        '12hr': '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[APap][mM]\s-\s',
        '24hr': '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s',
        'custom': ''
    }
    datetime_formats = {
        '12hr': '%d/%m/%Y, %I:%M %p - ',
        '24hr': '%d/%m/%Y, %H:%M - ',
        'custom': ''
    }

    with open(file, 'r', encoding='utf-8') as raw_data:
        # print(raw_data.read())
        raw_string = ' '.join(raw_data.read().split(
            '\n'))  # converting the list split by newline char. as one whole string as there can be multi-line messages
        user_msg = re.split(split_formats[key], raw_string)[
                   1:]  # splits at all the date-time pattern, resulting in list of all the messages with user names
        date_time = re.findall(split_formats[key], raw_string)  # finds all the date-time patterns

        df = pd.DataFrame({'date_time': date_time, 'user_msg': user_msg})  # exporting it to a df

    # converting date-time pattern which is of type String to type datetime,
    # format is to be specified for the whole string where the placeholders are extracted by the method
    df['date_time'] = pd.to_datetime(df['date_time'], format=datetime_formats[key])

    # split user and msg
    usernames = []
    msgs = []
    for i in df['user_msg']:
        a = re.split('([\w\W]+?):\s',
                     i)  # lazy pattern match to first {user_name}: pattern and spliting it aka each msg from a user
        if (a[1:]):  # user typed messages
            usernames.append(a[1])
            msgs.append(a[2])
        else:  # other notifications in the group(eg: someone was added, some left ...)
            usernames.append("group_notification")
            msgs.append(a[0])

    # creating new columns
    df['user'] = usernames
    df['message'] = msgs

    # dropping the old user_msg col.
    df.drop('user_msg', axis=1, inplace=True)

    df['year'] = df['date_time'].dt.year
    df['date_time'].dt.month_name()
    df['month'] = df['date_time'].dt.month_name()
    df['day'] = df['date_time'].dt.day
    df['hour'] = df['date_time'].dt.hour
    df['minute'] = df['date_time'].dt.minute

    return df