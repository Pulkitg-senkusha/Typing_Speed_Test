import time

def calculate_results(given_text, user_input, start_time, end_time):
    try:
        time_taken = end_time - start_time
        correct_chars = sum(a == b for a, b in zip(given_text, user_input))
        accuracy = (correct_chars / len(given_text)) * 100 if given_text else 0
        words_typed = len(user_input.split())
        wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0

        return {
            "time_taken": round(time_taken, 2),
            "accuracy": round(accuracy, 2),
            "wpm": round(wpm, 2),
            "correct_characters": f"{correct_chars}/{len(given_text)}"
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return{"error":str(e)}