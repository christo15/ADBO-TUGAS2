/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 
 */
public class User {
    private String name;
    private boolean computer;
    private int curIdx;

    public User(String name, boolean Computer) {
        this.name = name;
        this.computer = Computer;
        if(computer){
            this.name = "Comp";
        }
        this.curIdx =1;
    }

    public String getName() {
        return name;
    }

    public void setCurIdx(int curIdx) {
        this.curIdx = curIdx;
    }

    public int getCurIdx() {
        return curIdx;
    }

    public boolean isComputer() {
        return computer;
    }
    
}
