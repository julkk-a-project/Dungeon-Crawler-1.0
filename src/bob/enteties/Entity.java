package enteties;

public class Entity {
    public String name;
    public int level = 1;
    public int maxXp = (level * 3)^2;
    public int maxHp = 1;
    public int hp = maxhp;
    public int st = 1;
    public int mp = 0;
    public int ag = 1;
    public int xp = maxhp + st + mp + ag;
    public int agXp = 0; //just to prevent errors
    public int distance = 0; //used if player tries to run away
    public int armorType = 0; //0=human-like skin

    public void taunt(){
        System.out.println("Taunt");
        //sleep(2)
        try {
            Thread.sleep(2000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
    }
    public void fixHealth(){
        hp = maxHp;
    }

}
