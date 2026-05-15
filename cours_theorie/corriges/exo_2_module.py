def convert_to_second(user_input, is_hour=False):
    if is_hour:
        minutes = (int(user_input) * 60)
        secondes = minutes * 60
    else:
        secondes = int(user_input) * 60
    return secondes
