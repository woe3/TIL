package chap_03;

public class _01_String1 {
    public static void main(String[] args) {
        String s = "I Like Java and Python and C.";
        System.out.println(s);

        // 문자열의 길이
        System.out.println(s.length());

        // 대소문자 변환
        System.out.println(s.toUpperCase());
        System.out.println(s.toLowerCase());

        // 포함 관계
        System.out.println(s.contains("Java"));
        System.out.println(s.contains("cpp"));

        // 위치 정보
        System.out.println(s.indexOf("Python"));
        System.out.println(s.indexOf("cpp"));
        System.out.println(s.indexOf("and")); // 처음 만나는 위치
        System.out.println(s.lastIndexOf("and")); // 마지막으로 만나는 위치
        System.out.println(s.startsWith("I Like")); // 처음으로 시작하는 문자열
        System.out.println(s.endsWith("C.")); // 마지막으로 끝나느 문자열
        
    }
}
