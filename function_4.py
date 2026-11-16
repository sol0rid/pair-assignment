def gaps_in_fasta(path):
    count = 0
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                continue                  # заголовки не рахуємо
            count += line.count("N")      # скільки N у цьому рядку
    return count > 0, count

