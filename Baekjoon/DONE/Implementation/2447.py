def recursive(n):
    if n == 3:
        return ["***","* *","***"]
    else:
        prev = recursive(n//3)
        top_bot = []
        for i in range(len(prev)):
            top_bot.append(prev[i]*3)
        mid = []
        for i in range(len(prev)):
            mid.append(prev[i]+" "*(n//3)+prev[i])
        return top_bot + mid + top_bot


n = int(input())
print("\n".join(recursive(n)))
