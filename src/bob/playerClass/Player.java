package playerClass;

import java.util.Scanner;
import 

public class Player extends OVclass{

    public Player(int klass){
        super();
        if(klass == 1){
            this.name = "Mage";
            maxhp = 10;
            healthPoints = maxhp;
            streanght = 1;
            manapoint = 5;
        }else if(klass == 2){
            this.name = "Warrior";
            maxhp = 15;
            healthPoints = maxhp;
            streanght = 5;
        }else if(klass == 3){
            this.name = "Rouge";
            maxhp = 10;
            healthPoints = maxhp;
            streanght = 3;
            manapoint = 3;
        }else{
            System.out.println("error in klass chooser");
        }
    }

    public void PrintStats(){
        System.out.println("Class: " + this.name);
        System.out.println("Level: " + this.level);
        System.out.println("HP: " + this.healthPoints);
        System.out.println("Strenght: " + this.streanght);
        System.out.println("MP: " + this.manapoint);
        System.out.println("AG: " + this.agility);
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
}
