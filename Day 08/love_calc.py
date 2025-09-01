true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']

def calculate_love_score(name1, name2):
    t_score = 0
    l_score = 0
    lovers = name1 + name2
    lovers = lovers.lower()

    for letter in lovers:
        if letter in true:
            t_score += 1
        if letter in love:
            l_score += 1

    total = str(t_score) + str(l_score)
    
    print(f"\nLove Score = {total}")


calculate_love_score("Kanye West", "Kim Kardashian")