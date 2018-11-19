package playerClass;

public class OVclass {
    // Super Class for Player, subclasses are set in Player.java
    public String name = "blaha";
    public int level = 1;
    public int maxXp = (level * 3)^2;
    public int maxHp = 1;
    public int hp = maxHp;
    public int st = 1;
    public int mp = 0;
    public int ag = 1;
    public int xp = 0;
    public int score = 0;
    public int agXp;
    public int agMax;
    public int armorType = 0; //0=human-like skin

    public void heal(){
        hp = maxHp;
    }

    public void setXp(){
        maxXp = (level * 3)^2;
    }

    public void setAgXp(){
        agMax = (ag * 3)^1.1;
    }

}
