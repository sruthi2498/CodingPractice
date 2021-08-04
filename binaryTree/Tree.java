package binaryTree;

public class Tree{
	public TreeNode root;

	public Tree(){}

	public void insert(int val){
		if(root == null){
			root = new TreeNode(val,null,null);
		}
		else{
			insert(val, root);
		}

	} 
	private void insert(int val, TreeNode temp){
		if(val<=temp.val){
			if(temp.left == null){
				temp.left = new TreeNode(val,null,null);
				System.out.println("inserting "+val + " to left of "+temp.val);
			}
			else{
				insert(val, temp.left);
			}
		}
		else{
			if(temp.right == null){
				temp.right = new TreeNode(val,null,null);
				System.out.println("inserting "+val + " to right of "+temp.val);
			}
			else{
				insert(val, temp.right);
			}
			
		}
	}

	public void Print(){
		if(root!=null){
			Print(root);
		}
		System.out.println();

	}

	private void Print(TreeNode temp){
		System.out.print(temp.val+" ");
		if(temp.left!=null){
			Print(temp.left);
		}
		if(temp.right!=null){
			Print(temp.right);
		}
	}
}





