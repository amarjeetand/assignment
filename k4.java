
// Java program to generate Worst Case of Merge Sort 
  
import java.util.Arrays; 
  
class GFG  
{ 
    // Function to join left and right subarray 
    static void join(int arr[], int left[], int right[], 
                    int l, int m, int r) 
    { 
        int i; 
        for (i = 0; i <= m - l; i++) 
            arr[i] = left[i]; 
   
        for (int j = 0; j < r - m; j++) 
            arr[i + j] = right[j]; 
    } 
   
    // Function to store alternate elemets in left 
    // and right subarray 
    static void split(int arr[], int left[], int right[], 
                     int l, int m, int r) 
    { 
        for (int i = 0; i <= m - l; i++) 
            left[i] = arr[i * 2]; 
   
        for (int i = 0; i < r - m; i++) 
            right[i] = arr[i * 2 + 1]; 
    } 
      
    // Function to generate Worst Case of Merge Sort 
    static void generateWorstCase(int arr[], int l, int r) 
    { 
        if (l < r) 
        { 
            int m = l + (r - l) / 2; 
   
            // create two auxiliary arrays 
            int[] left = new int[m - l + 1]; 
            int[] right = new int[r - m]; 
   
            // Store alternate array elements in left 
            // and right subarray 
            split(arr, left, right, l, m, r); 
   
            // Recurse first and second halves 
            generateWorstCase(left, l, m); 
            generateWorstCase(right, m + 1, r); 
   
            // join left and right subarray 
            join(arr, left, right, l, m, r); 
        } 
    } 
      
    // driver program 
    public static void main (String[] args)  
    { 
        // sorted array 
        int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 
                      10, 11, 12, 13, 14, 15, 16 }; 
        int n = arr.length; 
        System.out.println("Sorted array is"); 
        System.out.println(Arrays.toString(arr)); 
          
        // generate Worst Case of Merge Sort 
        generateWorstCase(arr, 0, n - 1); 
   
        System.out.println("\nInput array that will result in \n"+ 
             "worst case of merge sort is \n"); 
      
        System.out.println(Arrays.toString(arr)); 
    } 
} 
  
// Contributed by Pramod Kumar 