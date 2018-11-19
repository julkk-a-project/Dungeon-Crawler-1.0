package playerClass;

import java.util.Scanner;
import 

public class Player extends OVclass{

    public Player(int klass){
        super();
        if(klass == 1){
            this.name = "Mage";
            maxHp = 10;
            hp = maxHp;
            st = 1;
            mp = 5;
        }else if(klass == 2){
            this.name = "Warrior";
            maxHp = 15;
            hp = maxHp;
            st = 5;
        }else if(klass == 3){
            this.name = "Rouge";
            maxHp = 10;
            hp = maxHp;
            st = 3;
            mp = 3;
        }else{
            System.out.println("error in klass chooser");
        }
    }

    public void PrintStats(){
        System.out.println("Class: " + this.name);
        System.out.println("Level: " + this.level);
        System.out.println("HP: " + this.hp +"/"+ this.maxHp);
        System.out.println("ST: " + this.st);
        System.out.println("MP: " + this.mp);
        System.out.println("AG: " + this.ag);
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
