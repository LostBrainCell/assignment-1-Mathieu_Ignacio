# SDEV 1001 - Assignment 1: Theme Park Weather Discount Day

This assignment covers introduction to programming, version control, variables, calculations, random numbers, boolean decisions, and making decisions with `if`, `elif`, and `else`.

## Best Practices

- Follow the PEP-8 Style guide for writing Python code https://peps.python.org/pep-0008/
- Name the files **exactly** as described by the assignment 


## Scenario

You have been hired by **Dragon Coaster Park** to create a small ticket booth program.

The park changes prices based on the guest's age, coupons, parking, snack passes, and a random daily weather event.

The goal is to practise:

- variables
- user input
- integer conversion
- calculations
- generating random numbers
- boolean variables
- decision making
- comparing values
- building a final total

---

## Files

You will complete two Python files:

```text
simple_ticket_booth.py
theme_park_weather_day.py
```

---

## Running the Automated Tests Locally

- You can run the automated tests locally by typing this command into the command line (exclude the .py from the filename):
```bash
python -m automated-tests-do-not-touch.<name_of_test_file>
```
- To test Part 1 (simple_ticket_booth.py), run this command:
```bash
python -m automated-tests-do-not-touch.part_1_simple_ticket_booth
```
- To test Part 2 (theme_park_weather_day.py), run this command:
```bash
python -m automated-tests-do-not-touch.part_2_theme_park_weather_day
```
- Your current working directory must be the parent directory of your assignment (assignment-1-yourname/).

### Assignment General Requirements

- Appropriate mathematical and logical operations are used to generate the expected results
- Allow the user to enter menu options in any case. For example, 'yes' and 'Yes' should be considered equal
- Currency should be formatted to 2 decimal places

# Part 1: Simple Ticket Booth

In this part, you will create a simple ticket booth program. See the Desired Output section for examples of how the output should look.

## Instructions

1. Generate a random mystery discount between $1.00 and $5.00 (whole numbers only):

2. Ask the user if they would like to buy a ticket.

- If the user enters `"yes"`, continue with the ticket purchase.
- If the user enters `"no"`, display `"Thanks, maybe next time"`.
- If the user enters anything else, display `"Invalid input, Please try again"`.

3. If the user buys a ticket, ask for the guest's age.

4. Ask whether the guest has a coupon. All coupons are for $5.00

5. Determine the base ticket price based on the following table.

| Guest Age | Base Ticket Price |
| --------- | ----------------- |
| under 5   | Free              |
| 5 to 12   | $12.00            |
| 13 to 64  | $25.00            |
| 65+       | $15.00            |

6. If the guests age is under 5 do not ask if they have a coupon (ticket is free).
   
7. If the guest has a coupon and the ticket is not free, subtract 5 dollars from the ticket price.

8. If the ticket is not free, apply the random mystery discount.

9. Display the final ticket price.

---

## Part 1 Desired Output

Because the discount is random, your exact discount amount may be different.

### User does not want to buy a ticket

```text
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) no
Thanks, maybe next time
```

### Invalid input

```text
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) potato
Invalid input, Please try again
```

### Child ticket with coupon and random discount

```text
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 10
Do you have a coupon? (yes/no) yes
Mystery discount: $3.00
Your ticket costs $4.00 
```
### Adult ticket without coupon and random discount

```text
$ python simple_ticket_booth.py
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 30
Do you have a coupon? (yes/no) no
Mystery discount: $4.00 
Your ticket costs $21.00
```

### Free ticket

```text
$ python simple_ticket_booth.py
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 4
Your ticket is free
```

---

# Part 2: Theme Park Weather Day

In this part, you will expand the program. The guest can add parking and a snack pass. The park will also have a random weather event that changes the total. See the Desired Output section for examples of how the output should look.

This part gives more practice with calculations, random numbers, boolean decisions, and nested decision logic.

## Instructions

1. Copy your working Part 1 code into `theme_park_weather_day.py`.

2. Generate a random weather rating between 1 and 3 (whole numbers only):

3. Use the weather rating to determine the weather disount (if any):

| Weather Rating | Weather Description | Discount                 |
| -------------- | ------------------- | ------------------------ |
| 1              | Sunny               | no change                |
| 2              | Rainy               | snack pass is half price |
| 3              | Stormy              | parking is free          |

4. Only ask about extras if the user chose to buy a ticket.

5. Ask if the guest needs parking. Parking costs $10.00.

6. Ask if the guest wants a snack pass. Snack passes cost $8.00.

7. Display the weather description.

Use one of these messages:

```text
Weather description: Sunny
Weather description: Rainy
Weather description: Stormy
```

8. Apply the weather rating.

- Sunny: no price change.
- Rainy: if the guest wants a snack pass, the snack pass is 1/2 price.
- Stormy: if the guest needs parking, parking is free.

---

## Part 2 Desired Output

Because the mystery discount and weather event are random, your exact output may be different.

### Adult ticket, parking, snack pass, sunny weather

```text
$ python theme_park_weather_day.py
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 30
Do you have a coupon? (yes/no) no
Mystery discount: $2.00
Your ticket costs $23.00
Do you need parking? (yes/no) yes
Do you want a snack pass? (yes/no) yes
Weather Description: Sunny
Parking added
Snack pass added
Your final total is $41.00
```

### Adult ticket, snack pass, rainy weather

```text
$ python theme_park_weather_day.py
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 30
Do you have a coupon? (yes/no) no
Mystery discount: $5.00
Your ticket costs $20.00
Do you need parking? (yes/no) no
Do you want a snack pass? (yes/no) yes
Weather Description: Rainy
Snack pass added
Rainy day snack discount applied
Your final total is $24.00
```

### Senior ticket with coupon, parking, stormy weather

```text
$ python theme_park_weather_day.py
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 70
Do you have a coupon? (yes/no) yes
Mystery discount: $2.00
Your ticket costs $8.00
Do you need parking? (yes/no) yes
Do you want a snack pass? (yes/no) no
Weather Description: Stormy
Parking added
Stormy day free parking applied
Your final total is $8.00
```

### Free ticket with snack pass

```text
$ python theme_park_weather_day.py
Welcome to Dragon Coaster Park
Would you like to buy a ticket? (yes/no) yes
Enter the guest age: 4
Your ticket is free
Do you need parking? (yes/no) no
Do you want a snack pass? (yes/no) yes
Weather Description: Sunny
Snack pass added
Your final total is $8.00
```

---

# Rubric

This assignment contains a code review component. Please refer to the What is a Code Review document in Brightspace under the "Welcome - Start Here" section for more details on the Code Review portion of this assignment.

## 3 Points - Best Practices
| Level        | Feedback Description                    |
| ------------ | --------------------------------------- |
| Excellent    | Best Practices followed.                |
| Satisfactory | Best Practices mostly followed.         |
| Poor         | Some Best Practices followed.           |
| Missing      | Program does not follow Best Practices. |

## 6 points - Part 1: Simple Ticket Booth

| Level                | Feedback Description                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| Excellent            | Tests pass. Program output matches desired output. Requirements met.              |
| Satisfactory         | Tests pass but program output varies slightly from desired output. Most requirements met.                  |
| Incomplete/Incorrect | Tests don't pass and program output differs partially from desired output. Some requirements met.          |
| Poor                 | Tests don't pass. Program output is significantly different than desired output. Requirements not met. |
| Missing              | Broken/Missing/Way Off                                                                                     |

## 8 points - Part 2: Theme Park Weather Day

| Level                | Feedback Description                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| Excellent            | Tests pass. Program output matches desired output. Requirements met.                                  |
| Satisfactory         | Tests pass but program output varies slightly from desired output. Most requirements met.                  |
| Incomplete/Incorrect | Tests don't pass and program output differs partially from desired output. Some requirements met.          |
| Poor                 | Tests don't pass. Program output is significantly different than desired output. Requirements not met. |
| Missing              | Broken/Missing/Way Off                                                                                     |


## Academic Integrity Note.

You must demonstrate incremental development of your solution. This means that you must begin work on your solution as soon as possible and commit, **at minimum**, after each part. Each commit must demonstrate functional improvements to the solution. Failure to show incremental work during the assignment period will result in loss of marks of up to 20%.

Additionally, you are encouraged to use external resources to help you learn what is needed for the assignment. However, if you submit code that differs greatly from what was demonstrated in class it must be documented (e.g. comments, citations, etc.) and you may be asked to provide a verbal explanation of how the code works to your instructor. Failure to explain any code you submitted will be considered as potential evidence of academic misconduct and may trigger an investigation, potentially resulting in further consequences.