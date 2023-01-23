package chap_04;

public class _07_DoWhile {
    public static void main(String[] args) {
        // 반복문 do while
        int distance = 25; // 전체 거리
        int move = 0; // 현재 위치
        int height = 2; // 키
        while (move + height < distance) {
            System.out.println("이동합니다");
            System.out.println("현재 위치 : " + move);
            move += 3;
        }
        System.out.println("도착하였습니다.");
        System.out.println("-----------------------");
        // do while
        move = 0;
        height = 25;
        do {
            System.out.println("이동합니다");
            System.out.println("현재 위치 : " + move);
            move += 3;
        }
        while (move + height < distance);
        System.out.println("도착하였습니다.");
    }
}
