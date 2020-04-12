
import java.util.*;

public class Semester
{

    public LinkedList<Subject> subjects = new LinkedList<>();

    public String number;

    public Semester(String number, Subject s){
        this.number = number;
        this.subjects.add(s);
    }

    public void printSubOfSem(String sub){
        for(Subject s: this.subjects){
            System.out.print(s.code + " " + "(" + s.grade + ")");
        }
    }

    public void addSub(Subject s){
        boolean p = true;
        for(Subject su: subjects){
            if(su.code.equals(s.code)){
                p = false;
            }
        }
        if(p) this.subjects.add(s);
    }

    
    public Subject getSub(String sub){
        for(Subject s: this.subjects){
            if(s.code.equals(sub)){ 
                return s;
            }
        }
        return null;
    }
}