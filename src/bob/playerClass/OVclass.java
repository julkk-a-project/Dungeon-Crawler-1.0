package playerClass;

public class OVclass {
    // Super Class for Player, subclasses are set in Player.java
    public String name = "blaha";
    public int level = 1;
    public int maxxp = (level * 3)^2;
    public int maxhp = 1;
    public int healthPoints = maxhp;
    public int streanght = 1;
    public int manapoint = 0;
    public int agility = 1;
    public int xp = 0;
    public int score = 0;
    public int AgilityXP;
    public int AgilityMax;

    public void heal(){
        healthPoints = maxhp;
    }

    public void setXp(){
        maxxp = (level * 3)^2;
    }

    public void setAgXp(){
        AgilityMax = (agility * 3)^1;
    }

}
