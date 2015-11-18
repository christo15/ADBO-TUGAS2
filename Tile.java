/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 
 */
public class Tile {
    private User[] user = new User[2];
    private int index;
    private UlarTangga ularTangga;

    public Tile(int index) {
        this.index = index;
        
    }

    public void setUser(User user) {
        if(this.user[0] == null){
            this.user[0] = user;
        }
        
        else if(this.user[0] != null){
            this.user[1] = user;
        }
    }

    public UlarTangga getUlarTangga() {
        return ularTangga;
    }

    public void setUlarTangga(UlarTangga ularTangga) {
        this.ularTangga = ularTangga;
    }

    public User getUser1() {
        return user[0];
    }
    public User getUser2() {
        return user[1];
    }
    
    public void removeUser(String str){
        if(user[0] != null){
            if(user[0].getName().equals(str)){
                    user[0]= null;
                };
        }
        else {
            if(user[1] != null){
                if(user[1].getName().equals(str)){
                    user[1]= null;
                };
            }
        }
    }

}
