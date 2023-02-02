package chapter_05.classpart;

public class Student {

    int studentID;
    String studentName;
    int grade;
    String address;

    public void showStudentInfo() {
        System.out.println(studentName + ", " + address);
    }
}
