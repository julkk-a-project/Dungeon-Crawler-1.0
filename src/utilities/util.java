package utilities;

public class util {

    public void intro(){
        int startimes = 2;
        for(int i = 0; i < 1;i++){
            String[] defaultLine = {"***********","***********", "*** D C ***", "*** 1.0 ***", "***********", "***********"};
            String[] dottedLine = {"...........", "...........", "... D C ...","... 1.0 ...", "...........", "..........."};
            int[] reversed = {5, 4, 3, 2, 1, 0};
            for(int j = 0;j < 6;j++){
                for(int x = 0;x < dottedLine.length;x++){
                    if(x == reversed[j]){
                        System.out.println(dottedLine[0]);
                        System.out.println(dottedLine[1]);
                        System.out.println(dottedLine[2]);
                        System.out.println(dottedLine[3]);
                        System.out.println(dottedLine[4]);
                        System.out.println(dottedLine[5]);
                    }else{
                        System.out.println(defaultLine[0]);
                        System.out.println(defaultLine[1]);
                        System.out.println(defaultLine[2]);
                        System.out.println(defaultLine[3]);
                        System.out.println(defaultLine[4]);
                        System.out.println(defaultLine[5]);
                    }
                }
                //TODO: fix intro so it looks "animated"
                /*try{
                    Runtime.getRuntime().exec("clear");
                }catch (IOException e){
                    e.printStackTrace();
                }*/
            }
        }
    }

    public void Print(String string){
        System.out.println(string);
    }
}
