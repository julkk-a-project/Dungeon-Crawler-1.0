package bob.gui;

import java.awt.*;

import javax.swing.*;

public class Gui {

    static GraphicsConfiguration gc;
    private JPanel Gamepanel;

    public void run(){
        JFrame JF = new JFrame(gc);
        JF.setTitle("Dungeon Crawler");
        JF.setSize(800,600);
        JF.setLocation(200,200);
        Gamepanel = new JPanel();
        Gamepanel.setLayout(new FlowLayout());
        JF.add(Gamepanel);
        JTextArea textArea = new JTextArea("blaha blaha",40,60);
        JScrollPane scrollBar = new JScrollPane(textArea);
        Gamepanel.add(scrollBar);
        JF.setVisible(true);

    }
}
