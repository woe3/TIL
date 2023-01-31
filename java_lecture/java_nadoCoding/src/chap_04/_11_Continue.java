package chap_04;

public class _11_Continue {
    public static void main(String[] args) {
        // continue

        // 손님 중에 노쇼가 있다면
        int max = 20; //최대 치킨 판매 수량
        int sold = 0; // 현재 치킨 판매수량
        int noShow = 17; // 노쇼한 손님 번호
        for (int i = 1; i < 50; i++) {
            System.out.println(i + "번 손님, 주문하신 음식 나왔습니다.");
            if (i == noShow) {
                System.out.println(i + "번 손님이 안계셔서 다음 손님에게 드리겠습니다.");
                continue;
            }
            sold++;
            if (sold == max) {
                System.out.println("재료가 모두 소진되었습니다.");
                break;
            }
        }
        System.out.println("영업을 종료하겠습니다.");
    }
}
