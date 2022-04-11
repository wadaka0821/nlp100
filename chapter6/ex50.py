import pandas as pd

def split_data(df:pd.DataFrame, train:float=0.8, validate:float=0.1, test:float=0.1) -> list[pd.DataFrame]:
    if (train + validate + test != 1):
        print('train + validate + test != 1')
        return list()
    df = df.sample(frac=1)
    N = int(len(df))
    return [df[0:int(N * train)], df[int(N * train):int(N * (train + validate))], df[int(N * (train + validate)):]]

if __name__ == '__main__':
    filename = 'newsCorpora.csv'
    header = ['id', 'title', 'url', 'publisher', 'category', 'story_alphanumeric_id', 'hostname', 'timestamp']
    df = pd.read_table(filename, encoding='utf-8', header=None, index_col=[0])
    df = df.rename(columns={num:label for num, label in enumerate(header)})
    df = df[df['publisher'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
    df = df[['title', 'category']]
    train, validate, test = split_data(df)
    train.to_csv('./data/train.txt', sep='\t')
    validate.to_csv('./data/valid.txt', sep='\t')
    test.to_csv('./data/test.txt', sep='\t')
    print(train.head())
    print(len(train))
    print(validate.head())
    print(len(validate))
    print(test.head())
    print(len(test))