w = input();lowercase = sum([1 for l in w if l in 'abcdefghijklmnopqrstuvwxyz']);uppercase = len(w)-lowercase;print(w.lower() if lowercase >= uppercase else w.upper())