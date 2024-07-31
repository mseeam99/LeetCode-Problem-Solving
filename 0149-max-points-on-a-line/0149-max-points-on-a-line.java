class Solution {
    public int maxPoints(int[][] points) {

        if(points.length <= 2) return points.length;
        final int inf = 999999; 
        int maxPoints = 0;

        for(int i=0; i < points.length; i++){

            Map<Double, Integer> map = new HashMap<>();
            
            for(int j=i+1; j<points.length; j++){
                double slope = 0; 

                // For Avoiding division by 0
                if(points[j][0]-points[i][0] != 0)
                    slope = ((double)(points[j][1]-points[i][1])/(double)(points[j][0]-points[i][0]));

                else 
                    slope = inf; // Assigning slope as infinity incase of division by 0
 
                if(slope == -0.0) slope = 0.0; // because 0.0 and -0.0 are treated as different keys by map. But we want to avoid it.

                map.put(slope, map.getOrDefault(slope, 0)+1);
                maxPoints = Math.max(maxPoints , map.get(slope)+1);
            }
        }
        return maxPoints;
    }
}