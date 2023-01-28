package class_and_instance;

public class class_and_instance_02 {

    public static void sum(int left, int right) {
        System.out.println(left + right);
    }

    public static void avg(int left, int right) {
        System.out.println((left + right)/2);
    }

    public static void main(String[] args) {
        int left, right;
        left = 20;
        right = 30;
        sum(left, right);
        avg(left, right);
    }
}
