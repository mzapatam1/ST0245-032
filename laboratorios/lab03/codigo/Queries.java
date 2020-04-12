
import java.util.*;
import java.io.*;

public class Queries 
{
    
    LinkedList<Student> students = new LinkedList<>();
    
    Subject sub;
   
    Semester sem;
    
    Semester aux; 
    
   
    public void read(String archive){
        try{
            Scanner reader = new Scanner(new File(archive));
            String titles = reader.nextLine();
            while(reader.hasNextLine()){
                reader.nextLine();
                String line = reader.nextLine(); 
                String [] data = line.split(",");
                if(!isStu(data[1])){
                    if(data.length == 15){
                        sub = new Subject(data[2], data[14]);
                    }else{
                        sub = new Subject(data[2], data[13]);
                    }
                    sem = new Semester(data[3],sub);
                    Student s = new Student(data[0],data[1],sem);
                    students.add(s); 
                }else{
                    Student a = searchStud(data[1]);
                   if(searchSem(a, data[3])){
                       aux = isSem(a, data[3]);
                       createSub(data,1);
                   }else{
                       createSub(data,2);
                       sem = new Semester(data[3],sub);
                       a.addSem(sem);
                    }
                }
            }
        }catch(Exception e){
            System.out.println("Your archive couldn't be read");
        }
    }
  
    
    private void createSub(String [] data, int cases){
        if(cases==1){
            if(!searchSub(data[2],aux)){
                if(data.length == 15){
                    sub = new Subject(data[2], data[14]);
                    aux.addSub(sub);
                }else{
                    sub = new Subject(data[2], data[13]);
                    aux.addSub(sub);
                }
            }
        }else{
            if(data.length == 15){
                    sub = new Subject(data[2], data[14]);
                }else{
                    sub = new Subject(data[2], data[13]);
                }            
        }
    }
    
   
    public Student searchStud(String code){
        for(Student s: students){
            if(s.stuCode.equals(code)){ 
                return s;
            }
        }
        return null;
    }
     
    
    private boolean searchSub(String subCode, Semester s){
        for(Subject sub: s.subjects){
            if(sub.code.equals(subCode)){
                return true;
            }
        }
        return false;  
    }
     

    private boolean isStu(String code){
        for(Student s: students){
            if(s.stuCode.equals(code)){ 
                return true;
            }
        }
        return false;
    }
    
   
    private boolean searchSem(Student a, String num){
        for(Semester s: a.semesters){
            if(s.number.equals(num)){ 
                return true;
            }
        }
        return false;
    }
    
   
    private Semester isSem(Student a, String sem){
        for(Semester s: a.semesters){
            if(s.number.equals(sem)){ 
                return s;
            }
        }
        return null;
    }
    
    
    private void printStuOfSub(String subj, String sem){
        try{
            for(Student s: students){
                for(Semester seme: s.semesters){ 
                    if(seme.number.equals(sem) && seme.getSub(subj) !=null){
                        System.out.println(s.name + " " + seme.getSub(subj).grade);                     
                    }
                }
            }
        }catch(Exception e){
            System.out.println("There's not students at that semester");
        }
    }
    
    
    private void SubSem(Student a, String sem){
        try{ 
            System.out.print(a.name + " "); 
            for(Semester s: a.semesters){
                if(s.number.equals(sem)){
                    s.printSubOfSem(sem); 
                }
            }
        }catch(Exception e){
            System.out.println("This student doesn't exist");
        }
    }
    
    
    private void readArchives(){
        read("NOTAS ST0242.csv");
        read("NOTAS ST0245.csv");
        read("NOTAS ST0247.csv");
    }

   
    public void query1(){
        readArchives();
        Scanner data = new Scanner(System.in);
        System.out.println("Write the subject code in uppercase");
        String Scode = data.next();
        System.out.println("Write the semester without hyphen");
        String semester = data.next();
        System.out.println(Scode + "-" + "Final Grade");
        printStuOfSub(Scode, semester);
    }
    
       
    public void query2(){
        readArchives();
        Scanner data = new Scanner(System.in);
        System.out.println("Write the student code");
        String stu = data.next();
        Student a = searchStud(stu);
        System.out.println("Write the semester without hyphen");
        String semester = data.next();
        System.out.println(semester);
        SubSem(a, semester); 
    }
}