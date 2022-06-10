import java.util.HashMap;
import java.util.Map;

public class Solution003 {
    public static int lengthOfLongestSubstring(String s) {
        int n = s.length(); // length of the string
        int ans = 0; // answer to the leetcode problem 3
        Map<Character, Integer> map = new HashMap<>(); // empty map to store keys and values
        for (int i = 0, j = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(i, map.get(s.charAt(j)));
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }

    public static void main(String[] args) {
        String str = "abba";
        int ans = lengthOfLongestSubstring(str);
        System.out.println(ans);
    }
}
