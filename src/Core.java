import playerClass.Player;
import utilities.util;
import playerClass.Player;

import java.util.Scanner;

public class Core {

    private Player player;
    private util utils = new util();

    //main game loop
    public void run(){
        //utils.intro();
        KlassChooser();
        player.PrintStats();
    }

    public void KlassChooser(){
        Scanner scanner = new Scanner(System.in);
        utils.Print("Choose a class");
        utils.Print("[1] Mage");
        utils.Print("[2] Warrior");
        utils.Print("[3] Rouge");
        int choice = scanner.nextInt();
        player = new Player(choice);
    }


    public static void main(String[] args){
        new Core().run();
    }
}
