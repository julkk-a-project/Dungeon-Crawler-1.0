import bob.playerClass.Player;
import bob.utilities.Util;

import java.util.Scanner;

public class Core {

    private Player player;
    private Util use = new Util();
    boolean[][] location = new boolean[5][5];
    int arskaTownAgro = 0;

    //main game loop
    public void run(){
    	use.ScreenClearer();
        //utils.intro();
        KlassChooser();
        player.PrintStats();
        location[0][0] = true;
        use.sleeper();
        use.ScreenClearer();
        while(player.hp > 0){
            if(location[0][0]){
                use.Print("You see a cave, Do you want to explore?\n [1]Yes\n [2]No");
                if(use.ChoiseSelectorInt() == 1){
                    //enter cave
                    break;
                }else if(use.ChoiseSelectorInt() == 2){
                    //don't
                }
            }
        }
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
        new Core().run();
    }
}
