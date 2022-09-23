for(int i=0;i<n;i++){
                if(i%2!=0){
                   boolean one = true;
                   for(int j=0;j<=i;j++){
                       if(one){
                           System.out.print("1 ");
                           one = false;
                       }else{
                           System.out.print("0 ");
                           one = true;
                       }
                   }
                }else{
                     boolean zero = true;
                    for(int j=0;j<=i;j++){
                       
                        if(zero){
                           System.out.print("0 ");
                            zero = false;
                       }else{
                           System.out.print("1 ");
                           zero = true;
                       }
                    }
                }
            System.out.println();
