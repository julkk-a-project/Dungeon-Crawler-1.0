package bob.logic;

import bob.enteties.Entity;
import bob.playerClass.Player;
import bob.utilities.Util;

public class Battle {

    private Util use = new Util();

    public void encounter(Entity ent){
        use.ScreenClearer();
        use.Print("You encounterd a: " + ent.name);
        ent.taunt();
    }

    public void battle(Player player, Entity ent){
        Entity[] entityList = new Entity[1];
        entityList[0] = ent;
        while(player.hp > 0 && entityList[0].hp > 0){
            use.Print("which attack do you wish to chose?\n(1)Slash\n(2)Fireball\n(3)Nether");
            if(use.ChoiseSelectorInt() == 1){
                //slash
                use.Print("You use SLASH!");
                int playerhit = agCheck(player,ent);
                if(playerhit == 1){
                    use.Print("Hit!");
                    ent.hp -= player.st;
                }else{
                    use.Print("Miss!");
                    use.Print(ent.name + "has" + ent.hp + "/" + ent.maxHp + "health" + "\n");
                }

            }else if(use.ChoiseSelectorInt() == 2) {
                //Fireball
                use.Print("You use Fireball!");
                int playerhit = agCheck(player,ent);
                if(playerhit == 1){
                    use.Print("Hit!");
                    ent.hp -= player.mp;
                }else{
                    use.Print("Miss!");
                    use.Print(ent.name + "has" + ent.hp + "/" + ent.maxHp + "health" + "\n");
                }

            }else if(use.ChoiseSelectorInt() == 3){
                //RUN!
                int escape = coward(player, ent);
                if(escape == 1){
                    break;
                }

            }else{
                use.Print("If you can read this, you encountered a error in the battle system");
            }
        }
    }

    public int agCheck(Player player, Entity ent){
        return 1;
    }

    public int coward(Player player, Entity ent){
        return 1;
    }
}