
import java.util.Random;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author
 */
public class Board {

    private Tile[] tile;
    private User[] player;
    private Dice dice;
    private User playerTurn;
    private Random rnd;

    public Board(int pilihan) {
        tile = new Tile[101];
        dice = new Dice();
        rnd = new Random();
        for (int i = 1; i < 101; i++) {
            tile[i] = new Tile(i);
        }

        if (pilihan == 1) {
            player = new User[2];
            player[0] = new User("P1", false);
            player[1] = new User("P2", false);
        } else if (pilihan == 2) {
            player = new User[2];
            player[0] = new User("P1", false);
            player[1] = new User("Comp", true);
        }

        tile[1].setUser(player[0]);
        tile[1].setUser(player[1]);

        this.playerTurn = player[0];

        //Ular & Tangga
        for (int i = 0; i < 5; i++) {
            //Ular
            int idx = rnd.nextInt(96) + 2;
            int idxTo = rnd.nextInt(idx - 2);
            if (tile[idx].getUlarTangga() == null) {
                tile[idx].setUlarTangga(new UlarTangga(idxTo));
            }

            //Tangga
            int idx2 = rnd.nextInt(96) + 2;
            int idxTo2 = rnd.nextInt(98 - idx2) + idx2;
            if (tile[idx2].getUlarTangga() == null) {
                tile[idx2].setUlarTangga(new UlarTangga(idxTo2));
            }
        }
    }

    public void Run(int x) {
        if (x == 1) {
            int temp = playerTurn.getCurIdx() + dice.roll();
            if (temp <= 100) {
                temp = this.checkAndChange(temp);
                tile[playerTurn.getCurIdx()].removeUser(playerTurn.getName());
                tile[temp].setUser(playerTurn);
                playerTurn.setCurIdx(temp);
            } else {
                tile[playerTurn.getCurIdx()].removeUser(playerTurn.getName());
                temp -= 100;
                temp = 100 - temp;
                temp = this.checkAndChange(temp);
                tile[temp].setUser(playerTurn);
                playerTurn.setCurIdx(temp);
            }
        } else {
            System.exit(0);
        }
        this.changeTurn();
        
    }

    private int checkAndChange(int temp) {
        if (tile[temp].getUlarTangga() != null) {
            return tile[temp].getUlarTangga().getToIndex();
        }
        return temp;
    }

    public void changeTurn() {
        if (playerTurn == player[0]) {
            this.playerTurn = player[1];
        } else if (playerTurn == player[1]) {
            this.playerTurn = player[0];
        }
    }

    public void printMap() {
        for (int i = 1; i <= 100; i++) {
            if (i < 10) {
                System.out.print(i + "  ");
            } else if (i >= 10) {
                System.out.print(i + " ");
            } else if (i == 100) {
                System.out.print(i + "");
            }

            if (tile[i].getUser1() == null && tile[i].getUser2() == null) {
                System.out.print("   -  ");
            } else {
                if (tile[i].getUser1() != null) {

                    System.out.print(tile[i].getUser1().getName() + " ");
                }
                if (tile[i].getUser2() != null) {
                    System.out.print(tile[i].getUser2().getName() + " ");

                }
            }

            if (tile[i].getUlarTangga() != null) {
                if (i < 10) {
                    System.out.print(tile[i].getUlarTangga().getToIndex() + "   ");
                } else if (i > 9) {
                    System.out.print(tile[i].getUlarTangga().getToIndex() + " ");
                }
            } else if (tile[i].getUlarTangga() == null) {
                System.out.print("   ");
            }

            if (i % 5 == 0) {
                System.out.println("");
            }
        }
    }

    public User[] getPlayer() {
        return player;
    }

    public User getPlayerTurn() {
        return playerTurn;
    }

    public boolean isWin() {
        if (player[0].getCurIdx() == 100 || player[1].getCurIdx() == 100) {
            if (player[0].getCurIdx() == 100) {
                System.out.println(player[0].getName() + " is The Winner");
            } else {
                System.out.println(player[1].getName() + " is The Winner");
            }
            System.out.print("=================================CONGRATULATION!!!==================================");
            return true;
        }
        return false;
    }
}
