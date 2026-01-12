import java.util.Scanner;

public class Lembrando {
    public static void main(String[] args) {
        System.out.println("hello world");
        System.out.println(1+1);
        System.out.println("int");

        double pi = 3.14;
        int raio = 5;
        double area = pi * raio * raio;
        System.out.println("A área do círculo é: " + area);

        Scanner scanner = new Scanner(System.in);
        scanner.nextLine();
        System.out.print("Digite algo: ");
        String variavel = scanner.nextLine();
        System.out.println("Você digitou: " + variavel);
    }
}