package chap_04;

public class _06_While {
    public static void main(String[] args) {
        // 반복문 while
        int distance = 25; // 전체 거리
        int move = 0; // 현재까지 움직인 거리
        while (move < distance) {
            System.out.println("이동합니다");
            System.out.println("현재 위치 : " + move);
            move += 3;
        }
        System.out.println("도착하였습니다.");

        // 무한 루프
    }
}
