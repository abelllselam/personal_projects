public class VariablesStepB {
    static int staticCount =2; //static class field
    int instanceCount =3; //instance (object) field

    public void demo() {
        int local = 0; //local variable (NOT intialized)
        System.out.println(local); //this will cause a compile error
    }

    public static void main(String [] args){
        VariablesStepB v = new VariablesStepB();
        v.demo();
        System.out.println("staticCount: " + staticCount);
        System.out.println("instanceCount: " + v.instanceCount);
    }
}
