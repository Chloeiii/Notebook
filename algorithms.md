### Table of Contents
- [Quick Mort](#quicksort)
- [Merge Sort](#mergesort)
- [A*]()
- [Binary Search]()
- [Trees]()
- [BFS](#bfs)
- [DFS](#dfs)
----
### QuickSort

Worst case: O(n^2)
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.
![](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png)

Ex: 

    // Java program for implementation of QuickSort 
    class QuickSort 
    { 
        /* This function takes last element as pivot, 
        places the pivot element at its correct 
        position in sorted array, and places all 
        smaller (smaller than pivot) to left of 
        pivot and all greater elements to right 
        of pivot */
        int partition(int arr[], int low, int high) 
        { 
            int pivot = arr[high]; 
            int i = (low-1); // index of smaller element 
            for (int j=low; j<high; j++) 
            { 
                // If current element is smaller than or 
                // equal to pivot 
                if (arr[j] <= pivot) 
                { 
                    i++; 

                    // swap arr[i] and arr[j] 
                    int temp = arr[i]; 
                    arr[i] = arr[j]; 
                    arr[j] = temp; 
                } 
            } 

            // swap arr[i+1] and arr[high] (or pivot) 
            int temp = arr[i+1]; 
            arr[i+1] = arr[high]; 
            arr[high] = temp; 

            return i+1; 
        } 


        /* The main function that implements QuickSort() 
        arr[] --> Array to be sorted, 
        low --> Starting index, 
        high --> Ending index */
        void sort(int arr[], int low, int high) 
        { 
            if (low < high) 
            { 
                /* pi is partitioning index, arr[pi] is 
                now at right place */
                int pi = partition(arr, low, high); 

                // Recursively sort elements before 
                // partition and after partition 
                sort(arr, low, pi-1); 
                sort(arr, pi+1, high); 
            } 
        } 
    } 

----
### MergeSort

Worst case: O(n^2)

    MergeSort(arr[], l,  r)
    If r > l
         1. Find the middle point to divide the array into two halves:  
                 middle m = (l+r)/2
         2. Call mergeSort for first half:   
                 Call mergeSort(arr, l, m)
         3. Call mergeSort for second half:
                 Call mergeSort(arr, m+1, r)
         4. Merge the two halves sorted in step 2 and 3:
                 Call merge(arr, l, m, r)

<img src = "https://www.geeksforgeeks.org/wp-content/uploads/Merge-Sort-Tutorial.png" width = 500>

Ex:

    /* Java program for Merge Sort */
    class MergeSort 
    { 
        // Merges two subarrays of arr[]. 
        // First subarray is arr[l..m] 
        // Second subarray is arr[m+1..r] 
        void merge(int arr[], int l, int m, int r) 
        { 
            // Find sizes of two subarrays to be merged 
            int n1 = m - l + 1; 
            int n2 = r - m; 

            /* Create temp arrays */
            int L[] = new int [n1]; 
            int R[] = new int [n2]; 

            /*Copy data to temp arrays*/
            for (int i=0; i<n1; ++i) 
                L[i] = arr[l + i]; 
            for (int j=0; j<n2; ++j) 
                R[j] = arr[m + 1+ j]; 


            /* Merge the temp arrays */
            // Initial indexes of first and second subarrays 
            int i = 0, j = 0; 

            // Initial index of merged subarry array 
            int k = l; 
            while (i < n1 && j < n2) 
            { 
                if (L[i] <= R[j]) 
                { 
                    arr[k] = L[i]; 
                    i++; 
                } 
                else
                { 
                    arr[k] = R[j]; 
                    j++; 
                } 
                k++; 
            } 

            /* Copy remaining elements of L[] if any */
            while (i < n1) 
            { 
                arr[k] = L[i]; 
                i++; 
                k++; 
            } 

            /* Copy remaining elements of R[] if any */
            while (j < n2) 
            { 
                arr[k] = R[j]; 
                j++; 
                k++; 
            } 
        } 

        // Main function that sorts arr[l..r] using 
        // merge() 
        void sort(int arr[], int l, int r) 
        { 
            if (l < r) 
            { 
                // Find the middle point 
                int m = (l+r)/2; 

                // Sort first and second halves 
                sort(arr, l, m); 
                sort(arr , m+1, r); 

                // Merge the sorted halves 
                merge(arr, l, m, r); 
            } 
        } 
    } 
___ 
### BFS
    List<Double> result = new ArrayList<>();
    Queue<TreeNode> nodes = new LinkedList<>();

    nodes.add(root);
    while(!nodes.isEmpty())
    int n = nodes.size();

    if(node.left != null) nodes.offer(node.left);
    if(node.right != null) nodes.offer(node.right);
    
___ 
### DFS
    pre-order traversal 
        Check if the current node is empty / null.
        Display the data part of the root (or current node).
        Traverse the left subtree by recursively calling the pre-order function.
        Traverse the right subtree by recursively calling the pre-order function.

    in-order traversal
        Check if the current node is empty / null.
        Traverse the left subtree by recursively calling the in-order function.
        Display the data part of the root (or current node).
        Traverse the right subtree by recursively calling the in-order function.

    post-order traversal
        Check if the current node is empty / null.
        Traverse the left subtree by recursively calling the post-order function.
        Traverse the right subtree by recursively calling the post-order function.
        Display the data part of the root (or current node).
