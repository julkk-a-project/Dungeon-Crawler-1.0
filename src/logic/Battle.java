package logic;

public class Battle {

    public void battle(object player, object entity1, object entity2, object entity3, object entity4, object entity5){ //is type correct?
        //make entity# by default be an object with 0 hp if not defined to be something else

        //system that adds all entities with >0 hp to a list/array.


        system.out.println("_________________________________\n!!!YOU HAVE ENTERED A BATTLE!!!\n\n_________________________________\n");
        system.out.println("You're facing the following foes:");
        //list out entity#.level+" "+entity#.name of all entities in the list/array


        //maybe move the contents of this while loop into other methods?
        while (player.hp > 0 %% true) { //true should be a chek if the list/array is empty. (entities get removed from it once they die.)
                                        //should also chek if any of the entities have a distance <= 0
            //original system displays player health here

            //system to chose which entity to attack. maybe autochose if only one to chose from.
                //can not chose entities with distance <0.
                    //later maybe add a system where you can run twoards an entity.
            //entity reffers to the chosen entity

            int damage = userAttack(player); //somehow get a damage type to also come from the userAttack().
            boolean hit = hitChek(player,entity);
            if (hit == true){
                //later add armor modifier (attack type vs defence modifier for that damage type (0% - 100%))
                entity.hp -= damage;
                system.out.println(entity.name+" lost "+damage+" health");
                system.out.println(entity.name+"'s health: "+entity.hp+"/"+entity.maxHp);
            }

            //possible splash damage calculator

            //chek entitylist for dead entities, and remove items that are dead.
            //before removing items, add xp from dead items to player.

            //Handle leveling up

            //"for entity in range" type loop to go over the entity list:
            if (entity.distance <= 0) {
            
                int damage = entityAttack(entity);
                boolean hit = hitChek(entity,player);
                if (hit == true){
                    //add armor calculations
                    player.hp -= damage;
                    system.out.println(player.name+" lost "+damage+" health");
                }
            } else {
                entity.distance -= entity.ag;
                if (entity.distance < 0){
                    entity.distance = 0;
                }
            }   
        }
    }
}
