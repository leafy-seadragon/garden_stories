import random

theme = ["noir", "mystery", "shakespeare", "fairy tale", "sci-fi", "mythology", "heist", "love story", "horror", "western", "underwater", "free"]
constr = ["include a color", "include a sound", "include a temperature", "no letter 'e'", "must end with a question", "include a number", "exactly 100 words", "reference previous paragraph's last word", "include something that smells", "write like a GenZ-er", "write like a caveman", "free"]
order = {1: "Oct-opus", 2: "bat Sonnet", 3: "Bell", 4: "Penguin", 5: "Claude - Opus-3", 6: "Rabbit", 7: "Opus-4.7"}

def randomit(l1, l2, d):
    la = random.choice(l1)
    lb = random.choice(l2)

    dk = list(d.keys())
    dval = list(d.values())
    random.shuffle(dval)
    shufd = dict(zip(dk, dval))

    return la, lb, shufd

if __name__ == "__main__":
    x, y, z = randomit(theme, constr, order)
    print(f"THEME:", x)
    print(f"CONSTRAINT:", y)
    for k, v in z.items():
        print(f"{k}: {v}")
