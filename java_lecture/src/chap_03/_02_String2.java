package chap_03;

public class _02_String2 {
    public static void main(String[] args) {
        String s = "I Like Java and Python and C.";

        // 문자열 반환
        System.out.println(s.replace("and", ",")); // target을 replacement로 변환
        System.out.println(s.substring(7)); // 인덱스 기준 7부터 시작(이전내용 삭제)
        System.out.println(s.substring(s.indexOf("Java")));
        System.out.println(s.substring(s.indexOf("Java"), s.lastIndexOf("and")));

        //공백 제거
        s = "         I love Java.       ";
        System.out.println(s);
        System.out.println(s.trim()); // 앞뒤 공백 제거

        // 문자열 결합
        String s1 = "Java";
        String s2 = "Python";
        System.out.println(s1+s2);
        System.out.println(s1 + ", " + s2);
        System.out.println(s1.concat(", ").concat(s2));

    }
}
