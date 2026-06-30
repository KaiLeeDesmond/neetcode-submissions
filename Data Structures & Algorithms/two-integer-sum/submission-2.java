class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i]; // The number needed to reach target
            
            if (m.containsKey(complement)) {
                return new int[]{m.get(complement), i}; // Return indices of the two numbers
            }
            
            m.put(nums[i], i); // Store the number as key and index as value
        }
        
        return new int[]{-1, -1}; // Return a default value if no solution is found
    }
}
