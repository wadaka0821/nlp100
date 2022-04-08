import pandas as pd

if __name__ == '__main__':
    filename = 'newsCorpora.csv'
    header = ['id', 'title', 'url', 'publisher', 'category', 'story_alphanumeric_id', 'hostname', 'timestamp']
    df = pd.read_table(filename, encoding='utf-8', header=None, index_col=[0])
    df = df.rename(columns={num:label for num, label in enumerate(header)})
    print(len(df))
    df = df[df['publisher'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
    df = df[['title', 'category']]
    print(df.tail())
    print(len(df))