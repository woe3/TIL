package chap_02;

public class _04_Operator4 {
    public static void main(String[] args) {
        //논리 연산자
        boolean buger = true;
        boolean kimchi = true;
        boolean steak = false;

        System.out.println(kimchi || steak || buger);
        System.out.println(kimchi && steak && buger);
        
        //놀리 부정 연산자
        System.out.println(!true);
        System.out.println(!false);
    }
}
