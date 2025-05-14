import requests

def count_words(subreddit, word_list, after=None, counter=None):
    if counter is None:
        counter = {}

    headers = {'User-Agent': 'MyRedditScraper'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if subreddit is invalid
    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])

    # Normalize word list (lowercase and merge duplicates)
    normalized_words = [word.lower() for word in word_list]
    merged_words = {}
    for word in normalized_words:
        if word in merged_words:
            merged_words[word] += 1
        else:
            merged_words[word] = 1

    # Count words in titles
    for post in posts:
        title = post['data']['title'].lower().split()
        for word in title:
            clean_word = ''.join([char for char in word if char.isalpha()])
            if clean_word in merged_words:
                if clean_word in counter:
                    counter[clean_word] += merged_words[clean_word]
                else:
                    counter[clean_word] = merged_words[clean_word]

    # Recursion if more posts
    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, counter)
    else:
        # Print sorted results
        if counter:
            sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_items:
                print(f"{word}: {count}")
