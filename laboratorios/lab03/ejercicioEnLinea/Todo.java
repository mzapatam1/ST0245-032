
import java.util.LinkedList;

public class Todo {

    public static String correct(String wrong) {
        boolean inicio=true;
        LinkedList<String> list=new LinkedList<>();
        String aux="";
        String rigth="";

       
        for(int i =0;i<wrong.length();i++){
            if((wrong.charAt(i)=='[') && inicio){
                list.addFirst(aux);
                aux="";

            } else if((wrong.charAt(i)=='[') && !inicio){
                list.addLast(aux);
                inicio=true;
                aux="";

            }else if((wrong.charAt(i)==']') && !inicio){
                list.addLast(aux);
                aux="";

            }else if((wrong.charAt(i)==']') && inicio){
                list.addLast(aux);
                inicio=false;
                aux="";

            }else{
                aux=aux+wrong.charAt(i);
            }

        }
        for(int i=0;i<list.size();i++){
            rigth=rigth+list.get(i);

        }
        return rigth;

    }

}
