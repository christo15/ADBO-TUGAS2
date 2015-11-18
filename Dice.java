public class Dice {
    private Random rnd = new Random();
    
    public int roll(){
        return rnd.nextInt(6)+1;
    }
    
}
