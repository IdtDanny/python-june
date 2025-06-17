evening = {'Kevin', 'John', 'James', 'Peter', 'Robert', 'Diane', 'Keza', 'Kai'}
day = {'Kai', 'Maurice', 'John', 'Peter', 'Diane', 'Keza', 'Mutoni', 'Vava'}
weekend = {'Rutabayiro', 'James', 'Robert', 'John', 'Mutoni', 'Epimaque', 'Gasana', 'Grace', 'Petronilla'}

# All sessions without duplicates
sessions = evening | day | weekend
print(f"Enrolled in all sessions without duplicates {sessions}")

# Evening session but not in other session
evening_only = evening - ( day | weekend)
print(f"Evening only are {evening_only}")

# Students in 3 sessions
three_session = evening & day & weekend
print(f"Enrolled in 3 sessions at once {three_session}")

# Evening session and weekend but not in day
evening_weekend = (evening | weekend) - day
print(f"Enrolled in evening and weekend but not in day {evening_weekend}")

# In day session only
day_only = day - (evening | weekend)
print(f"Enrolled in day only {day_only}")