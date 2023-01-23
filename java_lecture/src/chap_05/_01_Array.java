package chap_05;

public class _01_Array {
    public static void main(String[] args) {
        // 배열 선언 방법
        // 첫번째
//        String[] coffees = new String[4];

        // 두번째
//        String coffees[] = new String[4];

//        coffees[0] = "아메리카노";
//        coffees[1] = "카페 모카";
//        coffees[2] = "라떼";
//        coffees[3] = "카푸치노";

        // 세번째
//        String[] coffees = new String[] {"아메리카노", "카페모카", "라떼", "카푸치노"};

        // 네번째
        String[] coffees = {"아메리카노", "카페모카", "라떼", "카푸치노"};
        coffees[2] = "에스프레소";
        for (int i = 0; i < 4; i++) {
            System.out.println(coffees[i] + "하나");
        }
        System.out.println("주세요");
    }
}
