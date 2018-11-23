import bob.enteties.Goblin;
import bob.location.Cave;
import bob.logic.Battle;
import bob.playerClass.Player;
import bob.utilities.Util;
import bob.gui.Gui;
import java.util.Scanner;

public class Core {

    private Player player;
    private Battle battle = new Battle();
    private Util use = new Util();
    boolean[][] location = new boolean[5][5];
    int arskaTownAgro = 0;

    //main game loop
    public void run(){
        while(player.hp > 0){
            if(location[0][0]){
                use.Print("You see a cave, Do you want to explore?\n [1]Yes\n [2]No");
                int temp = use.ChoiseSelectorInt();
                if(temp == 1){
                    new Cave().welcomeMessage();
                    battle.encounter(player,new Goblin());
                    use.Print("Do you want to turn over more rocks?\n [1]Yes\n [2]No");
                    int cuntinue = use.ChoiseSelectorInt();
                    while (cuntinue == 1){
                        battle.encounter(player,new Goblin());
                        use.Print("Do you want to turn over more rocks?\n [1]Yes\n [2]No");
                        cuntinue = use.ChoiseSelectorInt();
                    }
                }else if(temp == 2){
                    location[0][0] = false;
                    location[0][1] = true;
                    use.Print("This location is yet not impemented");
                }
            }else if(location[0][1]){
                use.Print("This location is yet not impemented");
                location[0][0] = true;
            }else{
                use.Print("For debug purpuses, you will return to cave location");
                location[0][0] = true;
            }
        }
    }

    public void init(){
        use.ScreenClearer();
        //utils.intro();
        KlassChooser();
        player.PrintStats();
        location[0][0] = true;
        use.sleeper();
        use.ScreenClearer();
        run();
    }

    public void KlassChooser(){
        Scanner scanner = new Scanner(System.in);
        use.Print("Choose a class");
        use.Print("[1] Mage");
        use.Print("[2] Warrior");
        use.Print("[3] Rouge");
        int choice = scanner.nextInt();
        player = new Player(choice);
    }


    public static void main(String[] args){
        //new Core().init();
        new Gui().run();
    }
}
