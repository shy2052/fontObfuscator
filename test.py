from src.core import obfuscate_keep

if __name__ == '__main__':
    print(obfuscate_keep(
        '百度一下你就知道',
        '中国智造慧及全球',
        'MyWTF', 'WTF', '.'))
