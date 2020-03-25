
/**
 * Write a description of class Punto1 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
import java.io.*;
import java.util.*;
public class Punto1
{
   public static int Pila(String caracteres){
    String[] caracter=caracteres.split(" ");
    Stack<Integer> fenteros= new Stack<>();
    
    for(int i=0;i<caracter.length;i++){
    if(caracter[i].equals("+")){
    
    fenteros.push(fenteros.pop()+fenteros.pop());
   
    }else if(caracter[i].equals("-")){
    
    fenteros.push(fenteros.pop()-fenteros.pop());
   
    }else if(caracter[i].equals("*")){
    
    fenteros.push(fenteros.pop()*fenteros.pop());
   
    }else if(caracter[i].equals("/")){
    
    fenteros.push(fenteros.pop()/fenteros.pop());
   
    }else{
    fenteros.push(Integer.parseInt(caracter[i]));
    }
    
    
    }
     return fenteros.pop();
    
    
    }
}
