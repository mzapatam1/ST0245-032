
/**
 * Write a description of class MiArrayList here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyArrayList
{  int t;
   char [] elementos;
   final int capacidad = 10;
    public MyArrayList(){
        t = 0;
        elementos = new char[capacidad];
    }

    public char[] insertar(char x, int index) throws IndexOutOfBoundsException{
        if(index>elementos.length) duplicate();
        char aux = elementos[index];
        elementos[index] = x;
        for(int i = index+1;i<elementos.length-1;i++){
            elementos[i] = aux;
            aux = elementos[i+1];
        }
        t += 1;
        return elementos;
    }

    public char[] insertar(char x){
        if(t==elementos.length) duplicate();
        elementos[t] = x;
        t+=1;
        return elementos;
    }

    private char [] duplicate(){
        char [] arr = new char[2*elementos.length];
        for(int i = 0;i<elementos.length;i++){
            arr[i]=elementos[i];
        }
        return arr;
    }

    public char get(int i){
        if (i>t) return 0;
        return elementos[i];
    }

    public char[] remover(int index){
        char aux = elementos[index+1];
        for(int i = index;i<t-1;i++){
            elementos[i] = aux;
        }
        if(elementos[t-2]==elementos[t-1]) elementos[t-1]  = '\u0000';
        t -= 1;
        return elementos;
    }

    public boolean contains(char x){
        for(int i =0;i<elementos.length;i++){
            if(elementos[i]==x) return true;
            break;
        }
        return false;
    }

}
