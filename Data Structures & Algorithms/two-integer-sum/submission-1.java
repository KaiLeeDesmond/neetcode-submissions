class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> m = new HashMap<>();
        int ans[] = new int[2];
        for(int i=0;i<nums.length;i++)
        {
            m.put(i,nums[i]);
        }

        for(int v:m.values())
        {
            if(m.get(target-v))
            {
                ans[0] = m.get()
            }
            //subtract target and v.
            //check if the diff is present in the map
            //if yes, return the keys

        }


        
    }
}
