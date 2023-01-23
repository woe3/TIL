package chap_04;

public class _10_Break {
    public static void main(String[] args) {
        // break
        int max = 20;
        for (int i = 1; i < 50; i++) {
            System.out.println(i + "번 손님, 주문하신 음식 나왔습니다.");
            if (i == max) {
                System.out.println("재료가 모두 소진되었습니다.");
                break;
            }
        }
        System.out.println("영업을 종료하겠습니다.");
    }

}
