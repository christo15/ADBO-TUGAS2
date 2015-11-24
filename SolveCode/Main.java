
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author 
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("==========ular tangga===========");
        System.out.println("1. Player vs Player");
        System.out.println("2. Computer vs Player");

        int pilihan = sc.nextInt();
        Board board = new Board(pilihan);
        board.printMap();
     

        while (!board.isWin()) {
            if (!board.getPlayerTurn().isComputer()) {
                User turn = board.getPlayerTurn();
                System.out.println("=========== " + turn.getName() + " Turns Now============");
                System.out.println("1. ROLL?");
                System.out.println("2. EXIT?");
                board.Run(sc.nextInt());
            } else {
                System.out.println("=========== COMPUTER'S Turns Now============");
                board.Run(1);
            }
            board.printMap();
        }
        
    }
}
