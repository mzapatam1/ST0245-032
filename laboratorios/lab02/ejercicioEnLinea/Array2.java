
/**
 * Write a description of class Array2 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Array2
{
    public int countEvens(int[] nums) {
        int contador=0;
        for(int i=0; i<+nums.length;i++){
            if(nums[i]%2==0){
                contador++;

            }

        }
        return contador;
    }

    public int bigDiff(int[] nums) {
        int mayor=0;
        int menor=nums[0];
        for(int i=0;i<nums.length;i++){

            if(nums[i]>mayor){
                mayor=nums[i];
            }
            else if(menor>nums[i])
                menor=nums[i];

        }
        return mayor-menor;
    }

    public int sum13(int[] nums) {
        int suma=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==13){
                i=i+1;
            }else{
                suma=suma+nums[i];

            }

    
        }
        return suma;
    }

    public boolean sum28(int[] nums) {
        int contador=0;
        for(int i=0;i<nums.length;i++){

            if(nums[i]==2){
                contador+=nums[i];
            }

        }
        if(contador==8){
            return true;
        }else{
            return false;
        }
    }

    public boolean more14(int[] nums) {
        int contador1=0;
        int contador4=0;
        for(int i=0;i<nums.length;i++){

            if(nums[i]==1){
                contador1++;
            }else if(nums[i]==4){ contador4++;}

        }
        return contador1>contador4;

    }

}
