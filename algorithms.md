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
