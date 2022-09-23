 void printTriangle(int n) {
        int n_spaces = 2*n - 2;
        for(int i = 1; i <= n; i++){
            int temp = i;
            for(int j = 1; j <= i; j++){
                System.out.print(j + " ");
            }
            for(int k = 1; k <= n_spaces; k++){
                System.out.print("  ");
            }
            for(int l = 1; l <= i; l++){
                System.out.print(temp + " ");
                temp -= 1;
            }
            n_spaces -= 2;
            System.out.println();
        }
    }
