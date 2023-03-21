
import random

# Define the list of possible exercises for leg day
exercises = {
    "Barbell Back Squats": {"sets": 5, "reps": 5},
    "Hip thrusts": {"sets": 3, "reps": 15},
    "Barbell Front Squats": {"sets": 4, "reps": 12},
    "Wall sits": {"sets": 3, "reps": "30s"},
    "Leg extensions": {"sets": 3, "reps": 20},
    "Hamstring curls": {"sets": 3, "reps": 15},
    "Calf raise": {"sets": 3, "reps": 12},
    "Tibialis extension": {"sets": 3, "reps": 12},
    "Romanian Split Squats": {"sets": 3, "reps": 12},
    "Kettlebell Swings": {"sets": 3, "reps": "30s"}
}

workout = random.sample(list(exercises),6)

#print(workout)
for item in workout:
    sets_reps = exercises[item]
    print(f"{item}: {sets_reps['sets']} sets of {sets_reps['reps']} reps")

