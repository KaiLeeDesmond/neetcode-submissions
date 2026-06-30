class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set <Integer> n = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        if (n.size() <nums.length)
        {
            return true;
        }
        return false;

    }
}
