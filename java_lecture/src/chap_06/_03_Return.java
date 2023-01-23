package chap_06;

public class _03_Return {
    // 호텔 전화번호
    public static String getPhoneNumber() {
        String phoneNumber = "02-1234-1234";
        return phoneNumber;
    }

    public static void main(String[] args) {
        System.out.println(getPhoneNumber());
    }
}
