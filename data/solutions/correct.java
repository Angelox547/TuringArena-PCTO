class Solution extends Skeleton {
    int data(int d, int m, int y){
        int[] day30 = new int[4];
        int[] day31 = new int[7];
        day30[0] = 4;
        day30[1] = 6;
        day30[2] = 9;
        day30[3] = 11;

        day31[0] = 1;
        day31[1] = 3;
        day31[2] = 5;
        day31[3] = 7;
        day31[4] = 8;
        day31[5] = 10;
        day31[6] = 12;

        if (m != 2){
            for (int i = 0; i < 4; i++){
                if (day30[i] == m){
                    if (d > 0 && d < 31 && y > 0){
                        return 1;
                    }
                }
            }

            for(int i = 0; i < 7; i++){
                if (day31[i] == m){
                    if (d > 0 && d < 32 && y > 0){
                        return 1;
                    }
                }
            }
        }

        else if (m == 2){
            if (y > 0 && y % 4 == 0){
                if (d > 0 && d < 30){
                    return 1;
                }
            }

            else if (y > 0 && y % 4 != 0){
                if (d > 0 && d < 29){
                    return 1;
                }
            }
        }
        
        else{
            return 0;
        }
        return 0;
	}
}




