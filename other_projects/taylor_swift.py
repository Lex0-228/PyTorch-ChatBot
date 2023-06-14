import os, re
def search(request, directory):
    request = re.compile(f'.*[\s\"\'\(]{request}[\s\"\'\,\)\!\?\.:-].*', flags=re.I)
    number_of_matches = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file = os.path.join(root, file)
            with open(file, 'r') as lyrics:
                txt = lyrics.read()
                results = set(re.findall(request, txt))
                for result in results:
                    print(f'{lyrics.name.strip(".txt")}: {result}')
                    number_of_matches += 1
    print(f'Unique matches found: {number_of_matches}')

def TaylorSwift():
    request = input("Enter word to search for: ")
    for album in ['Taylor Swift', 'Fearless', 'Speak Now', 'Red', '1989', 'Reputation', 'Lover', 'Folklore', 'Evermore', 'Midnights']:
        search(request, f'Discography\{album}')

