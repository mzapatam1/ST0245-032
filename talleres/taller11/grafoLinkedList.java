import java.io.*;
import javafx.util.Pair; 
import java.util.*;
public class grafoLinkedList
{
    public LinkedList <Pair <Integer, Integer>> [] grafo;
    public int numVertices;

    public grafoLinkedList (int size) {
        numVertices = size;
        grafo = new LinkedList [numVertices];
    }

    public void addEdge (int size, int next, int weight){
        grafo[size].add(new Pair(next,weight)) ; 
    }

    public boolean areConnected (int size, int next){
        for (int i = 0; i<= grafo[size].size(); i++){
            int c = grafo[size].get(i).getKey();
            if (c==next){
                return true;
            }
        }
        return false;
    }

    public int getWeight (int size, int next){
        for (int i = 0; i<= grafo[size].size(); i++){
            int c = grafo[size].get(i).getKey();
            if (c==next){
                return grafo[size].get(i).getValue();
            }
        }
        return 0;
    }
    
    public LinkedList<Integer> getSuccessors(int vertex){
        LinkedList<Integer> s = new LinkedList <Integer>();
        for (int i = 0; i< numVertices; i++){
            if (getWeight(vertex, i) !=0)
                s.add(i);
        }
        return s;
    }
}