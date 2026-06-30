class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set <Integer> s = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        if(s.size()<nums.length)
        return true;
        return false;
 
    }
}
