import java.util.Scanner;

public class emailvalid{
    public static boolean checkmail(String email){
        String email_condition = "^[a-zA-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[a-zA-Z0-9.-]+$";
        return email.matches(email_condition);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the email address");
        String email = sc.next();
        System.out.println("Your entered email is:");
        System.out.println("Is email is valid:"+checkmail(email));
    }
}