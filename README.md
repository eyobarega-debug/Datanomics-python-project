# Datanomics Python Final Project

A collection of 6 Python programs built as a final project.

---

## Project Structure

| File | Description |
|------|-------------|
| `q1_snack_bar.py` | Snack Bar Ordering System |
| `q2_grocery_cart.py` | Grocery Cart System |
| `q3_todo_list.py` | To-Do List Manager |
| `q4_movie_booking.py` | Movie Ticket Booking |
| `q5_quiz_game.py` | Quiz Game |
| `q6_log_analysis.py` | Log Record Analysis |

---

## Programs

### Q1 - Snack Bar Ordering System
Displays a list of snacks and drinks with item numbers and prices.
The user chooses items by number in a loop.
Keeps track of selected items and their prices.
Ends when the user types `done`.
Prints a receipt showing all selected items and total cost.

---

### Q2 - Grocery Cart System
Has a predefined dictionary of groceries with prices.
The user adds items by typing their names.
For each valid item, asks for the quantity.
Keeps adding to the cart until the user types `checkout`.
Displays a final bill showing each item, quantity, subtotal, and total.

---

### Q3 - To-Do List Manager
Allows users to add tasks with priorities (low, medium, high).
Users can view the list, delete tasks by number, and mark tasks as complete.
Keeps looping until the user types `exit`.
Shows a summary at the end: number of completed tasks vs pending.

---

### Q4 - Movie Ticket Booking Simulation
Shows a list of available movie titles, showtimes, and seat prices.
The user chooses a movie and number of tickets.
Confirms total price and asks if they want to book another movie.
Ends when they say `no` and displays total bookings and cost.

---

### Q5 - Quiz Game
Contains a list of questions stored in a list of dictionaries.
Asks the user each question and records their answers.
At the end displays the user score and correct answers for wrong questions.

---

### Q6 - Log Record Analysis
Cleans invalid log records where user is empty or action is None.
Counts actions per user and frequency of each action.
Displays cleaned record count, user activity summary, and most common action.

**Expected Output:**
```
Cleaned Records: 4
User Activity:
{
    "alice": 2,
    "bob": 2,
    "charlie": 0
}
Action Counts:
{
    "login": 2,
    "purchase": 1,
    "logout": 1
}
Most Common Action: login
```

---

## How to Run

Make sure Python 3 is installed, then run any program:

```
python q1_snack_bar.py
python q2_grocery_cart.py
python q3_todo_list.py
python q4_movie_booking.py
python q5_quiz_game.py
python q6_log_analysis.py
```

---

## Team Members

| Name | Branch |
|------|--------|
| Eyob Arega | eyob-branch |
| Yosef Bezabih | yosef-branch |
| Endegena Ayenew | Endegena-branch |

---

## Course
**Datanomics Technology**  
Introduction to python  — Final Project
