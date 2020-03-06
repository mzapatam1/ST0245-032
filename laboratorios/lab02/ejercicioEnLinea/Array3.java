
/**
 * Write a description of class Array3 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Array3
{
    public boolean canBalance(int[] nums) {

        int sumap=nums[0];
        int sumaf=0;
        int i=0;
        boolean valor=false;
        if(nums.length>1){
            for(int j =1;j<nums.length;j++){
                sumaf=sumaf+nums[j];

            }
            while(i<nums.length-1){
                for(int j=i+1;j<nums.length;j++){
                    if(!(sumap==sumaf)){
                        sumap=sumap+nums[j];
                        sumaf=sumaf-nums[j];

                    }else
                    {valor=true;
                        break;
                    }

                }
                i++;

            }
            return valor;
        }
        else{
            return false;
        }

    }

    public int maxSpan(int[] nums) {
        int span = 0;
        int temp = 0;
        for(int i = 0; i<nums.length; i++){
            for(int j = nums.length; j>0; j--){
                if(nums[i]==nums[j-1]) temp = (j-i);
                span = Math.max(temp,span);
            }
        }
        return span;
    }

    public int[] fix34(int[] nums) 
    {
        int j = 1;
        for(int i = 0; i < nums.length - 1; i++)
        {
            if(nums[i] == 3 && nums[i+1] != 4)
            {
                for(; nums[j] != 4; j++);
                nums[j] = nums[i+1];
                nums[i+1] = 4;
            }
        }
        return nums;
    }

    public int[] fix45(int[] nums)
    {
        int j = 0;
        for(int i = 0; i < nums.length - 1; i++)
        {
            if(nums[i] == 4 && nums[i+1] != 5)
            {
                for(; !(nums[j] == 5 && (j == 0 || j > 0 && nums[j-1] != 4)); j++);
                nums[j] = nums[i+1];
                nums[i+1] = 5;
            }
        }
        return nums;
    }

    public int[] squareUp(int n)
    {
        int[] arr = new int[n*n];
        int p;
        for(int i = 1; i <= n; i++)
        {
            p = n * i - 1;
            for(int j = 1; j <= i; j++, p--)
                arr[p] = j;
        }
        return arr;
    }

}
