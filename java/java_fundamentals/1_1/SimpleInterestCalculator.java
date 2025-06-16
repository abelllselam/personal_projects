public class SimpleInterestCalculator{
    public static void main(String [] args){
        double principal = 1000.0;
        double rate = 5;
        int time = 3;

        double interest = principal * rate * time/100;

        double totalAmount = principal + interest;

        System.out.println("principal: " + principal);
        System.out.println("Rate: " + rate + " %");
        System.out.println("Time: " + time + " years");
        System.out.println("Interest: $" + interest);
        System.out.println("Total Amount: " + totalAmount);
    }
}