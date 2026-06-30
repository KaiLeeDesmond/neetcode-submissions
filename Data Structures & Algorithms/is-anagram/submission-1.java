class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character,Integer> hm = new HashMap <>();
            int new_count = 0;
        for(char c:s.toCharArray())
        {
            hm.put(c,hm.getOrDefault(c,0)+1);
        }

        for(char c:t.toCharArray())
        {
            if(!hm.containsKey(c))
            return false;
            if(hm.containsKey(c))
            new_count = hm.getOrDefault(c,0)-1;
            if(new_count==0)
            hm.remove(c);
            else
            hm.put(c,new_count);
        }

        if(hm.isEmpty())
        return true;
        else
        return false;

    }
}
