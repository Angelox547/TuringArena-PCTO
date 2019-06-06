class Solution extends Skeleton {
    int primo(int a){
        int i = 2;
		while( i < a/2+1){
			if(a%i == 0){
				return 0;
			}
			i++;
		}
		return 1;
	}
}




