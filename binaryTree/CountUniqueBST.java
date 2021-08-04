package binaryTree;


/*
https://leetcode.com/problems/unique-binary-search-trees/
*/


public class CountUniqueBST {
     public static int numTrees(int n) {
        if(n == 0){
            return 0;
        }
        int[] values = fillValues(n+1);
        return 0;
    }
    
    public static int[] fillValues(int m){
        System.out.println(" fillValues m = "+m);
        int[] values = new int[m];
        if(m == 0){
            return values;
        }
        values[0] = 1;// dummy
        values[1] = 1;

        int k;
        int j;
        int sum;
        if(m>1){
            for(int i=2;i<m;i++){
                System.out.println("i = "+ i);
                sum = 0;
                j = 0;
                k = i-j-1;
                while(j<=k){
                    
                    System.out.println(" j = "+j + " k = "+ k);
                    System.out.println(" values[j] = "+values[j]+" values[k] = "+values[k]);
                    if(j==k){
                        sum += values[j]*values[k];
                    }else{
                        sum += 2 * values[j] * values[k];
                    }
                    
                    System.out.println(" sum = "+ sum);
                    k-=1;
                    j+=1;
                }
                values[i] = sum;
            }
        }
        for(int i=0;i<m;i++){
             System.out.print(values[i]+" ");
        }
        System.out.println();
        return values;
    }

    public static void main(String args[]) {
        
        //System.out.println("result = "+numTrees(2));
         System.out.println("result = "+numTrees(5));
       //  System.out.println("result = "+numTrees(4));
    }
}