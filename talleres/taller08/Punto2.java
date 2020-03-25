
/**
 * Write a description of class Punto2 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
import java.io.*;
import java.util.*;

public class Punto2
{
    public static Stack<Integer> inversa (Stack <Integer >stack){
        int n = stack.size();
        Stack<Integer> temp = new Stack<Integer>();
        for(int i = 0; i < n; i++) 
            temp.push (stack.pop());
        return temp;
    }
      public static void cola(Queue<String> queue){
        while (!queue.isEmpty())    
            System.out.println("Atendiendo a " + queue.remove());
    }
    
}
