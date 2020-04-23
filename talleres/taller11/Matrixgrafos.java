
import java.util.*;

public class Matrixgrafos
{
    public int MatrixAdj[][];
    public int numVertices;
    
    
    
    public Matrixgrafos (int size) {
        numVertices = size;
        MatrixAdj = new int [numVertices][numVertices];
    }

    public void addEdge (int size, int next, int weight){
        MatrixAdj [size][next] = weight;
    }

    public void removeEdge (int size, int next){
        MatrixAdj [size][next] = 0;
    }

    public boolean areConnected (int size, int next){
        if (MatrixAdj [size][next] !=0)
            return true;
        else
            return false;
    }

    public int getWeight (int size, int next){
        if (areConnected (size,next))
            return MatrixAdj [size][next];
        else 
            return 0;
    }

    public LinkedList<Integer> getSuccessors(int vertex){
        LinkedList<Integer> s = new LinkedList <Integer>();
        for (int i = 0; i< numVertices; i++){
            if (MatrixAdj [vertex][i] !=0)
                s.add(i);
        }
        return s;
    }
}