import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/********************************************************
 ********************************************************/
public class Preorder {

    // 前序遍历
    public static List<Integer> preorderTraversal(TreeNode root) {
        // use ArrayList beacuae it is a resizable array
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        while (stack.size() > 0 || root != null){
            if (root != null) {
                res.add(root.val);
                stack.push(root);
                root = root.left;
            }
            else {
                TreeNode tmp = stack.pop();
                root = tmp.right;
            }
        }
        return res;
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
        List<Integer> res = preorderTraversal(n1);
        for (Integer i : res) {
            System.out.println(i);
        }
    }
}

