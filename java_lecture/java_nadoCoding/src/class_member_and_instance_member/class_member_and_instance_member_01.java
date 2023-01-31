package class_member_and_instance_member;


class Calculator {
    static double pi = 3.14;
    static int base = 0;
    int left, right;

    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public void sum() {
        System.out.println(left + right);
    }

    public void avg() {
        System.out.println((left + right) / 2);
    }
}
public class class_member_and_instance_member_01 {
    public static void main(String[] args) {
        Calculator c1 = new Calculator();
        c1.setOprands(10, 20);
        System.out.println(c1.pi);

        Calculator c2 = new Calculator();

        System.out.println(c1.base);
        System.out.println(c2.base);

        c1.base += 10;
        System.out.println(c1.base);
        System.out.println(c2.base);

        c2.base += 10;
        System.out.println(c1.base);
        System.out.println(c2.base);

        Calculator c3 = new Calculator();
        System.out.println((c3.base));
    }
}
