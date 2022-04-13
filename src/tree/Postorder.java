import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/********************************************************
 ********************************************************/
public class Postorder {

    // 后序遍历
    public static List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> lst = new LinkedList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();

        while (stk.size() > 0 || root != null) {
            if (root != null) {
                lst.addFirst(root.val);
                stk.push(root);
                root = root.right;
            } else {
                TreeNode tmp = stk.pop();
                root = tmp.left;
            }
        }
        return lst;
    }

    public static void main(String[] args) {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(3);
        TreeNode n3 = new TreeNode(4);
        TreeNode n4 = new TreeNode(4);
        TreeNode n5 = new TreeNode(5);
        TreeNode n6 = new TreeNode(6);
        n1.left = n2;
        n1.right = n3;
        n2.left = n4;
        n2.right = n5;
        n3.left = n6;
        List<Integer> res = postorderTraversal(n1);
        for (Integer i : res) {
            System.out.println(i);
        }
    }
}


