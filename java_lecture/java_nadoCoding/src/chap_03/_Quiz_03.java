package chap_03;

public class _Quiz_03 {
    public static void main(String[] args) {
        String socialNumber = "901027-1234567";
        System.out.println(socialNumber.substring(0, socialNumber.indexOf("-")+2));
    }
}
