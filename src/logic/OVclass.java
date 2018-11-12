package logic;

public class OVclass {

    public String name;
    public int level = 1;
    public int maxxp = (level * 3)^2;
    public int maxhp = 1;
    public int healthPoints = maxhp;
    public int streanght = 1;
    public int manapoint = 0;
    public int agility = 1;
    public int xp = 0;
    public int score = 0;

    public void heal(){
        healthPoints = maxhp;
    }

    public void setXp(){
        maxxp = (level * 3)^2;
    }

}
