package chap_01;

public class _03_Varialbes {
    public static void main(String[] args) {
        String name = "김현우";
        int time = 15;

        System.out.println(name + "님, 안녕하세요 배송이 시작됩니다. "+ time +"시에 배송이 완료될 예정입니다.");
        System.out.println(name + "님, 배송이 완료되었습니다.");

        double score = 90.5;
        char grade = 'A';
        System.out.println(name + "님의 평균 점수는 "+ score +"점입니다.");
        System.out.println("학점은 "+ grade +"입니다.");

        boolean pass = true;
        System.out.println("이번 시험에 합격 했을까요? " + pass);

        double d = 3.123456789;
        float f = 3.123456789f;
        System.out.println(d);
        System.out.println(f);

        long l = 1234567890123l;
        l = 1_234_567_890_123l;
        System.out.println(l);
    }
}
