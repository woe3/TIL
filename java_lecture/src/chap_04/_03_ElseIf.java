package chap_04;

public class _03_ElseIf {
    public static void main(String[] args) {
        // 조건문 elseif

        boolean hanlabongAde = false;
        boolean mangoJuice = true;

        if (hanlabongAde) {
            System.out.println("한라봉 에이드 +1");
        } else if (mangoJuice) {
            System.out.println("망고 주스 +1");
        } else {
            System.out.println("아이스 아메리카노 +1");
        }
    }
}
