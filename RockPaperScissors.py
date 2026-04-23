def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return "R"

    # Counter move helper
    def counter(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    # --- Strategy 1: Beat last move ---
    guess1 = counter(opponent_history[-1])

    # --- Strategy 2: Frequency analysis ---
    from collections import Counter
    count = Counter(opponent_history)
    most_common = count.most_common(1)[0][0]
    guess2 = counter(most_common)

    # --- Strategy 3: Pattern detection (last 3 moves) ---
    guess3 = "R"
    if len(opponent_history) >= 3:
        last_pattern = opponent_history[-3:]
        matches = []

        for i in range(len(opponent_history) - 3):
            if opponent_history[i:i+3] == last_pattern:
                matches.append(opponent_history[i+3] if i+3 < len(opponent_history) else None)

        matches = [m for m in matches if m]
        if matches:
            from collections import Counter
            prediction = Counter(matches).most_common(1)[0][0]
            guess3 = counter(prediction)

    # --- Strategy 4: Cycle prediction (like Quincy bot) ---
    cycle = ["R", "P", "S"]
    if len(opponent_history) >= 1:
        last = opponent_history[-1]
        predicted = cycle[(cycle.index(last) + 1) % 3]
        guess4 = counter(predicted)
    else:
        guess4 = "R"

    # Combine strategies (majority vote)
    guesses = [guess1, guess2, guess3, guess4]

    from collections import Counter
    final_move = Counter(guesses).most_common(1)[0][0]

    return final_move
