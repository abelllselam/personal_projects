Exercise: Simple Interest Calculator
Goal: Write a Java program that computes simple interest and the total amount after interest.

Create a file named SimpleInterestCalculator.java.

Declare and initialize these variables at the top of your main method (choose sensible values):

double principal -– the initial amount of money (e.g. 1000.0)

double rate -– annual interest rate in percent (e.g. 5.0 for 5%)

int time -– time in years (e.g. 3)

Calculate:

Simple interest using the formula

java
Copy
Edit
double interest = principal _ rate _ time / 100;
Total amount after interest:

java
Copy
Edit
double totalAmount = principal + interest;
Print each of these, formatted clearly. For example:

yaml
Copy
Edit

```java
Principal: $1000.0
Rate: 5.0%
Time: 3 years
Interest: $150.0
Total Amount: $1150.0
```

Bonus tweaks (pick any):

Use underscores in your numeric literals (e.g. double principal = 1_000.0;).

Change time to something larger and rerun—what happens?

Cast your totalAmount to an int when printing (e.g. (int) totalAmount) and observe truncation.

Add another println that tells whether the interest earned is more or less than $200 using a comparison operator (e.g. interest > 200).
